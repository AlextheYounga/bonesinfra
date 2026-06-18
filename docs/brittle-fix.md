I scanned the repo. The big picture: the structure is good, but runtime is brittle because failures can be hidden, several operations are not pinned/idempotent enough, and Nuxt is currently registered without actually deploying a runtime.

## Highest-priority fixes

### 1. Stop swallowing runtime import/setup failures

Right now `runtime.py` calls `template_runtime.load(data)` after nginx/AppArmor setup, and then runs doctor.  But `template_runtime.load()` catches `ImportError` and `KeyError` and silently does nothing.  The runtime registry also ignores `ImportError` during discovery.

That is probably your worst runtime brittleness. A broken Laravel/Nuxt module can degrade into “generic nginx static site config started successfully” instead of “runtime deploy failed immediately.”

Change it to fail loudly:

```python
def load(data):
    template = data.get("template")
    if not template:
        raise RuntimeError("Missing required runtime template")

    from bonesinfra.runtimes import get_runtime

    mod = get_runtime(template)
    deploy = getattr(mod, "deploy", None)
    if deploy is None:
        raise RuntimeError(f"Runtime {template!r} has no deploy() function")

    deploy()
```

Also change `_discover()` so it only ignores “module does not exist” for optional runtimes, not import errors inside a runtime module. Silent imports make debugging miserable.

### 2. Nuxt currently does nothing

Nuxt is registered in `_MODULE_PATHS`.  But the actual Nuxt runtime is just:

```python
def deploy():
    pass
```

So today, a Nuxt project will get the generic static nginx config, which serves `{{ paths.current_web_root }}` and falls back to `/index.html`.  That only works for a generated static app. It will not correctly run a Nuxt SSR/Nitro server.

You need to decide whether your Nuxt target is:

**Static Nuxt:** run `pnpm generate`, serve `.output/public`, and set `web_root = ".output/public"`.

**SSR Nuxt:** create a per-site Node systemd service, probably running:

```bash
node .output/server/index.mjs
```

Then nginx should proxy to that service, ideally through a Unix socket or localhost port. In other words, Nuxt needs a parallel to Laravel’s PHP-FPM service, not the base static nginx config.

### 3. Move runtime-specific setup before generic nginx startup

Current runtime plan order is:

```python
packages.install_apt(data)
apparmor.setup(...)
nginx.setup(...)
template_runtime.load(data)
doctor.run(data)
```

This means the generic per-site nginx service starts before Laravel overwrites its config. Laravel then deploys its own nginx config and restarts the per-site nginx service.   That can work, but it increases transient failure states and makes debugging harder.

A less brittle runtime plan would be:

```python
packages.install_apt(data)
apparmor.setup_base(...)
template_runtime.pre_nginx(data)
nginx.setup(data, paths, here)
template_runtime.post_nginx(data)
doctor.run(data)
```

For Laravel, `pre_nginx` would install PHP, render PHP-FPM config, load AppArmor, validate PHP-FPM, and start PHP-FPM. Then nginx is rendered once against the correct final config. For Nuxt SSR, `pre_nginx` would install/validate Node service config and `post_nginx` could restart the app service after nginx validates.

## Laravel-specific issues

Laravel is closer than Nuxt, but I see several failure points.

First, Laravel uses `runtime.toml` default `php_version = "8.5"`.  Your installer then blindly tries to install `php8.5`, `php8.5-cli`, `php8.5-fpm`, etc.  That is brittle. Runtime config should either default to the distro’s supported PHP version or validate that `/usr/sbin/php-fpm{version}` exists after install, before rendering services. You already test PHP-FPM config later, but a clearer preflight would fail with “PHP 8.5 not available from configured apt sources.”

Second, the PHP repo setup uses `packages.sury.org/php` with a distro codename resolved from the host.   That should be guarded by distro detection. If the server is Ubuntu, Debian-style Sury repo assumptions may become fragile. I would add an explicit `php_repo_strategy`:

```toml
php_repo_strategy = "system" # or "ondrej-ppa", "sury-debian", "none"
php_version = "8.3"
```

Then refuse unknown OS/repo combinations.

Third, the Laravel build script puts the app into maintenance mode during build after Composer install.  For release-based deploys, that is not ideal. Build should happen in the new release directory before `current` is switched. Only migrations and final cache warmup should happen near cutover. If `current` already points to the previous working release, you can avoid maintenance mode for most failures.

## Setup brittleness

Setup has a few “works until it doesn’t” operations.

### Live runtime users and `usermod`

One concrete failure showed up during setup with the default runtime account:

```text
usermod: user www-data is currently used by process <pid>
```

The old setup path used `server.user(... groups=[...])` for the runtime user even
when that user already existed. On Linux, pyinfra implements that as `usermod -G`
for existing accounts. That is brittle for built-in service users like `www-data`
because they are often already running nginx, php-fpm, or other long-lived
processes by the time setup runs.

The safer behavior is:

1. Only create the runtime user with `server.user(...)` when it does not already exist.
2. For an existing runtime user, avoid rewriting the whole account.
3. Add any missing supplementary groups with group-membership commands such as:

```bash
id -nG www-data | tr ' ' '\n' | grep -Fxq deployers || gpasswd -a www-data deployers
```

That keeps setup idempotent without taking down a live service account just to
change supplementary group membership.

`install_rust()` always runs the rustup curl installer as root.  `bonesremote.install()` then installs from the live Git repo via Cargo using the current remote HEAD.  That means setup can change behavior depending on whatever is currently in `bonesdeploy.git`. Pin this to a tag, branch, or commit:

```toml
bonesremote_version = "v0.3.2"
```

Then:

```bash
cargo install --locked --root /usr/local --git "$repo" --tag "$version" bonesremote
```

Also, `git init --bare` is run every setup.  It is not catastrophic, but setup should distinguish “create repo” from “repo exists.” A better operation would check for `HEAD`, validate it is a bare repo, and refuse to overwrite if the path exists but is not a bare Git repo.

## Isolation comments

The systemd hardening is a good start. Your per-site nginx service runs as the runtime user, uses an AppArmor profile, restricts address families to Unix sockets, uses `ProtectSystem=strict`, and only allows writes to the runtime socket dir.   Laravel PHP-FPM has similar hardening and only grants read/write paths for the socket dir and Laravel storage.

The main gap is that “runtime correctness” is not yet checked strongly enough. `bonesremote doctor` runs at the end as the deploy user.  I would make doctor runtime-aware and very concrete:

```bash
systemctl is-active <project>-nginx
test -S /run/<project>/nginx.sock
curl --unix-socket /run/<project>/nginx.sock http://localhost/

# Laravel
systemctl is-active <project>-php-fpm
test -S /run/<project>/php-fpm.sock
php <current>/artisan about --no-interaction

# Nuxt SSR
systemctl is-active <project>-nuxt
curl --unix-socket /run/<project>/nuxt.sock http://localhost/
```

## Practical priority order

Do these first:

1. Make runtime loading fail loudly.
2. Implement actual Nuxt runtime or explicitly mark it unsupported unless static mode is selected.
3. Reorder runtime deployment so runtime-specific services are prepared before nginx starts.
4. Pin `bonesremote` install instead of building from live Git HEAD.
5. Add runtime doctor checks for sockets, systemd units, and HTTP responses.
6. Change Laravel PHP config from “assume version/repo works” to explicit distro/repo/version validation.
7. Ensure package data includes templates, `.toml`, and shell scripts if this is installed as a package; `pyproject.toml` currently defines dependencies and package-dir but no package-data rules for the Jinja templates/runtime assets.

My strongest guess: your runtime issues are mostly from silent runtime skips, Nuxt having no implementation, and services being started before the runtime-specific config is fully known.
