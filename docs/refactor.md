I read through the current `bonesinfra` shape. The repo is small, but it is already showing the same kind of boundary drift as `bonesdeploy`.

The biggest issue: **`main.py` is doing too much.** It is the CLI entrypoint, runtime catalog interface, config loader, path builder, deploy data builder, validation layer, and pyinfra dispatcher all in one file. It also manually mutates `sys.path`, which is a sign this is not yet a real package boundary.

There is also some stale identity: `pyproject.toml` still names the project `infra`, uses placeholder description text, and exposes a script named `bones`.  That should become clearly `bonesinfra`, even if it remains hidden from users.

# Current problems I’d fix conceptually

## 1. Entrypoint owns too much

`main.py` defines Typer apps, runtime commands, setup/runtime/ssl apply commands, config parsing, runtime config merging, path construction, validation, and pyinfra execution. The `_load_deploy_config` function alone loads TOML, extracts config fields, builds deployment paths, merges runtime config, adds SSL fields, and returns pyinfra data.

That should be split. CLI code should not build deployment data. It should call application services.

## 2. Data flow is confused

Rust currently sends JSON into stdin for setup/ssl, but `main.py` does not appear to read stdin in `setup_apply` or `ssl_apply`; those functions call `_load_deploy_config` from the config path and ignore stdin entirely.

That means values Rust computed, like `deploy_authorized_key`, may not actually reach Python unless they are also present in the TOML. That needs to be clarified fast.

Pick one rule:

```text
Either Python reads config + stdin overrides,
or Rust stops sending stdin.
```

Given the current architecture, I would choose:

```text
Python reads config, runtime config, and optional JSON stdin overrides.
```

That gives Rust a clean way to pass computed values without forcing them into user config.

## 3. Pyinfra deploy scripts mix orchestration and operations

`setup.py` is a full deploy plan and also contains raw operations for packages, Rust install, users/groups, repo directories, placeholder release, SSH key install, firewall, and bonesremote installation.

`runtime.py` does the same for runtime packages, AppArmor, nginx, template runtime loading, and doctor checks.

This is okay for early scripting, but it gets hard to reason about. Each file should become a deploy plan that delegates to smaller operation modules.

## 4. Runtime registry hides failure

The runtime registry catches `ImportError` and silently skips missing runtime modules.  `runtime.py` also catches `(ImportError, KeyError)` when loading template runtime deploy code and silently passes.

That makes debugging painful. Missing runtime code should be explicit, especially now that Rust depends on Python for runtime questions/defaults/apply.

## 5. There are already bug-shaped seams

Laravel has:

```python
add_php_apt_source(php_version)
```

but the function is defined as:

```python
def add_php_apt_source():
```

That kind of issue is exactly what happens when runtime modules are too loose and not covered by simple structural tests.

## 6. `paths.py` is duplicating Rust shared paths

`paths.py` reimplements a large chunk of the same deployment path model that exists in Rust. It contains defaults, nginx/systemd/AppArmor paths, release paths, socket paths, binary paths, and the full `DeploymentPaths` dataclass.

Some duplication may be acceptable, but this should be treated as a **contract**, not casual copy-paste. Either Python owns a mirrored version with tests against known fixtures, or Rust passes `paths` and Python trusts them.

Given the current direction, I would lean toward:

```text
Rust owns path derivation.
Python accepts paths in DeployContext.
Python only derives paths as fallback/dev convenience.
```

# Proposed clean structure

I’d move toward this package shape:

```text
bonesinfra/
  pyproject.toml
  README.md

  src/bonesinfra/
    __init__.py
    __main__.py

    cli/
      __init__.py
      app.py
      runtime.py
      setup.py
      ssl.py

    app/
      __init__.py
      setup_apply.py
      runtime_apply.py
      ssl_apply.py
      runtime_catalog.py

    domain/
      __init__.py
      config.py
      context.py
      paths.py
      runtime.py
      questions.py

    infra/
      __init__.py
      pyinfra_runner.py
      toml_store.py
      stdin_json.py

    deploys/
      __init__.py

      setup/
        __init__.py
        plan.py
        packages.py
        users.py
        directories.py
        placeholder.py
        firewall.py
        bonesremote.py

      runtime/
        __init__.py
        plan.py
        packages.py
        apparmor.py
        nginx.py
        template_runtime.py
        doctor.py

      ssl/
        __init__.py
        plan.py
        nginx.py
        certbot.py

    runtimes/
      __init__.py
      registry.py

      laravel/
        __init__.py
        metadata.py
        deploy.py
        php_repo.py
        php_fpm.py
        nginx.py
        apparmor.py
        assets/

      django/
        __init__.py
        metadata.py
        deploy.py

      rails/
        __init__.py
        metadata.py
        deploy.py

    assets/
      nginx/
      apparmor/
```

Not all of this has to happen immediately. But that is the shape I would aim for.

# Boundary rules

## `cli/`

Owns Typer only.

Allowed:

```text
Typer app creation
argument definitions
calling app services
printing JSON results
turning exceptions into exit codes
```

Not allowed:

```text
pyinfra imports
path derivation
TOML parsing details
runtime module discovery details
deployment plan logic
```

## `app/`

Owns use-case orchestration.

Examples:

```text
apply setup
apply runtime
apply SSL
list runtimes
get runtime questions
get runtime defaults
```

This is where CLI calls should land.

## `domain/`

Owns typed data.

Important object:

```python
@dataclass
class DeployContext:
    host: str
    ssh_user: str
    ssh_port: int
    data: dict[str, Any]
    paths: DeploymentPaths
    runtime: dict[str, Any]
```

The main point is: build the deploy context once, then pass it around. Do not reconstruct `data`, `paths`, `runtime`, and SSL fields in every command.

## `infra/`

Owns external machinery.

Examples:

```text
pyinfra runner
TOML loading
stdin JSON loading
maybe package/resource lookup
```

`pyinfra_runner.py` already mostly belongs here. It is a clean adapter shape: it receives hostname, SSH user/port, data, and a deploy callable, then configures pyinfra and runs operations.

## `deploys/`

Owns top-level pyinfra deployment plans.

Instead of `src/setup.py`, `src/runtime.py`, and `src/ssl.py` as giant-ish files, make them plans:

```python
def deploy():
    ctx = current_context()
    packages.install_base(ctx)
    users.ensure_users_and_groups(ctx)
    directories.setup_repo_and_project_dirs(ctx)
    placeholder.seed(ctx)
    firewall.configure(ctx)
    bonesremote.install(ctx)
```

The plan reads like the deployment story. The operation modules hold the raw pyinfra calls.

## `runtimes/`

Owns runtime-specific behavior.

Each runtime should have a consistent small interface:

```python
def metadata() -> RuntimeMetadata
def questions() -> list[Question]
def defaults() -> dict
def deploy(ctx: DeployContext) -> None
```

Right now runtime modules are uneven. Django and Rails are small package installers.   Laravel is much larger and mixes questions, runtime config loading, PHP repo setup, package installation, storage directories, PHP-FPM, AppArmor, nginx, and systemd.  That should be split inside the Laravel runtime folder.

# Refactor order I recommend

## Pass 1: Package identity cleanup

Small, obvious, high leverage.

```text
- Rename project from "infra" to "bonesinfra"
- Replace script name "bones" with "bonesinfra" or remove public script entirely
- Move root main.py toward src/bonesinfra/__main__.py
- Remove sys.path mutation
```

Current `pyproject.toml` still says `name = "infra"` and `bones = "main:main"`.  Fixing that makes the repo feel real.

## Pass 2: Split CLI from app logic

Move Typer declarations into:

```text
src/bonesinfra/cli/app.py
```

Move the actual behavior into:

```text
src/bonesinfra/app/runtime_catalog.py
src/bonesinfra/app/setup_apply.py
src/bonesinfra/app/runtime_apply.py
src/bonesinfra/app/ssl_apply.py
```

After this pass, CLI functions should be tiny wrappers.

## Pass 3: Create `DeployContext`

Extract `_load_deploy_config` out of `main.py` into something like:

```text
domain/context.py
```

It should do one thing: load config, runtime config, optional stdin overrides, and produce a context object.

This is also where you fix the stdin ambiguity.

Suggested behavior:

```text
DeployContext.from_files(
    bones_toml,
    runtime_toml=None,
    ssh_user="root",
    stdin_overrides=None,
)
```

Then `setup`, `runtime`, and `ssl` all use the same path.

## Pass 4: Turn `setup.py`, `runtime.py`, `ssl.py` into plans

Keep behavior the same, but split helpers into modules.

Example:

```text
deploys/setup/plan.py
deploys/setup/packages.py
deploys/setup/users.py
deploys/setup/directories.py
deploys/setup/firewall.py
deploys/setup/bonesremote.py
```

No new abstraction needed. Just move functions by concern.

## Pass 5: Split Laravel runtime

Laravel is already large enough to become a mini-package:

```text
runtimes/laravel/metadata.py
runtimes/laravel/deploy.py
runtimes/laravel/php_repo.py
runtimes/laravel/php_packages.py
runtimes/laravel/php_fpm.py
runtimes/laravel/apparmor.py
runtimes/laravel/nginx.py
```

Also fix the `add_php_apt_source(php_version)` mismatch during this pass.

## Pass 6: Runtime registry cleanup

Replace silent import skipping with explicit registry entries.

Current registry catches `ImportError` and silently ignores missing modules.  I would change that to fail in tests and be explicit at runtime.

Something like:

```python
RUNTIMES = {
    "laravel": RuntimeSpec(...),
    "django": RuntimeSpec(...),
}
```

If a runtime is listed but broken, tests should fail.

## Pass 7: Add clean-code tests

Add simple tests that scan the repo, similar to what you did in Rust.

Tests I would add:

```text
- main/CLI files must not import pyinfra
- app files must not import pyinfra.operations directly
- domain files must not import pyinfra
- runtime registry must import every declared runtime
- every runtime must expose questions/defaults/deploy or an explicit no-op deploy
- no silent except ImportError/pass in runtime loading
- no sys.path mutation
- no file over 300-400 lines
- setup/runtime/ssl plan files should stay small
```

# What not to do yet

Do not overbuild a framework.

I would avoid:

```text
- abstract base classes everywhere
- dependency injection framework
- plugin loader magic
- dynamic filesystem discovery
- packaging as zipapp/PEX in this pass
- rewriting all pyinfra operations into classes
```

The immediate goal is just:

```text
CLI thin
context explicit
deploy plans readable
operations grouped
runtime modules consistent
```

# Blunt summary

The repo should become:

```text
Typer CLI -> app service -> deploy context -> pyinfra plan -> grouped operations
```

Right now it is closer to:

```text
main.py -> everything
setup/runtime/ssl.py -> everything else
runtime modules -> whatever shape each one happens to have
```

The next clean pass should not change what BonesInfra does. It should make it obvious **where each kind of code belongs**.
