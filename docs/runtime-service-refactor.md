Yes. After checking `src/bonesinfra/runtimes`, the clean path is to define **one common isolation substrate**, then implement each framework as a thin adapter on top of it.

Right now the registry exposes seven runtimes: `laravel`, `django`, `next`, `nuxt`, `rails`, `sveltekit`, and `vue`.  But only Laravel is close to a real isolated runtime: it installs PHP packages, configures PHP-FPM, AppArmor, and nginx.  Django and Rails only install apt packages; they do not create app services.   Next, Nuxt, SvelteKit, and Vue are currently empty `pass` stubs.

## The core design

Every runtime should produce the same kind of isolated unit:

```text
/srv/sites/<project>/
├── current -> releases/<release>
├── shared/
├── releases/
└── build/

/srv/conf/<project>/
├── nginx.conf
├── <runtime>.service config files
└── env files if needed

/run/<project>/
├── nginx.sock
├── app.sock
├── pids
└── temporary runtime files

/var/log/bonesdeploy/<project>/
├── nginx-access.log
├── nginx-error.log
├── app-error.log
└── framework-specific logs
```

Each app runtime should have:

```text
systemd service:
  User=<runtime_user>
  Group=<runtime_group>
  SupplementaryGroups=<release_group>
  WorkingDirectory=/srv/sites/<project>/current
  RuntimeDirectory=<project>
  ReadOnlyPaths=/srv/sites/<project>/current
  ReadWritePaths=/run/<project> /srv/sites/<project>/current/storage-or-equivalent /var/log/bonesdeploy/<project>
  ProtectSystem=strict
  ProtectHome=yes
  PrivateTmp=yes
  RestrictAddressFamilies=AF_UNIX
  AppArmorProfile=bonesdeploy-<project>-<runtime>
```

Laravel already shows the rough model: the PHP-FPM systemd unit runs as the runtime user, uses a per-project runtime directory, has an AppArmor profile, and limits writable paths.   The problem is that this pattern needs to become **generic**, not Laravel-only.

## Fix the runtime loader first

Before adding more runtimes, remove this:

```python
try:
    ...
except (ImportError, KeyError):
    pass
```

`template_runtime.load()` silently hides broken runtime implementations.  That is deadly for provisioning. If Django, Rails, or Next fails to import or deploy, runtime apply should fail loudly. Silent failure is how you end up thinking a runtime was applied when nothing happened.

Replace it with:

```python
def load(ctx):
    template = ctx.runtime.runtime_data.get("template")
    if not template:
        return

    from bonesinfra.runtimes import get_runtime

    runtime = get_runtime(template)
    if not hasattr(runtime, "deploy"):
        raise RuntimeError(f"Runtime {template} does not expose deploy(ctx)")

    runtime.deploy(ctx)
```

## Add a common runtime service layer

Create something like:

```text
src/bonesinfra/runtimes/common/
├── __init__.py
├── service.py
├── nginx.py
├── apparmor.py
├── logs.py
├── node.py
├── python.py
└── ruby.py
```

The goal is not abstraction for its own sake. The goal is to avoid seven runtimes each inventing their own systemd/AppArmor/nginx model.

`common.service` should render a generic app service:

```ini
[Unit]
Description={{ runtime_label }} for {{ project_name }}
After=network.target apparmor.service
Requires=apparmor.service

[Service]
Type=simple
User={{ runtime_user }}
Group={{ runtime_group }}
SupplementaryGroups={{ release_group }}
WorkingDirectory={{ paths.current }}
RuntimeDirectory={{ project_name }}
RuntimeDirectoryMode=0750
EnvironmentFile=-{{ paths.conf_root }}/runtime.env
ExecStart={{ runtime_exec }}

AppArmorProfile={{ apparmor_profile_name }}

NoNewPrivileges=yes
PrivateTmp=yes
ProtectHome=yes
ProtectSystem=strict
RestrictNamespaces=yes
LockPersonality=yes
RestrictRealtime=yes
SystemCallArchitectures=native
CapabilityBoundingSet=
AmbientCapabilities=
PrivateDevices=yes
ProtectKernelTunables=yes
ProtectKernelModules=yes
ProtectControlGroups=yes
RestrictAddressFamilies=AF_UNIX

ReadOnlyPaths={{ paths.current }}
ReadWritePaths={{ paths.runtime_socket_dir }} {{ runtime_write_paths }} /var/log/bonesdeploy/{{ project_name }}

StandardOutput=journal
StandardError=journal
Restart=always
RestartSec=2

[Install]
WantedBy=multi-user.target
```

Then each runtime only supplies:

```python
runtime_exec
socket_path
runtime_write_paths
packages
nginx mode
apparmor allowances
validation command
```

## Runtime-by-runtime plan

### Laravel

Laravel should keep the PHP-FPM model, but stabilize it. The PHP-FPM config is currently a full `--fpm-config` file even though it is named like a pool file.  Rename it to `php-fpm.conf.j2`, add explicit logs/pid under `/run/<project>` or `/var/log/bonesdeploy/<project>`, and validate as the runtime user, not just root.

Laravel runtime shape:

```text
service: <project>-php-fpm.service
socket: /run/<project>/php-fpm.sock
nginx: fastcgi_pass unix:/run/<project>/php-fpm.sock
writable:
  /srv/sites/<project>/current/storage
  /srv/sites/<project>/current/bootstrap/cache
  /run/<project>
  /var/log/bonesdeploy/<project>
```

### Django

Django should use Gunicorn behind nginx over a Unix socket. Gunicorn’s own deployment docs strongly recommend running it behind a proxy server, advise nginx, and show Unix socket proxying with systemd. ([Gunicorn][1])

Django runtime shape:

```text
service: <project>-gunicorn.service
socket: /run/<project>/gunicorn.sock
exec: /srv/sites/<project>/current/.venv/bin/gunicorn <module>.wsgi:application --bind unix:/run/<project>/gunicorn.sock
nginx: proxy_pass http://unix:/run/<project>/gunicorn.sock
writable:
  /run/<project>
  /var/log/bonesdeploy/<project>
  optional media/static dirs if configured
```

Runtime questions should include:

```text
wsgi_module: "config.wsgi:application" or "<project>.wsgi:application"
python_version
install_postgres
static_root
media_root
```

Do not use the distro `python3-gunicorn` package as the final app server if the project has a venv. Gunicorn’s docs explicitly say that for a virtualenv deployment, it is generally easiest to install Gunicorn into the virtualenv and run that script. ([Gunicorn][1])

### Rails

Rails should use Puma as the app server, over a Unix socket. The current Rails runtime only installs Ruby packages.  It needs a per-site Puma systemd service.

Rails runtime shape:

```text
service: <project>-puma.service
socket: /run/<project>/puma.sock
exec: bundle exec puma -e production -b unix:///run/<project>/puma.sock
nginx: proxy_pass http://unix:/run/<project>/puma.sock
writable:
  /run/<project>
  /var/log/bonesdeploy/<project>
  /srv/sites/<project>/current/tmp
  /srv/sites/<project>/current/log
  /srv/sites/<project>/current/storage
```

Runtime questions:

```text
ruby_version
install_postgres
install_redis
rails_env = production
```

### Next.js

For Next, prefer standalone output. Next’s docs say `output: 'standalone'` creates `.next/standalone` with only the files needed for production, plus a minimal `server.js`; they also document running it with `node .next/standalone/server.js` and setting `PORT`/`HOSTNAME`. ([Next.js][2])

Next runtime shape:

```text
service: <project>-next.service
socket: probably TCP localhost first, Unix socket later if supported by wrapper
exec: node .next/standalone/server.js
env:
  NODE_ENV=production
  PORT=<internal port>
  HOSTNAME=127.0.0.1
nginx: proxy_pass http://127.0.0.1:<internal port>
writable:
  /run/<project>
  /var/log/bonesdeploy/<project>
  optional .next/cache if ISR/cache is enabled
```

For strict isolation, Unix sockets are ideal, but Next’s documented standalone server speaks in terms of `PORT` and `HOSTNAME`, not a standard socket env. ([Next.js][2]) So start with `127.0.0.1:<allocated_port>` unless you add a small wrapper server.

### Nuxt

Nuxt/Nitro can run as a standalone Node output. Nitro docs say the Node server preset outputs a ready-to-run Node server at `.output/server/index.mjs`, and environment variables include `NITRO_PORT`/`PORT`, `NITRO_HOST`/`HOST`, and `NITRO_UNIX_SOCKET`. ([Nitro][3])

Nuxt runtime shape:

```text
service: <project>-nuxt.service
socket: /run/<project>/nuxt.sock
exec: node .output/server/index.mjs
env:
  NODE_ENV=production
  NITRO_UNIX_SOCKET=/run/<project>/nuxt.sock
nginx: proxy_pass http://unix:/run/<project>/nuxt.sock
writable:
  /run/<project>
  /var/log/bonesdeploy/<project>
```

Nuxt is cleaner than Next for your architecture because Nitro officially supports a Unix socket env.

### SvelteKit

SvelteKit with `adapter-node` runs with `node build`, and the docs say `SOCKET_PATH` can be used to serve over a Unix socket. ([Svelte][4]) It also needs production env handling: SvelteKit docs say production `.env` files are not automatically loaded unless you use `dotenv` or Node’s `--env-file`. ([Svelte][4])

SvelteKit runtime shape:

```text
service: <project>-sveltekit.service
socket: /run/<project>/sveltekit.sock
exec: node --env-file=.env build
env:
  NODE_ENV=production
  SOCKET_PATH=/run/<project>/sveltekit.sock
  ORIGIN=https://<domain>
nginx: proxy_pass http://unix:/run/<project>/sveltekit.sock
writable:
  /run/<project>
  /var/log/bonesdeploy/<project>
```

SvelteKit also documents `ORIGIN`, `PROTOCOL_HEADER`, and `HOST_HEADER` for reverse proxy correctness. ([Svelte][4])

### Vue

Vue should not have a runtime service by default. It is normally a static Vite build. Vite’s docs say the default production output is `dist`, and `vite preview` is intended for local preview, not as a production server. ([vitejs][5])

Vue runtime shape:

```text
service: none
nginx: serve static files from /srv/sites/<project>/current/dist
writable:
  none, usually
```

So Vue is the first example of an isolated runtime that is isolated by **not having a process**. The nginx per-site service already isolates the serving layer.

## Structural change I’d make

Change each runtime from this loose shape:

```python
def questions(): ...
def deploy(ctx): ...
```

to a tiny module that declares its type:

```python
RUNTIME = {
    "name": "django",
    "kind": "wsgi",
    "app_service": True,
    "socket_name": "gunicorn.sock",
    "questions": [...],
}
```

Then `deploy(ctx)` can call common helpers:

```python
def deploy(ctx):
    paths = runtime_paths(ctx)
    python.install_packages(ctx)
    logs.ensure(ctx)
    apparmor.render_app_profile(ctx, runtime="gunicorn")
    service.render_app_service(
        ctx,
        name="gunicorn",
        exec="/srv/sites/.../.venv/bin/gunicorn ...",
        socket="/run/<project>/gunicorn.sock",
        writable_paths=[...],
    )
    nginx.render_proxy(ctx, socket="/run/<project>/gunicorn.sock")
    service.validate_as_runtime_user(...)
    service.enable_and_start(...)
```

The important rule is: **all dynamic/server runtimes should converge on “one app service + one socket + one nginx proxy + one AppArmor profile.”** Static runtimes should converge on “no app service + nginx static root.”

## Implementation order

Start with Laravel because it is already closest. Fix PHP-FPM logs, rename the FPM template, create `/var/log/bonesdeploy/<project>`, and validate as runtime user.

Second, implement the common service/log/AppArmor helpers and move Laravel onto them without changing behavior too much.

Third, implement SvelteKit and Nuxt because they naturally support Unix sockets. Nitro supports `NITRO_UNIX_SOCKET`; SvelteKit supports `SOCKET_PATH`. ([Nitro][3]) ([Svelte][4])

Fourth, implement Django with Gunicorn over a Unix socket.

Fifth, implement Rails with Puma over a Unix socket.

Sixth, implement Next with `127.0.0.1:<port>` first, unless you decide to introduce a local wrapper that can bind a Unix socket.

Seventh, implement Vue as static-only.

The end state should be boring: every runtime either produces a service behind a private socket or static files behind the per-site nginx service. No global PHP-FPM pool, no global Puma, no global Gunicorn, no shared Node service, no framework process listening publicly on TCP.

[1]: https://docs.gunicorn.org/en/stable/deploy.html "Deploying Gunicorn — Gunicorn 23.0.0 documentation"
[2]: https://nextjs.org/docs/app/api-reference/config/next-config-js/output "next.config.js: output | Next.js"
[3]: https://nitro.build/deploy/runtimes/node "Node.js - Nitro"
[4]: https://svelte.dev/docs/kit/adapter-node "Node servers • SvelteKit Docs"
[5]: https://vite.dev/guide/static-deploy.html "Deploying a Static Site | Vite"
