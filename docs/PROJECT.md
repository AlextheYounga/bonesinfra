# BonesInfra Project Notes

BonesInfra is the hidden Python provisioning engine for BonesDeploy.

It is not the public product interface. It is called by `bonesdeploy` to run pyinfra-based provisioning, runtime setup, SSL setup, and runtime-specific infrastructure tasks.

The user should normally never call `bonesinfra` directly, except for dev testing.

---

# Role in the System

BonesDeploy is split into three cooperating systems:

```text
bonesdeploy
  Local Rust CLI.
  Public user interface.

bonesremote
  Remote Rust release lifecycle executor.

bonesinfra
  Hidden Python/pyinfra provisioning engine.
```

BonesInfra owns provisioning.

BonesRemote owns deployment.

BonesDeploy owns public UX.

---

# What BonesInfra Owns

BonesInfra owns:

- pyinfra API integration
- setup provisioning
- runtime provisioning
- SSL provisioning
- runtime catalog
- runtime questions/defaults
- framework-specific infrastructure
- Jinja2 templates used by provisioning
- runtime package installation
- runtime services
- nginx/AppArmor/systemd provisioning details

BonesInfra does not own:

- public user UX
- local project initialization
- `.bones` scaffold ownership
- git hook lifecycle
- release activation
- release rollback
- release pruning
- source checkout
- build workspace lifecycle
- deployment script execution

Those belong to `bonesdeploy` and `bonesremote`.

---

# Public vs Private Interface

BonesInfra exposes a command-line interface because Rust needs a stable process boundary.

That CLI is private.

Current script entrypoint:

```text
bonesinfra = "bonesinfra.__main__:main"
```

Expected private command shapes:

```sh
bonesinfra runtime list
bonesinfra runtime questions <runtime>
bonesinfra setup apply --config <bones.toml> [--ssh-user root]
bonesinfra runtime apply --config <bones.toml> --runtime-config <runtime.toml> --ssh-user <user>
bonesinfra ssl apply --config <bones.toml> [--ssh-user root]
```

This command surface is an internal contract with `bonesdeploy`.

Do not treat it as public user-facing API unless that decision is made deliberately later.

---

# Package Layout

BonesInfra uses a `src/` Python package layout.

Expected structure:

```text
bonesinfra/
├── pyproject.toml
├── README.md
├── PROJECT.md
└── src/
    └── bonesinfra/
        ├── __init__.py
        ├── __main__.py
        ├── cli/
        ├── app/
        ├── domain/
        ├── infra/
        ├── deploys/
        ├── runtimes/
        └── assets/
```

The outer `bonesinfra/` is the repository.

The inner `src/bonesinfra/` is the importable Python package.

The package should run through:

```sh
python -m bonesinfra
```

or through the installed script:

```sh
bonesinfra
```

Avoid `sys.path` mutation.

Avoid root-level script architecture.

---

# Layer Responsibilities

## `cli/`

Owns Typer command definitions.

Allowed:

- declare commands
- declare arguments/options
- call app services
- print JSON for query commands

Not allowed:

- pyinfra operations
- TOML parsing details
- path derivation
- direct deploy plan logic
- runtime module loading internals
- server provisioning logic

CLI should stay thin.

Example:

```python
def setup_apply_cmd(config: str, ssh_user: str = "root"):
    setup_apply.apply(config, ssh_user)
```

## `app/`

Owns use-case orchestration.

Examples:

```text
app/setup_apply.py
app/runtime_apply.py
app/ssl_apply.py
app/runtime_catalog.py
```

Responsibilities:

- load deploy context
- validate use-case-level requirements
- call the correct deploy plan
- call the pyinfra runner through `app.apply`

App code may know that setup uses `deploys.setup.plan`.

App code should not contain raw pyinfra operations.

## `domain/`

Owns stable data concepts.

Examples:

```text
domain/context.py
domain/paths.py
domain/runtime.py
domain/questions.py
```

Responsibilities:

- represent deploy context
- represent derived deployment paths
- represent runtime questions/defaults
- normalize config data
- keep data-shaping logic testable

Domain code should not import pyinfra.

## `infra/`

Owns external machinery.

Examples:

```text
infra/pyinfra_runner.py
infra/toml_store.py
infra/stdin_json.py
```

Responsibilities:

- run pyinfra programmatically
- load TOML files
- read stdin JSON overrides if supported
- bridge app services to external libraries

Infra code may import pyinfra.

App/domain/CLI should avoid direct pyinfra dependency.

## `deploys/`

Owns pyinfra deploy plans.

Expected shape:

```text
deploys/
├── setup/
│   ├── plan.py
│   ├── packages.py
│   ├── users.py
│   ├── directories.py
│   ├── firewall.py
│   └── bonesremote.py
├── runtime/
│   ├── plan.py
│   ├── packages.py
│   ├── apparmor.py
│   ├── nginx.py
│   ├── template_runtime.py
│   └── doctor.py
└── ssl/
    ├── plan.py
    ├── nginx.py
    └── certbot.py
```

Deploy plan files should read like stories.

Example:

```python
def deploy_setup():
    install_system_packages()
    install_rust()
    ensure_users_and_groups()
    setup_repo_and_project_dirs()
    seed_placeholder_release()
    install_authorized_key()
    setup_firewall()
    install_bonesremote()
```

Raw pyinfra operations should live in focused modules.

## `runtimes/`

Owns runtime-specific infrastructure.

Examples:

```text
runtimes/
├── registry.py
├── laravel/
├── django/
├── rails/
├── next/
├── sveltekit/
└── vue/
```

Each runtime should expose a consistent interface.

Recommended interface:

```python
def questions() -> list[dict]:
    ...

def defaults() -> dict:
    ...

def deploy() -> None:
    ...
```

A runtime may have a no-op deploy, but it should be explicit.

Avoid silent runtime import failure.

---

# Deploy Context

`DeployContext` is the main object passed from app services into pyinfra plans.

It should represent:

```text
host
ssh_user
ssh_port
flat_data
```

`flat_data` is the data passed into pyinfra host data.

It should include fields such as:

```text
project_name
project_root
web_root
repo_path
deploy_user
runtime_user
runtime_group
release_group
project_root_parent
ssh_port
paths
ssl_domain
ssl_email
```

Runtime config values may be merged into `flat_data`.

`paths` should contain derived deployment paths.

Long-term, this shape should be covered by a contract fixture shared with `bonesdeploy`.

---

# Rust/Python Contract

BonesInfra speaks a private contract with BonesDeploy.

The contract should define:

- command names
- stdin JSON shape
- stdout JSON shape
- runtime list response
- runtime questions response
- runtime defaults response
- deploy context shape
- error/exit behavior

Recommended files:

```text
contracts/
├── bonesinfra-api.md
├── bonesinfra-contract.toml
├── schemas/
│   ├── deploy-context.schema.json
│   ├── runtime-list.schema.json
│   ├── runtime-questions.schema.json
│   └── runtime-defaults.schema.json
└── fixtures/
    ├── bones.toml
    ├── runtime.laravel.toml
    ├── deploy-context.setup.json
    ├── deploy-context.runtime.json
    └── deploy-context.ssl.json
```

Both `bonesdeploy` and `bonesinfra` should test against the same contract fixtures.

Do not let Rust and Python agree only by coincidence.

---

# Runtime Catalog

The runtime catalog should be explicit.

Avoid silent import failure.

Bad:

```python
try:
    import runtime
except ImportError:
    pass
```

Good:

```python
RUNTIMES = {
    "laravel": RuntimeSpec(...),
    "django": RuntimeSpec(...),
}
```

If a declared runtime is broken, tests should fail.

Runtime query commands should return stable JSON:

```sh
bonesinfra runtime list
bonesinfra runtime questions laravel
```

Expected `runtime list` response:

```json
["django", "laravel", "next", "rails", "sveltekit", "vue"]
```

Expected `runtime questions` response:

```json
[
  {
    "key": "php_version",
    "type": "choice",
    "label": "PHP version",
    "choices": ["8.2", "8.3", "8.4"],
    "default": "8.3"
  }
]
```

Rust depends on this data to prompt users.

---

# PyInfra Runner

The pyinfra runner is an infrastructure adapter.

It should:

- create pyinfra config
- create inventory
- attach host data
- connect
- execute deploy plan
- run operations
- return nonzero exit on pyinfra failure

It should not know about Laravel, SSL, nginx, config files, or runtime selection.

---

# Setup Provisioning

Setup provisioning prepares the machine.

Responsibilities:

- install base packages
- install Rust/cargo if needed
- ensure deploy user
- ensure runtime user
- ensure runtime group
- ensure release group
- create bare repo parent
- initialize bare git repo
- create repo bones directory
- create project root
- create releases directory
- create build directory
- create shared directory
- seed placeholder release
- install deploy authorized key
- configure firewall
- install `bonesremote`
- run `bonesremote init`

Setup should run as root or bootstrap SSH user.

---

# Runtime Provisioning

Runtime provisioning prepares per-site services.

Responsibilities:

- install runtime apt packages
- configure AppArmor
- configure nginx router
- configure per-site nginx service
- run runtime-specific deploy operations
- run remote doctor check

Runtime setup is separate from SSL.

---

# SSL Provisioning

SSL provisioning obtains and enables certificates.

Responsibilities:

- render HTTP challenge config
- run certbot webroot challenge
- render HTTPS config
- validate nginx
- reload nginx

SSL is intentionally separate from runtime setup.

---

# Runtime-Specific Infrastructure

Runtime modules should be small and grouped by concern.

Example Laravel layout:

```text
runtimes/laravel/
├── __init__.py
├── metadata.py
├── deploy.py
├── php_repo.py
├── php_packages.py
├── php_fpm.py
├── apparmor.py
├── nginx.py
└── assets/
```

Laravel should not be one giant file.

Django, Rails, Node, Vue, etc. can stay small, but they should still follow the same interface.

---

# Error Rules

Prefer explicit failure.

Do not silently skip broken runtime modules.

Do not silently ignore missing required config values.

Do not print success if pyinfra reports failure.

Recommended exit behavior:

```text
0 = success
1 = pyinfra/deploy failure
3 = invalid input/config
```

Keep exact codes simple unless the contract defines more.

---

# Testing Rules

Add tests that enforce boundaries.

Suggested tests:

```text
- cli/ files do not import pyinfra
- domain/ files do not import pyinfra
- app/ files do not import pyinfra.operations
- runtime registry imports every declared runtime
- every runtime exposes questions/defaults/deploy or explicit no-op deploy
- runtime question JSON matches contract schema
- deploy context fixture parses
- no sys.path mutation
- no source file over 300-400 lines
```

The goal is not purity.

The goal is preventing the repo from turning back into:

```text
main.py does everything
setup.py does everything else
runtime modules all have different shapes
```

---

# Documentation Rules

Do not document BonesInfra as public user-facing UX.

Do document it as:

```text
hidden Python provisioning engine for BonesDeploy
```

Avoid saying:

```text
users should run bonesinfra
bonesinfra owns deployment
bonesinfra owns git hooks
bonesinfra owns release activation
```

Prefer saying:

```text
bonesdeploy invokes bonesinfra
bonesinfra runs pyinfra provisioning
bonesremote owns release deployment
```

---

# Current Target

The current target is clarity, not cleverness.

```text
Typer CLI -> app service -> DeployContext -> pyinfra runner -> deploy plan -> grouped operations
```

Keep files small.

Keep boundaries obvious.

Make every module explainable in one sentence.