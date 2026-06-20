Project Path: bonesdeploy

Source Tree:

```txt
bonesdeploy
├── AGENTS.md
├── Cargo.toml
├── LICENSE
├── README.md
├── clippy.toml
├── compile.sh
├── crates
│   ├── bonesdeploy
│   │   ├── Cargo.toml
│   │   ├── kit
│   │   │   ├── bones.toml
│   │   │   ├── deployment
│   │   │   │   ├── 01_install_build_deps.sh
│   │   │   │   └── 02_run_build.sh
│   │   │   ├── hooks
│   │   │   │   ├── hooks.sh
│   │   │   │   ├── post-receive
│   │   │   │   └── pre-push
│   │   │   └── runtime.toml
│   │   ├── runtimes
│   │   │   ├── django
│   │   │   │   ├── deployment
│   │   │   │   │   ├── 01_install_build_deps.sh
│   │   │   │   │   └── 02_run_build.sh
│   │   │   │   └── runtime.toml
│   │   │   ├── laravel
│   │   │   │   ├── deployment
│   │   │   │   │   ├── 01_install_build_deps.sh
│   │   │   │   │   └── 02_run_build.sh
│   │   │   │   └── runtime.toml
│   │   │   ├── next
│   │   │   │   └── runtime.toml
│   │   │   ├── nuxt
│   │   │   │   ├── deployment
│   │   │   │   │   ├── 01_install_build_deps.sh
│   │   │   │   │   └── 02_run_build.sh
│   │   │   │   └── runtime.toml
│   │   │   ├── rails
│   │   │   │   ├── deployment
│   │   │   │   │   ├── 01_install_build_deps.sh
│   │   │   │   │   └── 02_run_build.sh
│   │   │   │   └── runtime.toml
│   │   │   ├── sveltekit
│   │   │   │   ├── deployment
│   │   │   │   │   ├── 01_install_build_deps.sh
│   │   │   │   │   └── 02_run_build.sh
│   │   │   │   └── runtime.toml
│   │   │   └── vue
│   │   │       ├── deployment
│   │   │       │   ├── 01_install_build_deps.sh
│   │   │       │   └── 02_run_build.sh
│   │   │       └── runtime.toml
│   │   └── src
│   │       ├── cli
│   │       │   ├── args.rs
│   │       │   ├── dispatch.rs
│   │       │   └── mod.rs
│   │       ├── commands
│   │       │   ├── config.rs
│   │       │   ├── deploy_project.rs
│   │       │   ├── doctor.rs
│   │       │   ├── init_config.rs
│   │       │   ├── init_project.rs
│   │       │   ├── manage.rs
│   │       │   ├── mod.rs
│   │       │   ├── pull_state.rs
│   │       │   ├── push_state.rs
│   │       │   ├── remote_data.rs
│   │       │   ├── remote_runtime.rs
│   │       │   ├── remote_setup.rs
│   │       │   ├── remote_ssl.rs
│   │       │   ├── rollback.rs
│   │       │   ├── tests
│   │       │   │   └── test_init_project.rs
│   │       │   ├── update.rs
│   │       │   ├── update_release.rs
│   │       │   └── version.rs
│   │       ├── config.rs
│   │       ├── infra
│   │       │   ├── bonesinfra.rs
│   │       │   ├── bonesinfra_cli.rs
│   │       │   ├── bootstrap_ssh.rs
│   │       │   ├── embedded.rs
│   │       │   ├── git.rs
│   │       │   ├── mod.rs
│   │       │   ├── rsync.rs
│   │       │   └── ssh.rs
│   │       ├── main.rs
│   │       └── ui
│   │           ├── mod.rs
│   │           └── prompts.rs
│   ├── bonesremote
│   │   ├── Cargo.toml
│   │   └── src
│   │       ├── cli
│   │       │   ├── args.rs
│   │       │   ├── dispatch.rs
│   │       │   └── mod.rs
│   │       ├── commands
│   │       │   ├── activate_release.rs
│   │       │   ├── config.rs
│   │       │   ├── deploy.rs
│   │       │   ├── doctor.rs
│   │       │   ├── drop_failed_release.rs
│   │       │   ├── init.rs
│   │       │   ├── mod.rs
│   │       │   ├── post_deploy.rs
│   │       │   ├── post_receive.rs
│   │       │   ├── rollback.rs
│   │       │   ├── service.rs
│   │       │   ├── stage_release.rs
│   │       │   ├── tests
│   │       │   │   └── test_doctor.rs
│   │       │   ├── version.rs
│   │       │   └── wire_release.rs
│   │       ├── config.rs
│   │       ├── main.rs
│   │       ├── privileges.rs
│   │       ├── release
│   │       │   └── scripts.rs
│   │       └── release_state.rs
│   └── shared
│       ├── Cargo.toml
│       └── src
│           ├── config.rs
│           ├── lib.rs
│           └── paths.rs
├── docker
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs
│   ├── PROJECT.md
│   ├── bonesinfra-verification.md
│   ├── commands
│   ├── images
│   ├── references
│   │   └── bonesinfra.md
│   ├── security
│   └── slop-refactor.md
├── runtimes
├── rustfmt.toml
└── tests
    ├── ASSERTIONS.md
    └── cleancode
        ├── Cargo.toml
        └── src
            ├── cleancode_file_too_long.rs
            ├── cleancode_no_legacy_terms.rs
            ├── cleancode_no_literal_wrapped_fallback.rs
            ├── cleancode_no_manufactured_success.rs
            └── lib.rs

```

`AGENTS.md`:

```md
You are a lazy senior developer. Lazy means efficient, not careless. The best code is the code never written.

Before writing any code, stop at the first rung that holds:

1. Does this need to be built at all? (YAGNI)
2. Does the standard library already do this? Use it.
3. Does a native platform feature cover it? Use it.
4. Does an already-installed dependency solve it? Use it.
5. Can this be one line? Make it one line.
6. Only then: write the minimum code that works.

Rules:

- No abstractions that weren't explicitly requested.
- No new dependency if it can be avoided.
- No boilerplate nobody asked for.
- Deletion over addition. Boring over clever. Fewest files possible.
- Question complex requests: "Do you actually need X, or does Y cover it?"
- Pick the edge-case-correct option when two stdlib approaches are the same size, lazy means less code, not the flimsier algorithm.
- Mark intentional simplifications with a `ponytail:` comment. If the shortcut has a known ceiling (global lock, O(n²) scan, naive heuristic), the comment names the ceiling and the upgrade path.

Not lazy about: input validation at trust boundaries, error handling that prevents data loss, security, accessibility, the calibration real hardware needs (the platform is never the spec ideal, a clock drifts, a sensor reads off), anything explicitly requested. Lazy code without its check is unfinished: non-trivial logic leaves ONE runnable check behind, the smallest thing that fails if the logic breaks (an assert-based demo/self-check or one small test file; no frameworks, no fixtures). Trivial one-liners need no test.

(Yes, this file also applies to agents working on the ponytail repo itself. Especially to them.)
```

`Cargo.toml`:

```toml
[workspace]
resolver = "3"
members = ["crates/shared", "crates/bonesdeploy", "crates/bonesremote", "tests/cleancode"]

[workspace.lints.clippy]

```

`LICENSE`:

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2026 Alex Younger

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```

`README.md`:

```md
# BonesDeploy

## Remote release deployment tool for simple Linux servers

<div style="margin:0 auto; display: block;"><img width=600 height=600 src="docs/images/bonesdeploy.png" alt="BonesDeploy" /></div>

> WARNING: BonesDeploy is still under active development. There may be some cool bugs!

BonesDeploy deploys project releases to a remote Linux server over SSH. It scaffolds deployment configs and scripts into your repo, syncs them to the remote, and manages permissions through provisioning-time contracts (setgid directories + systemd sandboxing) without forcing containers, a control plane, or a platform layer.

It produces two binaries:
- **`bonesdeploy`** — local CLI for init, config, deployment, and management
- **`bonesremote`** — server-side release lifecycle executor, installed on the deployment host

## Why BonesDeploy

BonesDeploy is built for developers who want direct server deploys without handing deployment over to a PaaS or rebuilding everything around Docker.

- **Drop-in** — add it to an existing repo, scaffold `.bones/`, and deploy over your existing SSH workflow
- **Simple lifecycle** — `bonesdeploy deploy` runs the full deployment pipeline on the remote server; `bonesremote deploy` owns the lifecycle
- **Permission-aware** — BonesDeploy treats deploy-user to service-user handoff as a first-class concern instead of leaving shared groups or ACL sprawl behind
- **Self-hosted and lightweight** — ideal for VPSes, old servers, and Raspberry Pis where simplicity matters more than orchestration
- **Editable by design** — the generated hooks and deployment scripts are yours; BonesDeploy gives you structure, not lock-in
- **Git optional** — git push can trigger deploys through a thin post-receive adapter, but `bonesdeploy deploy` is the primary deployment command

If you want a Heroku-style abstraction layer, use a platform. If you want a disciplined, transparent deployment tool that drops into a normal Linux box, use BonesDeploy.

## How It Works

BonesDeploy uses a two-user permission contract:

1. A **deploy user** (default: `git`) handles SSH access, owns the bare repo, and creates release artifacts. This user has restricted sudo ability (service restart only) but no password login.
2. A **runtime user** (defaults to the project name) owns runtime state — shared files, sockets, and writable directories. This user has no home folder, no login, and no sudo ability — limiting attack scope.

Permissions are a **provisioning-time contract**, not a deployment-time repair:

- The deploy user owns immutable release archives (`releases/`) with setgid so the runtime group can read them.
- The runtime user owns mutable shared state (`shared/`).
- Root creates users, directories, systemd units, and sockets during provisioning.
- No deploy step changes ownership or applies recursive chown.

The sudoers configuration is strictly limited to `bonesremote service restart`, the only command that needs elevated privileges during normal operation.

This gives you a clean privilege boundary:

- the **deploy user** can connect, stage, and activate
- the **runtime user** runs the app
- `root` provisions the machine and restarts services

## Installation

### Local (bonesdeploy)

```sh
cargo install --git https://github.com/AlextheYounga/bonesdeploy.git bonesdeploy
```

### Server (bonesremote)

```sh
sudo cargo install --root /usr/local --git https://github.com/AlextheYounga/bonesdeploy.git bonesremote --force
```

Then run the remote setup:

```sh
sudo bonesremote init
```

This installs a sudoers drop-in at `/etc/sudoers.d/bonesdeploy` so the deploy user can run only the privileged `bonesremote` commands without a password.

## Usage

### Initial Setup

In your project repository:

```sh
bonesdeploy init
```

This will:
1. Create a `.bones/` folder with deployment scripts and hooks
2. Prompt for project name, branch, remote name, host, and port
3. Add `.bones` to `.gitignore`
4. Symlink the `pre-push` hook into `.git/hooks/`
5. Create a local deployment git remote if needed

BonesDeploy assumes opinionated server defaults unless you change them in `.bones/bones.toml`:

- `port = "22"`
- `web_root = "public"`
- `project_root = "/srv/sites/<project_name>"`
- `deploy_user = "git"`
- `runtime_user = "<project_name>"`
- `runtime_group = "<project_name>"`
- `release_group = "<project_name>-release"`

The `init` command creates the local `.bones/` scaffold and records project settings.
If `pyinfra` is missing, BonesDeploy installs it automatically into an isolated managed environment under `XDG_STATE_HOME` (defaults to `~/.local/state/bonesdeploy/pyinfra/.venv`).
Template-based projects then use `bonesdeploy remote runtime` to prompt for a framework and scaffold runtime assets (for example: Laravel installs PHP + PHP-FPM, Django installs Python runtime packages, Node templates install Node.js).
`bonesdeploy remote setup` handles machine bootstrap as root, while `bonesdeploy remote runtime` applies per-site runtime assets such as AppArmor and nginx after a quick confirmation prompt.

To customize nginx behavior, edit the Jinja2 templates in the `src/assets/` directory of the `bonesinfra` repo and re-run `bonesdeploy remote runtime`.

When DNS is ready, enable SSL with certbot (separate from runtime):

```sh
bonesdeploy remote ssl --domain app.example.com --email ops@example.com
```

This runs the dedicated SSL deploy to obtain a Let's Encrypt certificate and configure the runtime nginx router for HTTPS. SSL is fully decoupled from runtime configuration.

### Syncing Configuration

After editing hooks or deployment scripts in `.bones/`:

```sh
bonesdeploy push
```

This rsyncs `.bones/` to the remote bare repo and symlinks the hooks.

### Deploying

Deploy the configured project release:

```sh
bonesdeploy deploy
```

This SSHs into the host and runs `bonesremote deploy --config <remote bones.toml>`, which orchestrates the full server-side pipeline: doctor check → stage release → checkout → wire shared paths → run deployment scripts → activate → restart services → prune old releases.

To roll back to the previous release without rebuilding:

```sh
bonesdeploy rollback
```

### Git-triggered deploy (optional)

If `deploy_on_push = true`:

```sh
git push production master
# post-receive resolves the pushed revision
# post-receive calls bonesremote deploy --config <path> --revision <sha>
```

Git post-receive is a thin adapter — it does not orchestrate the deployment lifecycle. `bonesremote deploy` owns the lifecycle regardless of the trigger.

If `deploy_on_push = false` (the default), pushes only update refs. Run `bonesdeploy deploy` when ready.

### Health Checks

```sh
bonesdeploy doctor          # check local + remote
bonesdeploy doctor --local  # check local only
```

### Updating

Update BonesDeploy binaries to the latest release:

```sh
bonesdeploy update
```

This atomically updates both local (`bonesdeploy`) and remote (`bonesremote`) using symlink flipping for zero-downtime updates with instant rollback capability.

## Configuration

`bonesdeploy init` generates `.bones/bones.toml`:

```toml
remote_name = "production"
project_name = "myproject"
repo_path = "/home/git/myproject.git"
project_root = "/srv/sites/myproject"
port = '22'
branch = 'master'
domain = ''
preview_domain = ""
email = ''
deploy_on_push = false
ssl_enabled = false
releases = 5
```

`host` and `repo_path` are inferred from the deployment remote URL when possible; if parsing fails, init asks only for those missing values.

## Project Structure

```
.bones/
├── bones.toml           # project configuration
├── runtime.toml         # framework runtime configuration
├── hooks.sh             # shared hook functions imported by hook entrypoints
├── deployment/
│   └── 01_*.sh          # deployment scripts (run sequentially)
└── hooks/
    ├── pre-push         # symlinked to .git/hooks/pre-push
    └── post-receive     # thin adapter → calls bonesremote deploy
```

Hooks are written to `.bones/hooks/` once during init and import shared functions from `.bones/hooks.sh`. After that they belong to you — edit freely. Deployment scripts in `.bones/deployment/` must be numbered (e.g. `01_install_deps.sh`, `02_build.sh`) and are always run in order.

Git hooks exist as an optional transport — `bonesdeploy deploy` is the primary deployment command. `post-receive` is a thin adapter that delegates to `bonesremote deploy`.

## Good Fit

BonesDeploy is a strong fit when you want:

- direct Linux deploys over SSH
- simple app hosting on one machine at a time
- explicit provisioning-time permission contracts with setgid group inheritance
- a lightweight alternative to container-first deployment stacks
- something you can run comfortably on low-cost hosts and Raspberry Pis

BonesDeploy can still deploy Docker-based apps if your deployment scripts call `docker compose`, but Docker is optional rather than the foundation.

## License

MIT

## Coverage

Coverage is driven with `cargo-llvm-cov` using cargo aliases in `.cargo/config.toml`.

Install once:

```sh
cargo install cargo-llvm-cov
```

Generate a terminal summary:

```sh
cargo cov
```

Generate lcov output for CI tooling:

```sh
cargo cov-lcov
```

Generate an HTML report:

```sh
cargo cov-html
```

Reports are written under `target/coverage/`.

```

`clippy.toml`:

```toml
too-many-lines-threshold = 60
cognitive-complexity-threshold = 15
too-many-arguments-threshold = 4
```

`compile.sh`:

```sh
cargo build --release
mkdir -p ./bin
cp ./target/release/bonesdeploy ./bin/
cp ./target/release/bonesremote ./bin/

```

`crates/bonesdeploy/Cargo.toml`:

```toml
[package]
name = "bonesdeploy"
version = "0.4.2"
edition = "2024"

[dependencies]
anyhow = "1.0.102"
clap = { version = "4.6.1", features = ["derive"] }
console = "0.15"
inquire = "0.9.4"
openssh = { version = "0.11.6", features = ["native-mux"] }
rust-embed = { version = "8.11.0", features = ["include-exclude"] }
serde = { version = "1.0.228", features = ["derive"] }
serde_json = "1.0"
toml = "0.8"
tempfile = "3.0"
tokio = { version = "1.52.1", features = ["rt", "rt-multi-thread", "macros"] }
shared = { path = "../shared" }

[lints.clippy]
# broad groups (lower priority so individual lint overrides take effect)
correctness = { level = "deny", priority = -1 }
suspicious = { level = "deny", priority = -1 }
complexity = { level = "warn", priority = -1 }
style = { level = "warn", priority = -1 }
perf = { level = "warn", priority = -1 }
pedantic = { level = "warn", priority = -1 }

# readability / naming
similar_names = "warn"
many_single_char_names = "warn"
module_name_repetitions = "warn"
enum_variant_names = "warn"
struct_field_names = "warn"
disallowed_names = "deny"
wildcard_imports = "warn"
module_inception = "warn"

# complexity / API readability
cognitive_complexity = "warn"
too_many_arguments = "deny"
fn_params_excessive_bools = "warn"
large_types_passed_by_value = "warn"
trivially_copy_pass_by_ref = "warn"

# panic / debug leftovers
unwrap_used = "deny"
expect_used = "deny"
panic = "deny"
todo = "deny"
unimplemented = "deny"
dbg_macro = "deny"
# This is a CLI binary: stdout/stderr output is the intended UX.
print_stdout = "allow"
print_stderr = "allow"

# docs / contracts
missing_panics_doc = "deny"
missing_errors_doc = "deny"
missing_safety_doc = "deny"
undocumented_unsafe_blocks = "deny"

# numeric safety
cast_possible_truncation = "warn"
cast_sign_loss = "warn"
cast_possible_wrap = "warn"
checked_conversions = "warn"

# anti-mess / consistency
absolute_paths = "warn"
allow_attributes = "deny"
redundant_clone = "warn"
implicit_clone = "warn"
semicolon_if_nothing_returned = "warn"
match_same_arms = "warn"
needless_pass_by_value = "warn"
cloned_instead_of_copied = "warn"
flat_map_option = "warn"
from_iter_instead_of_collect = "warn"
inefficient_to_string = "warn"
manual_let_else = "warn"
manual_ok_or = "warn"
map_unwrap_or = "warn"
unnecessary_wraps = "warn"

```

`crates/bonesdeploy/kit/bones.toml`:

```toml
# project_name = "mysite"
# remote_name = "production"
# host = ''
ssh_user = "root"
port = '22'
branch = 'master'
domain = ''
preview_domain = ""
email = ''
deploy_on_push = false
ssl_enabled = false
releases = 5

```

`crates/bonesdeploy/kit/deployment/01_install_build_deps.sh`:

```sh
#!/usr/bin/env bash

set -Eeuo pipefail

export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
NVM_INSTALL_URL="https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.5/install.sh"

if [ -s "$NVM_DIR/nvm.sh" ]; then
  exit 0
fi

if command -v curl >/dev/null 2>&1; then
  curl -fsSL "$NVM_INSTALL_URL" | PROFILE=/dev/null NVM_DIR="$NVM_DIR" bash
else
  echo "curl or wget is required to install nvm."
  exit 1
fi
```

`crates/bonesdeploy/kit/deployment/02_run_build.sh`:

```sh
#!/usr/bin/env bash

set -Eeuo pipefail

# Load nvm if .nvmrc is present
if [ -f "./.nvmrc" ]; then
  export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
  if [ -s "$NVM_DIR/nvm.sh" ]; then
    # shellcheck disable=SC1090
    source "$NVM_DIR/nvm.sh"
  elif [ -s "$HOME/.config/nvm/nvm.sh" ]; then
    # shellcheck disable=SC1090
    source "$HOME/.config/nvm/nvm.sh"
  fi
  nvm install
fi

# Clean install and build
rm -rf node_modules

if [ -f "./pnpm-lock.yaml" ]; then
  npm install -g pnpm
  pnpm install --frozen-lockfile
  pnpm build
elif [ -f "./yarn.lock" ]; then
  command -v corepack >/dev/null 2>&1 && corepack enable || true
  yarn install --frozen-lockfile
  yarn build
elif [ -f "./package-lock.json" ]; then
  npm install --include=optional
  npm run build
else
  echo "No lockfile found. Run your package manager locally first."
  exit 1
fi

```

`crates/bonesdeploy/kit/hooks/hooks.sh`:

```sh
bones_init_remote_context() {
	local git_dir_input="${1:-${GIT_DIR:-.}}"
	GIT_DIR=$(cd "$git_dir_input" && pwd)
	BONES_TOML="$GIT_DIR/bones/bones.toml"
}

bones_should_deploy_on_push() {
	if [ "${BONES_FORCE_DEPLOY:-0}" = "1" ]; then
		return 0
	fi

	local deploy_on_push
	deploy_on_push=$(bonesremote config --file "$BONES_TOML" deploy_on_push 2>/dev/null || true)

	if [ -z "$deploy_on_push" ]; then
		return 0
	fi

	if [ "$deploy_on_push" = "false" ]; then
		return 1
	fi

	return 0
}

bones_read_config_branch() {
	bonesremote config --file "$BONES_TOML" branch 2>/dev/null || true
}

bones_is_zero_oid() {
	local oid="$1"
	[[ "$oid" =~ ^0+$ ]]
}

bones_resolve_deploy_push_target() {
	local branch
	branch=$(bones_read_config_branch)
	if [ -z "$branch" ]; then
		echo "[bonesdeploy] Could not read branch from $BONES_TOML"
		return 1
	fi

	local target_ref="refs/heads/$branch"
	local oldrev=""
	local newrev=""
	local refname=""

	if [ "${BONES_FORCE_DEPLOY:-0}" = "1" ]; then
		newrev=$(git --git-dir "$GIT_DIR" rev-parse "$target_ref" 2>/dev/null || true)
		if [ -z "$newrev" ]; then
			echo "[bonesdeploy] Configured deployment ref not found: $target_ref"
			return 1
		fi
	else
		while read -r oldrev newrev refname; do
			if [ "$refname" = "$target_ref" ]; then
				break
			fi
			newrev=""
		done

		if [ -z "$newrev" ]; then
			echo "[bonesdeploy] Push did not update $target_ref; skipping deployment."
			return 1
		fi

		if bones_is_zero_oid "$newrev"; then
			echo "[bonesdeploy] Push deleted $target_ref; skipping deployment."
			return 1
		fi
	fi

	export BONES_DEPLOY_REF="$target_ref"
	export BONES_DEPLOY_NEWREV="$newrev"
	return 0
}

bones_run_remote_deploy() {
	local revision="${1:-}"
	echo "[bonesdeploy] Starting remote deploy..."
	local cmd=(bonesremote deploy --config "$BONES_TOML")
	if [ -n "$revision" ]; then
		cmd+=(--revision "$revision")
	fi

	if ! "${cmd[@]}"; then
		echo "[bonesdeploy] remote deploy failed."
		exit 1
	fi

	echo "[bonesdeploy] Deployment finished."
}

bones_read_local_remote_name() {
	bonesdeploy config --file .bones/bones.toml remote_name 2>/dev/null || true
}

bones_should_run_for_remote() {
	local pushed_remote_name="$1"
	BONES_REMOTE=$(bones_read_local_remote_name)

	if [ -z "$BONES_REMOTE" ]; then
		echo "[bonesdeploy] Warning: Could not read remote_name from .bones/bones.toml"
		return 1
	fi

	if [ "$pushed_remote_name" != "$BONES_REMOTE" ]; then
		return 1
	fi

	return 0
}

bones_run_doctor_local() {
	echo "[bonesdeploy] Pushing to bones remote '$BONES_REMOTE', running doctor..."

	if ! bonesdeploy doctor --local; then
		echo "[bonesdeploy] Doctor reported issues. Push aborted."
		exit 1
	fi

	echo "[bonesdeploy] Doctor passed."
}

```

`crates/bonesdeploy/kit/hooks/post-receive`:

```
#!/usr/bin/env bash
#
# post-receive — Remote hook, runs after refs are updated.
#
# Resolves the pushed deployment ref and delegates the full remote
# deployment lifecycle to bonesremote.

set -euo pipefail

GIT_DIR="${GIT_DIR:-.}"
GIT_DIR=$(cd "$GIT_DIR" && pwd)
HOOKS_LIB="$GIT_DIR/bones/hooks/hooks.sh"

if [ ! -f "$HOOKS_LIB" ]; then
    echo "[bonesdeploy] Missing hook library: $HOOKS_LIB"
    exit 1
fi

# shellcheck source=/dev/null
. "$HOOKS_LIB"
bones_init_remote_context "$GIT_DIR"

main() {
	if ! bones_should_deploy_on_push; then
		echo "[bonesdeploy] deploy_on_push=false, skipping deployment on push."
		exit 0
	fi

	if ! bones_resolve_deploy_push_target; then
		exit 0
	fi

	bones_run_remote_deploy "$BONES_DEPLOY_NEWREV"
}

main

```

`crates/bonesdeploy/kit/hooks/pre-push`:

```
#!/usr/bin/env bash
#
# pre-push — Local hook, symlinked to .git/hooks/pre-push
#
# Checks if we are pushing to the bonesdeploy-managed remote.
# If so, runs `bonesdeploy doctor` and aborts on any failure.
#
# Git passes the remote name and URL as arguments:
#   $1 = remote name
#   $2 = remote URL

set -euo pipefail
REMOTE_NAME="$1"
REPO_ROOT=$(git rev-parse --show-toplevel)
cd "$REPO_ROOT"
HOOKS_LIB="$REPO_ROOT/.bones/hooks/hooks.sh"

if [ ! -f "$HOOKS_LIB" ]; then
    echo "[bonesdeploy] Missing hook library: $HOOKS_LIB"
    exit 1
fi

# shellcheck source=/dev/null
. "$HOOKS_LIB"

main() {
	if bones_should_run_for_remote "$REMOTE_NAME"; then
		bones_run_doctor_local
	fi
}

main

```

`crates/bonesdeploy/kit/runtime.toml`:

```toml
runtime_user = ""
runtime_group = ""
release_group = ""

[permissions]
paths = [
	{ path = "*", type = "dir", mode = "750"},
	{ path = "*", type = "file", mode = "640"},
]

[shared]
paths = [
	{ path = ".env", type = "file" },
	{ path = "storage", type = "dir"},
]


```

`crates/bonesdeploy/runtimes/django/deployment/01_install_build_deps.sh`:

```sh
#!/usr/bin/env bash

set -Eeuo pipefail

export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
NVM_INSTALL_URL="https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.5/install.sh"

if [ -s "$NVM_DIR/nvm.sh" ]; then
  exit 0
fi

if command -v curl >/dev/null 2>&1; then
  curl -fsSL "$NVM_INSTALL_URL" | PROFILE=/dev/null NVM_DIR="$NVM_DIR" bash
else
  echo "curl or wget is required to install nvm."
  exit 1
fi
```

`crates/bonesdeploy/runtimes/django/deployment/02_run_build.sh`:

```sh
#!/usr/bin/env bash

set -Eeuo pipefail

command -v python3 >/dev/null 2>&1 || { echo "python3 not found"; exit 1; }

# Activate virtualenv
VENV_DIR="${VENV_DIR:-venv}"
if [ -d "./$VENV_DIR" ]; then
  # shellcheck disable=SC1090
  source "./$VENV_DIR/bin/activate"
else
  echo "Virtual environment not found at ./$VENV_DIR"
  echo "Create one on the server: python3 -m venv $VENV_DIR"
  exit 1
fi

# Install dependencies
if [ -f "./requirements.txt" ]; then
  pip install -r requirements.txt --quiet
elif [ -f "./pyproject.toml" ]; then
  pip install . --quiet
fi

# Run migrations
python3 manage.py migrate --noinput

# Collect static files
python3 manage.py collectstatic --noinput

# Restart gunicorn via systemd
SERVICE_NAME="$PROJECT_NAME"
if ! command -v systemctl >/dev/null 2>&1; then
  echo "systemctl not found. Restart your app server manually."
elif systemctl is-active --quiet "$SERVICE_NAME" 2>/dev/null; then
  systemctl restart "$SERVICE_NAME"
elif systemctl list-unit-files | grep -q "$SERVICE_NAME"; then
  systemctl start "$SERVICE_NAME"
else
  echo "No systemd service found for $SERVICE_NAME. Restart your app server manually."
fi

```

`crates/bonesdeploy/runtimes/django/runtime.toml`:

```toml
template = "django"
web_root = "public"

[permissions]
paths = [
    { path = "*", type = "dir", mode = "750" },
    { path = "*", type = "file", mode = "640" },
    { path = "static", type = "dir", mode = "750", recursive = true },
    { path = "media", type = "dir", mode = "770", recursive = true },
]

[shared]
paths = [
    { path = ".env", type = "file" },
    { path = "storage", type = "dir" },
]

```

`crates/bonesdeploy/runtimes/laravel/deployment/01_install_build_deps.sh`:

```sh
#!/usr/bin/env bash

set -Eeuo pipefail

trap 'status=$?; echo "[bonesdeploy] Failed at line $LINENO: $BASH_COMMAND (status $status)" >&2; exit "$status"' ERR

[ -f artisan ] || { echo "[bonesdeploy] artisan not found; skipping Laravel build dependency install."; exit 0; }
[ -f package.json ] || { echo "[bonesdeploy] package.json not found; skipping Node install."; exit 0; }

: "${PROJECT_ROOT:?PROJECT_ROOT must be set by bonesremote}"

NODE_DIR="$PROJECT_ROOT/build/node"
NODE_BIN="$NODE_DIR/bin/node"

command -v curl >/dev/null 2>&1 || { echo "[bonesdeploy] curl not found" >&2; exit 1; }
command -v tar >/dev/null 2>&1 || { echo "[bonesdeploy] tar not found" >&2; exit 1; }

read_node_version() {
  if [ -n "${BONES_NODE_VERSION:-}" ]; then
    printf '%s\n' "$BONES_NODE_VERSION"
    return
  fi

  if [ -f .node-version ]; then
    head -n 1 .node-version
    return
  fi

  if [ -f .nvmrc ]; then
    head -n 1 .nvmrc
    return
  fi

  if [ -f .tool-versions ]; then
    awk '$1 == "nodejs" || $1 == "node" { print $2; exit }' .tool-versions
    return
  fi

  if command -v php >/dev/null 2>&1; then
    php -r '
      $p = json_decode(file_get_contents("package.json"), true) ?: [];

      if (isset($p["volta"]["node"])) {
          echo $p["volta"]["node"];
          exit;
      }

      if (isset($p["engines"]["node"])) {
          echo $p["engines"]["node"];
          exit;
      }
    '
  fi
}

raw_version="$(read_node_version | head -n 1 | sed 's/#.*$//' | tr -d '\r' | xargs || true)"
version="${raw_version#v}"

if ! [[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  cat >&2 <<'EOF'
[bonesdeploy] Laravel frontend build requires an exact pinned Node version.

Add one of these to the project:
  .node-version        example: 24.17.0
  .nvmrc              example: 24.17.0
  .tool-versions      example: nodejs 24.17.0
  package.json volta  example: "volta": { "node": "24.17.0" }

Or set:
  BONES_NODE_VERSION=24.17.0

Aliases and ranges are intentionally rejected:
  node
  latest
  lts/*
  24
  >=20
EOF
  exit 1
fi

ensure_corepack() {
  export PATH="$NODE_DIR/bin:$PATH"

  if ! command -v corepack >/dev/null 2>&1; then
    echo "[bonesdeploy] corepack not found in Node install; installing corepack..."
    npm install -g corepack@latest
  fi

  corepack enable --install-directory "$NODE_DIR/bin" 2>/dev/null || true
}

if [ -x "$NODE_BIN" ] && "$NODE_BIN" --version | grep -qx "v$version"; then
  echo "[bonesdeploy] Node v${version} already installed."
  ensure_corepack
  exit 0
fi

arch="$(uname -m)"
case "$arch" in
  x86_64)  node_arch="x64" ;;
  aarch64) node_arch="arm64" ;;
  *) echo "[bonesdeploy] Unsupported architecture for Node binary install: $arch" >&2; exit 1 ;;
esac

url="https://nodejs.org/dist/v${version}/node-v${version}-linux-${node_arch}.tar.xz"
tmp="$(mktemp -d)"

cleanup() {
  rm -rf "$tmp"
}
trap cleanup EXIT

echo "[bonesdeploy] Installing Node v${version}..."
echo "[bonesdeploy] Downloading $url"

mkdir -p "$(dirname "$NODE_DIR")"

curl -fsSL --retry 3 --retry-delay 2 "$url" | tar -xJ -C "$tmp"

rm -rf "$NODE_DIR"
mv "$tmp/node-v${version}-linux-${node_arch}" "$NODE_DIR"

ensure_corepack

echo "[bonesdeploy] Node installed: $(node --version)"
echo "[bonesdeploy] npm installed:  $(npm --version)"
```

`crates/bonesdeploy/runtimes/laravel/deployment/02_run_build.sh`:

```sh
#!/usr/bin/env bash

set -Eeuo pipefail

trap 'status=$?; echo "[bonesdeploy] Failed at line $LINENO: $BASH_COMMAND (status $status)" >&2; exit "$status"' ERR

[ -f artisan ] || { echo "[bonesdeploy] artisan not found" >&2; exit 1; }

command -v php >/dev/null 2>&1 || { echo "[bonesdeploy] php not found" >&2; exit 1; }
command -v composer >/dev/null 2>&1 || { echo "[bonesdeploy] composer not found" >&2; exit 1; }

: "${PROJECT_ROOT:?PROJECT_ROOT must be set by bonesremote}"

export COMPOSER_ALLOW_SUPERUSER="${COMPOSER_ALLOW_SUPERUSER:-1}"
export CI=1
export COREPACK_ENABLE_DOWNLOAD_PROMPT=0

artisan_command_exists() {
  local command_name="$1"
  php artisan list --raw 2>/dev/null | awk '{ print $1 }' | grep -qx "$command_name"
}

package_json_value() {
  local php_expr="$1"

  php -r '
    $p = json_decode(file_get_contents("package.json"), true) ?: [];
    '"$php_expr"'
  ' 2>/dev/null || true
}

detect_package_manager() {
  local package_manager

  package_manager="$(package_json_value '
    $pm = $p["packageManager"] ?? "";
    if ($pm) {
        echo explode("@", $pm)[0];
    }
  ')"

  if [ -n "$package_manager" ]; then
    printf '%s\n' "$package_manager"
    return
  fi

  if [ -f pnpm-lock.yaml ]; then
    echo "pnpm"
  elif [ -f yarn.lock ]; then
    echo "yarn"
  elif [ -f package-lock.json ] || [ -f npm-shrinkwrap.json ]; then
    echo "npm"
  else
    echo "npm"
  fi
}

has_build_script() {
  [ -f package.json ] || return 1

  [ "$(package_json_value '
    echo isset($p["scripts"]["build"]) ? "1" : "0";
  ')" = "1" ]
}

run_frontend_build() {
  [ -f package.json ] || {
    echo "[bonesdeploy] package.json not found; skipping frontend build."
    return
  }

  has_build_script || {
    echo "[bonesdeploy] package.json has no build script; skipping frontend build."
    return
  }

  export PATH="$PROJECT_ROOT/build/node/bin:$PATH"

  command -v node >/dev/null 2>&1 || {
    echo "[bonesdeploy] node not found. Did 01_install_build_deps.sh run?" >&2
    exit 1
  }

  if ! command -v corepack >/dev/null 2>&1; then
    echo "[bonesdeploy] corepack not found; installing corepack..."
    npm install -g corepack@latest
  fi

  corepack enable --install-directory "$(dirname "$(command -v node)")" 2>/dev/null || true

  local package_manager
  package_manager="$(detect_package_manager)"

  echo "[bonesdeploy] Node: $(node --version)"
  echo "[bonesdeploy] npm:  $(npm --version)"
  echo "[bonesdeploy] Frontend package manager: $package_manager"

  case "$package_manager" in
    npm)
      if [ -f package-lock.json ] || [ -f npm-shrinkwrap.json ]; then
        echo "[bonesdeploy] Installing frontend dependencies with npm ci..."
        npm ci --include=dev
      else
        echo "[bonesdeploy] package-lock.json not found; falling back to npm install..."
        npm install
      fi

      echo "[bonesdeploy] Building frontend assets with npm..."
      npm run build
      ;;

    pnpm)
      if [ -f pnpm-lock.yaml ]; then
        echo "[bonesdeploy] Installing frontend dependencies with pnpm frozen lockfile..."
        corepack pnpm install --frozen-lockfile --prod=false
      else
        echo "[bonesdeploy] pnpm-lock.yaml not found; falling back to non-frozen pnpm install..."
        corepack pnpm install --prod=false
      fi

      echo "[bonesdeploy] Building frontend assets with pnpm..."
      corepack pnpm run build
      ;;

    yarn)
      local yarn_version
      yarn_version="$(corepack yarn --version 2>/dev/null || true)"

      if [[ "$yarn_version" == 1.* ]]; then
        echo "[bonesdeploy] Installing frontend dependencies with Yarn classic..."
        corepack yarn install --frozen-lockfile
      else
        echo "[bonesdeploy] Installing frontend dependencies with Yarn modern..."
        corepack yarn install --immutable
      fi

      echo "[bonesdeploy] Building frontend assets with yarn..."
      corepack yarn run build
      ;;

    *)
      echo "[bonesdeploy] Unsupported package manager: $package_manager" >&2
      exit 1
      ;;
  esac
}

enter_maintenance_mode() {
  if [ "${BONES_LARAVEL_MAINTENANCE:-1}" = "0" ]; then
    echo "[bonesdeploy] Maintenance mode disabled by BONES_LARAVEL_MAINTENANCE=0."
    return
  fi

  echo "[bonesdeploy] Entering Laravel maintenance mode..."

  if php artisan down --render="errors::503"; then
    return
  fi

  php artisan down
}

exit_maintenance_mode() {
  php artisan up || true
}

echo "[bonesdeploy] Installing Composer dependencies..."
composer install --no-dev --prefer-dist --no-interaction --optimize-autoloader

# Generate frontend route/action files before Vite compiles the JS/TS bundle.
if artisan_command_exists "wayfinder:generate"; then
  echo "[bonesdeploy] Generating Wayfinder files..."
  php artisan wayfinder:generate
fi

run_frontend_build

enter_maintenance_mode
trap exit_maintenance_mode EXIT

if [ ! -f .env ] || ! grep -Eq '^APP_KEY=base64:' .env; then
  echo "[bonesdeploy] Generating Laravel APP_KEY..."
  php artisan key:generate --force
fi

echo "[bonesdeploy] Ensuring Laravel storage link exists..."
php artisan storage:link --force || true

if [ "${BONES_LARAVEL_SKIP_MIGRATIONS:-0}" = "1" ]; then
  echo "[bonesdeploy] Skipping migrations because BONES_LARAVEL_SKIP_MIGRATIONS=1."
else
  echo "[bonesdeploy] Running migrations..."
  php artisan migrate --force
fi

echo "[bonesdeploy] Rebuilding Laravel caches..."
php artisan optimize:clear
php artisan config:cache
php artisan route:cache
php artisan view:cache

if artisan_command_exists "event:cache"; then
  php artisan event:cache || true
fi

if artisan_command_exists "queue:restart"; then
  php artisan queue:restart || true
fi

php artisan up
trap - EXIT

echo "[bonesdeploy] Laravel build complete."
```

`crates/bonesdeploy/runtimes/laravel/runtime.toml`:

```toml
template = "laravel"
web_root = "public"
php_version = "8.5"

[permissions]
paths = [
    { path = "*", type = "dir", mode = "750" },
    { path = "*", type = "file", mode = "640" },
    { path = "storage", type = "dir", mode = "770", recursive = true },
    { path = "bootstrap/cache", type = "dir", mode = "770", recursive = true },
    { path = "database", type = "dir", mode = "770", recursive = false },
    { path = "database/database.sqlite", type = "file", mode = "660", recursive = false },
]

[shared]
paths = [
    { path = "storage", type = "dir" },
    { path = ".env", type = "file" },
]

```

`crates/bonesdeploy/runtimes/next/runtime.toml`:

```toml
template = "next"
web_root = "public"

[permissions]
paths = [
    { path = "*", type = "dir", mode = "750" },
    { path = "*", type = "file", mode = "640" },
    { path = ".next", type = "dir", mode = "770", recursive = true },
]

[shared]
paths = [
    { path = ".env", type = "file" },
    { path = "storage", type = "dir" },
]

```

`crates/bonesdeploy/runtimes/nuxt/deployment/01_install_build_deps.sh`:

```sh
#!/usr/bin/env bash

set -Eeuo pipefail

export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
NVM_INSTALL_URL="https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.5/install.sh"

if [ -s "$NVM_DIR/nvm.sh" ]; then
  exit 0
fi

if command -v curl >/dev/null 2>&1; then
  curl -fsSL "$NVM_INSTALL_URL" | PROFILE=/dev/null NVM_DIR="$NVM_DIR" bash
else
  echo "curl or wget is required to install nvm."
  exit 1
fi
```

`crates/bonesdeploy/runtimes/nuxt/deployment/02_run_build.sh`:

```sh
  #!/usr/bin/env bash
  set -Eeuo pipefail

  if [ -f "./.nvmrc" ]; then
    export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
    if [ -s "$NVM_DIR/nvm.sh" ]; then
      # shellcheck disable=SC1090
      source "$NVM_DIR/nvm.sh"
    elif [ -s "$HOME/.config/nvm/nvm.sh" ]; then
      # shellcheck disable=SC1090
      source "$HOME/.config/nvm/nvm.sh"
    fi
    nvm install
  fi

  if [ -f "./pnpm-lock.yaml" ]; then
    npm install -g pnpm
    pnpm install --frozen-lockfile
    pnpm generate
  elif [ -f "./yarn.lock" ]; then
    command -v corepack >/dev/null 2>&1 && corepack enable || true
    yarn install --frozen-lockfile
    yarn generate
  elif [ -f "./package-lock.json" ]; then
    npm ci --include=optional
    npm run generate
  else
    echo "No lockfile found. Run your package manager locally first."
    exit 1
  fi

```

`crates/bonesdeploy/runtimes/nuxt/runtime.toml`:

```toml
template = "nuxt"
web_root = ".output/public"

[permissions]
paths = [
    { path = "*", type = "dir", mode = "750" },
    { path = "*", type = "file", mode = "640" },
    { path = ".output", type = "dir", mode = "770", recursive = true },
    { path = ".nuxt", type = "dir", mode = "770", recursive = true },
]

[shared]
paths = [
    { path = ".env", type = "file" },
    { path = "storage", type = "dir" },
]

```

`crates/bonesdeploy/runtimes/rails/deployment/01_install_build_deps.sh`:

```sh
#!/usr/bin/env bash

set -Eeuo pipefail

export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
NVM_INSTALL_URL="https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.5/install.sh"

if [ -s "$NVM_DIR/nvm.sh" ]; then
  exit 0
fi

if command -v curl >/dev/null 2>&1; then
  curl -fsSL "$NVM_INSTALL_URL" | PROFILE=/dev/null NVM_DIR="$NVM_DIR" bash
else
  echo "curl or wget is required to install nvm."
  exit 1
fi
```

`crates/bonesdeploy/runtimes/rails/deployment/02_run_build.sh`:

```sh
#!/usr/bin/env bash

set -Eeuo pipefail

command -v ruby >/dev/null 2>&1 || { echo "ruby not found"; exit 1; }
command -v bundle >/dev/null 2>&1 || { echo "bundler not found"; exit 1; }

# Load rbenv if available
if [ -d "$HOME/.rbenv" ]; then
  export PATH="$HOME/.rbenv/bin:$PATH"
  eval "$(rbenv init -)"
fi

# Install Ruby version from .ruby-version if rbenv is available
if [ -f "./.ruby-version" ] && command -v rbenv >/dev/null 2>&1; then
  rbenv install --skip-existing
fi

# Install dependencies
bundle install --deployment --without development test

# Precompile assets
if bundle exec rails assets:precompile 2>/dev/null; then
  echo "Assets precompiled."
fi

# Run database migrations
RAILS_ENV=production bundle exec rails db:migrate

# Restart puma via systemd
SERVICE_NAME="$PROJECT_NAME"
if ! command -v systemctl >/dev/null 2>&1; then
  echo "systemctl not found. Restart your app server manually."
elif systemctl is-active --quiet "$SERVICE_NAME" 2>/dev/null; then
  systemctl restart "$SERVICE_NAME"
elif systemctl list-unit-files | grep -q "$SERVICE_NAME"; then
  systemctl start "$SERVICE_NAME"
else
  echo "No systemd service found for $SERVICE_NAME. Restart your app server manually."
fi

```

`crates/bonesdeploy/runtimes/rails/runtime.toml`:

```toml
template = "rails"
web_root = "public"

[permissions]
paths = [
    { path = "*", type = "dir", mode = "750" },
    { path = "*", type = "file", mode = "640" },
    { path = "tmp", type = "dir", mode = "770", recursive = true },
    { path = "log", type = "dir", mode = "770", recursive = true },
    { path = "storage", type = "dir", mode = "770", recursive = true },
    { path = "public/assets", type = "dir", mode = "750", recursive = true },
]

[shared]
paths = [
    { path = ".env", type = "file" },
    { path = "storage", type = "dir" },
]

```

`crates/bonesdeploy/runtimes/sveltekit/deployment/01_install_build_deps.sh`:

```sh
#!/usr/bin/env bash

set -Eeuo pipefail

export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
NVM_INSTALL_URL="https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.5/install.sh"

if [ -s "$NVM_DIR/nvm.sh" ]; then
  exit 0
fi

if command -v curl >/dev/null 2>&1; then
  curl -fsSL "$NVM_INSTALL_URL" | PROFILE=/dev/null NVM_DIR="$NVM_DIR" bash
else
  echo "curl or wget is required to install nvm."
  exit 1
fi
```

`crates/bonesdeploy/runtimes/sveltekit/deployment/02_run_build.sh`:

```sh
#!/usr/bin/env bash

set -Eeuo pipefail

# Load nvm if .nvmrc is present
if [ -f "./.nvmrc" ]; then
  export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
  if [ -s "$NVM_DIR/nvm.sh" ]; then
    # shellcheck disable=SC1090
    source "$NVM_DIR/nvm.sh"
  elif [ -s "$HOME/.config/nvm/nvm.sh" ]; then
    # shellcheck disable=SC1090
    source "$HOME/.config/nvm/nvm.sh"
  fi
  nvm install
fi

# Clean install and build
rm -rf node_modules

if [ -f "./pnpm-lock.yaml" ]; then
  npm install -g pnpm
  pnpm install --frozen-lockfile
  pnpm build
elif [ -f "./yarn.lock" ]; then
  command -v corepack >/dev/null 2>&1 && corepack enable || true
  yarn install --frozen-lockfile
  yarn build
elif [ -f "./package-lock.json" ]; then
  npm install --include=optional
  npm run build
else
  echo "No lockfile found. Run your package manager locally first."
  exit 1
fi

```

`crates/bonesdeploy/runtimes/sveltekit/runtime.toml`:

```toml
template = "sveltekit"
web_root = "build"

[permissions]
paths = [
    { path = "*", type = "dir", mode = "750" },
    { path = "*", type = "file", mode = "640" },
    { path = "build", type = "dir", mode = "770", recursive = true },
]

[shared]
paths = [
    { path = ".env", type = "file" },
    { path = "storage", type = "dir" },
]

```

`crates/bonesdeploy/runtimes/vue/deployment/01_install_build_deps.sh`:

```sh
#!/usr/bin/env bash

set -Eeuo pipefail

export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
NVM_INSTALL_URL="https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.5/install.sh"

if [ -s "$NVM_DIR/nvm.sh" ]; then
  exit 0
fi

if command -v curl >/dev/null 2>&1; then
  curl -fsSL "$NVM_INSTALL_URL" | PROFILE=/dev/null NVM_DIR="$NVM_DIR" bash
else
  echo "curl or wget is required to install nvm."
  exit 1
fi
```

`crates/bonesdeploy/runtimes/vue/deployment/02_run_build.sh`:

```sh
#!/usr/bin/env bash

set -Eeuo pipefail

# Load nvm if .nvmrc is present
if [ -f "./.nvmrc" ]; then
  export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
  if [ -s "$NVM_DIR/nvm.sh" ]; then
    # shellcheck disable=SC1090
    source "$NVM_DIR/nvm.sh"
  elif [ -s "$HOME/.config/nvm/nvm.sh" ]; then
    # shellcheck disable=SC1090
    source "$HOME/.config/nvm/nvm.sh"
  fi
  nvm install
fi

# Clean install and build
rm -rf node_modules

if [ -f "./pnpm-lock.yaml" ]; then
  npm install -g pnpm
  pnpm install --frozen-lockfile
  pnpm build
elif [ -f "./yarn.lock" ]; then
  command -v corepack >/dev/null 2>&1 && corepack enable || true
  yarn install --frozen-lockfile
  yarn build
elif [ -f "./package-lock.json" ]; then
  npm install --include=optional
  npm run build
else
  echo "No lockfile found. Run your package manager locally first."
  exit 1
fi

```

`crates/bonesdeploy/runtimes/vue/runtime.toml`:

```toml
template = "vue"
web_root = "dist/public"

[permissions]
paths = [
    { path = "*", type = "dir", mode = "750" },
    { path = "*", type = "file", mode = "640" },
    { path = "dist", type = "dir", mode = "755", recursive = true },
]

[shared]
paths = [
    { path = ".env", type = "file" },
    { path = "storage", type = "dir" },
]

```

`crates/bonesdeploy/src/cli/args.rs`:

```rs
use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(name = "bonesdeploy", about = "Remote release deployment tool")]
pub struct Cli {
    #[command(subcommand)]
    pub command: Command,
}

#[derive(Subcommand)]
pub enum Command {
    /// Set up bonesdeploy in the current repository. Run this once per project.
    Init {
        /// Skip all interactive prompts; required fields must be provided via flags
        #[arg(long)]
        non_interactive: bool,
        /// Run remote setup after init (instead of prompting)
        #[arg(long)]
        setup_remote: bool,
        /// Project name (default: current directory name)
        #[arg(long)]
        project_name: Option<String>,
        /// Git branch to deploy
        #[arg(long)]
        branch: Option<String>,
        /// Deployment remote name (default: production)
        #[arg(short = 'r', long)]
        remote: Option<String>,
        /// Server hostname or IP
        #[arg(short = 'H', long)]
        host: Option<String>,
        /// SSH port (default: 22)
        #[arg(long)]
        port: Option<String>,
    },
    /// Check local and remote environment health
    Doctor {
        /// Skip remote checks
        #[arg(long)]
        local: bool,
    },
    /// Sync .bones/ folder to the remote bare repo
    Push,
    /// Sync .bones/ folder back from the remote bare repo
    Pull,
    /// Deploy the configured project release to the remote server
    Deploy,
    /// Update bonesdeploy and bonesremote to the latest version
    Update {
        /// Skip local update
        #[arg(long)]
        skip_local: bool,
        /// Skip remote update
        #[arg(long)]
        skip_remote: bool,
    },
    /// Remote operations
    Remote {
        #[command(subcommand)]
        command: RemoteCommand,
    },
    /// Open remote server management TUI
    Manage,
    /// Roll back current release to the previous one
    Rollback,
    /// Get a config value from a TOML file
    Config {
        /// Path to TOML config file
        #[arg(long)]
        file: String,
        /// Key to read
        key: String,
    },
    /// Print the version
    Version,
}

#[derive(Subcommand)]
pub enum RemoteCommand {
    /// Run remote setup against configured host
    Setup,
    /// Apply the configured runtime against configured host
    Runtime,
    /// Obtain and configure SSL certificates with certbot
    Ssl {
        /// Domain name for the certificate (e.g. app.example.com)
        #[arg(long)]
        domain: Option<String>,
        /// Email used for Let's Encrypt registration and notices
        #[arg(long)]
        email: Option<String>,
    },
}

```

`crates/bonesdeploy/src/cli/dispatch.rs`:

```rs
use anyhow::Result;

use crate::cli::args::{Cli, Command, RemoteCommand};
use crate::commands::{
    config, deploy_project, doctor, init_config, init_project, manage, pull_state, push_state, remote_runtime,
    remote_setup, remote_ssl, rollback, update, version,
};

pub async fn run(cli: &Cli) -> Result<()> {
    match &cli.command {
        Command::Init { non_interactive, setup_remote, project_name, branch, remote, host, port } => {
            let remote_setup_ran = init_project::run(&init_config::InitArgs {
                non_interactive: *non_interactive,
                setup_remote: *setup_remote,
                project_name: project_name.clone(),
                branch: branch.clone(),
                remote: remote.clone(),
                host: host.clone(),
                port: port.clone(),
            })?;
            if remote_setup_ran {
                push_state::run().await?;
            }
            Ok(())
        }
        Command::Doctor { local } => doctor::run(*local).await,
        Command::Push => push_state::run().await,
        Command::Pull => pull_state::run(),
        Command::Deploy => deploy_project::run().await,
        Command::Update { skip_local, skip_remote } => {
            update::run(update::Options { skip_local: *skip_local, skip_remote: *skip_remote }).await
        }
        Command::Manage => manage::run(),
        Command::Remote { command } => match command {
            RemoteCommand::Setup => remote_setup::run(),
            RemoteCommand::Runtime => remote_runtime::run(),
            RemoteCommand::Ssl { domain, email } => remote_ssl::run(domain.clone(), email.clone()),
        },
        Command::Rollback => rollback::run().await,
        Command::Config { file, key } => config::run(file, key),
        Command::Version => {
            version::run();
            Ok(())
        }
    }
}

```

`crates/bonesdeploy/src/cli/mod.rs`:

```rs
pub mod args;
pub mod dispatch;

```

`crates/bonesdeploy/src/commands/config.rs`:

```rs
use std::fs;

use anyhow::{Context, Result, bail};

pub fn run(file: &str, key: &str) -> Result<()> {
    let content = fs::read_to_string(file).with_context(|| format!("Failed to read config file: {file}"))?;
    let value: toml::Value = toml::from_str(&content).with_context(|| format!("Failed to parse TOML: {file}"))?;

    let result = value.get(key);
    let Some(toml_value) = result else {
        bail!("Key '{key}' not found in {file}");
    };

    match toml_value {
        toml::Value::String(s) => print!("{s}"),
        toml::Value::Boolean(b) => print!("{b}"),
        toml::Value::Integer(i) => print!("{i}"),
        toml::Value::Float(f) => print!("{f}"),
        _ => bail!("Unsupported value type for key '{key}'"),
    }

    Ok(())
}

```

`crates/bonesdeploy/src/commands/deploy_project.rs`:

```rs
use anyhow::Result;
use console::style;
use shared::paths;
use std::path::Path;

use crate::config;
use crate::infra::ssh;

pub async fn run() -> Result<()> {
    let bones_toml = Path::new(paths::LOCAL_BONES_TOML);
    let cfg = config::load(bones_toml)?;

    let remote_bones_toml = cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).repo_bones_toml;

    println!("Deploying {} on {}...", style(&cfg.project_name).cyan().bold(), style(&cfg.host).cyan());

    let session = ssh::connect(&cfg).await?;

    println!("Running remote deploy...");
    ssh::stream_cmd(&session, &format!("bonesremote deploy --config '{remote_bones_toml}'")).await?;

    session.close().await?;

    println!("\n{} Deployment complete.", style("Done!").green().bold());

    Ok(())
}

```

`crates/bonesdeploy/src/commands/doctor.rs`:

```rs
use std::fs;
use std::path::Path;

use anyhow::Result;
use console::style;

use crate::config;
use crate::infra::rsync;
use crate::infra::ssh;
use shared::config::default_deploy_user;
use shared::paths;

pub async fn run(local_only: bool) -> Result<()> {
    println!("{}", style("bonesdeploy doctor").bold());

    let mut issues: Vec<String> = Vec::new();

    let cfg = config::load(Path::new(paths::LOCAL_BONES_TOML)).ok();
    let deploy_on_push = cfg.as_ref().is_some_and(|c| c.deploy_on_push);

    check_bones_structure(&mut issues);
    check_deployment_naming(&mut issues);

    if deploy_on_push {
        check_pre_push_symlink(&mut issues);
    }

    if !local_only {
        match &cfg {
            Some(cfg) => check_remote(cfg, deploy_on_push, &mut issues).await,
            None => issues.push("Cannot load .bones/bones.toml; skipping remote checks".into()),
        }
    }

    if issues.is_empty() {
        println!("\n{} All checks passed.", style("OK").green().bold());
        Ok(())
    } else {
        println!();
        for issue in &issues {
            println!("  {} {issue}", style("!").red().bold());
        }
        anyhow::bail!("Doctor found {} issue{}", issues.len(), if issues.len() == 1 { "" } else { "s" });
    }
}

fn check_bones_structure(issues: &mut Vec<String>) {
    let bones_dir = Path::new(paths::LOCAL_BONES_DIR);

    if !bones_dir.exists() {
        issues.push(format!("{}/ does not exist", paths::LOCAL_BONES_DIR));
        return;
    }

    if !bones_dir.is_symlink() {
        issues.push(format!(
            "{}/ is not a symlink — expected a symlink to ~/.config/bonesdeploy/<project>.bones/",
            paths::LOCAL_BONES_DIR
        ));
        return;
    }

    let expected = [
        paths::LOCAL_BONES_TOML,
        paths::LOCAL_BONES_HOOKS_SCRIPT,
        paths::LOCAL_BONES_HOOKS_DIR,
        paths::LOCAL_BONES_DEPLOYMENT_DIR,
    ];

    for path in &expected {
        if !Path::new(path).exists() {
            issues.push(format!("{path} is missing"));
        }
    }
}

fn check_deployment_naming(issues: &mut Vec<String>) {
    let deployment_dir = Path::new(paths::LOCAL_BONES_DEPLOYMENT_DIR);
    if !deployment_dir.exists() {
        return;
    }

    let Ok(entries) = fs::read_dir(deployment_dir) else {
        return;
    };

    for entry in entries {
        let Ok(entry) = entry else { continue };
        let name = entry.file_name();
        let name = name.to_string_lossy();

        // Scripts must start with a numeric prefix like "01_"
        let has_numeric_prefix = name.chars().take_while(char::is_ascii_digit).count() > 0;

        if !has_numeric_prefix {
            issues.push(format!("Deployment script '{name}' does not start with a numeric prefix (e.g. 01_)"));
        }
    }
}

fn check_pre_push_symlink(issues: &mut Vec<String>) {
    let link = Path::new(paths::GIT_PRE_PUSH_HOOK);

    if !link.symlink_metadata().is_ok_and(|m| m.is_symlink()) {
        issues.push(format!("{} is not symlinked", paths::GIT_PRE_PUSH_HOOK));
        return;
    }

    let Ok(target) = fs::read_link(link) else {
        issues.push(format!("{}: cannot read symlink target", paths::GIT_PRE_PUSH_HOOK));
        return;
    };

    let expected = Path::new(paths::PRE_PUSH_HOOK_TARGET);
    if target != expected {
        issues.push(format!(
            "{} points to '{}', expected '{}'",
            paths::GIT_PRE_PUSH_HOOK,
            target.display(),
            expected.display()
        ));
    }
}

async fn check_remote(cfg: &config::Bones, deploy_on_push: bool, issues: &mut Vec<String>) {
    let session = match ssh::connect(cfg).await {
        Ok(s) => s,
        Err(e) => {
            issues.push(format!("Cannot connect to remote: {e}"));
            return;
        }
    };

    let repo_path = &cfg.repo_path;

    if ssh::run_cmd(&session, "command -v bonesremote").await.is_err() {
        issues.push("bonesremote is not available on the remote".into());
    }

    let check_bones = format!("test -d {repo_path}/{}", paths::BONES_DIR);
    if ssh::run_cmd(&session, &check_bones).await.is_err() {
        issues.push(format!("{repo_path}/{}/ does not exist on remote (run 'bonesdeploy push')", paths::BONES_DIR));
    }

    check_rsync_sync(cfg, issues);

    // Check hooks are symlinked properly (only when git-triggered deploy is enabled)
    if deploy_on_push {
        let check_hooks = format!(
            "for hook in {repo_path}/{}/{}/{}; do \
            name=$(basename \"$hook\"); \
            link=\"{repo_path}/{}/$name\"; \
            if [ ! -L \"$link\" ] || [ \"$(readlink \"$link\")\" != \"$hook\" ]; then \
                echo \"$name\"; \
            fi; \
         done",
            paths::BONES_DIR,
            paths::HOOKS_DIR,
            "*",
            paths::HOOKS_DIR
        );
        match ssh::run_cmd(&session, &check_hooks).await {
            Ok(output) => {
                for hook in output.lines() {
                    let hook = hook.trim();
                    if !hook.is_empty() {
                        issues.push(format!(
                            "{repo_path}/{}/{hook} is not properly symlinked to {}/{}/{hook}",
                            paths::HOOKS_DIR,
                            paths::BONES_DIR,
                            paths::HOOKS_DIR
                        ));
                    }
                }
            }
            Err(e) => issues.push(format!("Failed to check remote hook symlinks: {e}")),
        }
    }

    let _ = session.close().await;
}

fn check_rsync_sync(cfg: &config::Bones, issues: &mut Vec<String>) {
    let user = default_deploy_user();
    let host = &cfg.host;
    let port = &cfg.port;
    let repo_path = &cfg.repo_path;
    let dest = format!("{user}@{host}:{repo_path}/{}/", paths::BONES_DIR);

    let ssh_arg = format!("ssh -p {port}");
    let source = format!("{}/", paths::LOCAL_BONES_DIR);
    let output = match rsync::output(&["-avnc", "--delete", "-e", &ssh_arg, &source, &dest]) {
        Ok(output) => output,
        Err(e) => {
            issues.push(format!("Failed to run rsync sync check: {e}"));
            return;
        }
    };

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        issues.push(format!("rsync sync check failed: {stderr}"));
        return;
    }

    let stdout = String::from_utf8_lossy(&output.stdout);
    let changed: Vec<&str> = stdout
        .lines()
        .filter(|line| {
            let line = line.trim();
            // Skip rsync summary/header lines and directory-only entries
            !line.is_empty()
                && !line.starts_with("sending ")
                && !line.starts_with("sent ")
                && !line.starts_with("total ")
                && !line.ends_with('/')
        })
        .collect();

    if !changed.is_empty() {
        issues.push(format!(
            "Local .bones/ is out of sync with remote (run 'bonesdeploy push'). Changed files:\n{}",
            changed.iter().map(|f| format!("      {f}")).collect::<Vec<_>>().join("\n")
        ));
    }
}

```

`crates/bonesdeploy/src/commands/init_config.rs`:

```rs
use crate::config;
use crate::infra::git;

use anyhow::{Result, anyhow};
use shared::config::validate_host;
use shared::paths;

pub struct InitArgs {
    pub non_interactive: bool,
    pub setup_remote: bool,
    pub project_name: Option<String>,
    pub branch: Option<String>,
    pub remote: Option<String>,
    pub host: Option<String>,
    pub port: Option<String>,
}

pub(crate) fn collect_non_interactive(
    project_name_hint: &str,
    existing_config: Option<&config::Bones>,
    args: &InitArgs,
) -> Result<config::Bones> {
    let project_name = resolve_project_name(args, existing_config, project_name_hint)?;
    let remote_name = resolve_remote_name(args, existing_config);
    let inferred_remote = infer_remote_details(&remote_name)?;
    let host = resolve_host(args, existing_config, inferred_remote.as_ref())?;
    let branch = resolve_branch(args, existing_config);
    let port = resolve_port(args, existing_config, inferred_remote.as_ref());
    validate_host(&host)?;

    let repo_path = resolve_repo_path(&project_name, existing_config, inferred_remote.as_ref());
    let project_root =
        seed_path_override(existing_config, |cfg| &cfg.project_root, &project_name, config::default_project_root_for);
    let deploy_on_push = existing_config.is_none_or(|cfg| cfg.deploy_on_push);
    let releases_keep = existing_config.map_or(5, |cfg| cfg.releases_keep.max(1));

    let ssl_enabled = existing_config.is_some_and(|cfg| cfg.ssl_enabled);
    let domain = existing_config.map_or_else(String::new, |cfg| cfg.domain.clone());
    let email = existing_config.map_or_else(String::new, |cfg| cfg.email.clone());

    Ok(config::Bones {
        remote_name,
        project_name,
        host,
        port,
        repo_path,
        project_root,
        branch,
        deploy_on_push,
        releases_keep,
        ssl_enabled,
        domain,
        email,
        ..Default::default()
    })
}

fn resolve_project_name(
    args: &InitArgs,
    existing_config: Option<&config::Bones>,
    project_name_hint: &str,
) -> Result<String> {
    args.project_name
        .clone()
        .filter(|v| !v.is_empty())
        .or_else(|| existing_config.and_then(|cfg| non_empty(&cfg.project_name)))
        .or_else(|| {
            let name = project_name_hint.to_string();
            (!name.is_empty()).then_some(name)
        })
        .ok_or_else(|| {
            anyhow!(
                "{} --project-name is required in non-interactive mode.\n\
                 Usage: bonesdeploy init --non-interactive --project-name <name> --host <host>",
                console::style("Error:").red().bold(),
            )
        })
}

fn resolve_remote_name(args: &InitArgs, existing_config: Option<&config::Bones>) -> String {
    args.remote
        .clone()
        .filter(|v| !v.is_empty())
        .or_else(|| existing_config.and_then(|cfg| non_empty(&cfg.remote_name)))
        .unwrap_or_else(|| String::from("production"))
}

fn infer_remote_details(remote_name: &str) -> Result<Option<git::RemoteConnectionDetails>> {
    if git::remote_exists(remote_name)? { git::infer_remote_connection_details(remote_name) } else { Ok(None) }
}

fn resolve_host(
    args: &InitArgs,
    existing_config: Option<&config::Bones>,
    inferred_remote: Option<&git::RemoteConnectionDetails>,
) -> Result<String> {
    args.host
        .clone()
        .filter(|v| !v.is_empty())
        .or_else(|| existing_config.and_then(|cfg| non_empty(&cfg.host)))
        .or_else(|| inferred_remote.map(|details| details.host.clone()))
        .ok_or_else(|| {
            anyhow!(
                "{} --host is required in non-interactive mode.\n\
                 Usage: bonesdeploy init --non-interactive --project-name <name> --host <host>",
                console::style("Error:").red().bold(),
            )
        })
}

fn resolve_branch(args: &InitArgs, existing_config: Option<&config::Bones>) -> String {
    args.branch
        .clone()
        .filter(|v| !v.is_empty())
        .or_else(|| existing_config.and_then(|cfg| non_empty(&cfg.branch)))
        .unwrap_or_else(|| String::from("main"))
}

fn resolve_port(
    args: &InitArgs,
    existing_config: Option<&config::Bones>,
    inferred_remote: Option<&git::RemoteConnectionDetails>,
) -> String {
    args.port
        .clone()
        .filter(|v| !v.is_empty())
        .or_else(|| existing_config.and_then(|cfg| non_empty(&cfg.port)))
        .or_else(|| inferred_remote.map(|details| details.port.clone()))
        .unwrap_or_else(|| String::from("22"))
}

pub fn non_empty(value: &str) -> Option<String> {
    let value = value.trim();
    (!value.is_empty()).then(|| value.to_string())
}

pub fn resolve_repo_path(
    project_name: &str,
    existing_config: Option<&config::Bones>,
    inferred_remote: Option<&git::RemoteConnectionDetails>,
) -> String {
    if let Some(details) = inferred_remote {
        return details.repo_path.clone();
    }

    existing_config.map(|cfg| cfg.repo_path.as_str()).filter(|value| !value.is_empty()).map_or_else(
        || paths::default_repo_path_for(project_name),
        |value| value.replace("<project_name>", project_name),
    )
}

pub fn seed_path_override(
    existing_config: Option<&config::Bones>,
    field: impl Fn(&config::Bones) -> &String,
    current_project_name: &str,
    default_for: fn(&str) -> String,
) -> String {
    let Some(cfg) = existing_config else { return String::new() };
    let value = field(cfg);
    if value.is_empty() {
        return String::new();
    }
    let resolved = value.replace("<project_name>", current_project_name);
    if resolved == default_for(current_project_name) { String::new() } else { resolved }
}

```

`crates/bonesdeploy/src/commands/init_project.rs`:

```rs
use std::fs;
use std::os::unix::fs as unix_fs;
use std::path::Path;

use anyhow::{Context, Result, bail};
use console::style;

use crate::commands::init_config;
pub use crate::commands::init_config::InitArgs;
use crate::commands::remote_setup;
use crate::config;
use crate::infra::bonesinfra;
use crate::infra::bonesinfra_cli;
use crate::infra::embedded;
use crate::infra::git;
use crate::ui::prompts;
use shared::config::{default_deploy_user, release_group_for, runtime_group_for, runtime_user_for};
use shared::paths;

pub fn run(args: &InitArgs) -> Result<bool> {
    git::ensure_git_repository()?;

    println!("Preparing local bonesinfra...");
    bonesinfra::prefetch()?;
    println!("Local bonesinfra ready.");

    let bones_dir = Path::new(paths::LOCAL_BONES_DIR);
    let had_bones_entry = fs::symlink_metadata(bones_dir).is_ok();
    let has_live_bones_dir = bones_dir.exists();
    let is_fresh = !has_live_bones_dir;

    let mut initial_project_name: Option<String> = None;

    if is_fresh {
        let project_name = resolve_project_name(args)?;
        let config_dir = config::bones_config_dir(&project_name);

        println!("Creating {}...", config_dir.display());
        if config_dir.exists() && !config_dir.is_dir() {
            fs::remove_file(&config_dir)
                .with_context(|| format!("Stale file at {}, cannot create directory", config_dir.display()))?;
        }
        fs::create_dir_all(&config_dir)?;
        embedded::scaffold(&config_dir)?;

        if had_bones_entry {
            fs::remove_file(bones_dir)
                .with_context(|| format!("Failed to remove stale {} symlink", bones_dir.display()))?;
        }
        unix_fs::symlink(&config_dir, bones_dir)?;
        println!("Symlinked .bones -> {}", config_dir.display());

        let seed = config::Bones { project_name: project_name.clone(), ..Default::default() };
        config::save(&seed, Path::new(paths::LOCAL_BONES_TOML))?;

        initial_project_name = Some(project_name);
    } else {
        println!(".bones/ already exists, keeping existing local bones state.");
    }

    update_gitignore()?;

    let bones_toml = Path::new(paths::LOCAL_BONES_TOML);
    let cfg = load_or_collect_config(bones_toml, args)?;

    if let Some(ref initial) = initial_project_name
        && cfg.project_name != *initial
    {
        let old_dir = config::bones_config_dir(initial);
        let new_dir = config::bones_config_dir(&cfg.project_name);
        fs::rename(&old_dir, &new_dir)?;
        fs::remove_file(bones_dir)?;
        unix_fs::symlink(&new_dir, bones_dir)?;
        println!("Renamed centralized folder to {}.bones", cfg.project_name);
    }

    config::save(&cfg, bones_toml)?;
    println!("Saved config to {}", paths::LOCAL_BONES_TOML);

    if is_fresh {
        let runtime_toml = Path::new(paths::LOCAL_BONES_RUNTIME_TOML);
        seed_runtime_config(args, &cfg.project_name, bones_dir, runtime_toml)?;
    }
    ensure_local_remote(&cfg)?;

    symlink_pre_push()?;

    let remote_setup_ran = args.setup_remote || (!args.non_interactive && prompts::confirm_remote_setup()?);
    if remote_setup_ran {
        remote_setup::run()?;
    } else {
        print_follow_up_hint();
    }

    Ok(remote_setup_ran)
}

fn print_follow_up_hint() {
    println!();
    println!("{}", style("Next:").cyan().bold());
    println!("Run {} to sync {} to the remote.", style("bonesdeploy push").cyan(), style(".bones/").cyan());
}

fn seed_runtime_config(args: &InitArgs, project_name: &str, bones_dir: &Path, runtime_toml: &Path) -> Result<()> {
    let template = if args.non_interactive {
        None
    } else {
        let available = embedded::runtime_names();
        prompts::choose_template(&available)?
    };

    if let Some(ref template_name) = template {
        let defaults = embedded::runtime_defaults(template_name)?;
        let answers = if args.non_interactive {
            serde_json::Value::Object(defaults.clone())
        } else {
            let questions = bonesinfra_cli::runtime_questions(template_name)?;
            prompts::prompt_runtime_questions(&questions, &serde_json::Value::Object(defaults.clone()))?
        };
        let mut map = answers.as_object().cloned().unwrap_or(defaults);
        inject_runtime_identity(&mut map, project_name);
        config::save_runtime(&map, runtime_toml)?;
        embedded::scaffold_runtime_deployment(template_name, bones_dir)?;
        println!("Applied runtime template: {template_name}");
        println!("Saved runtime config to {}", paths::LOCAL_BONES_RUNTIME_TOML);
    } else {
        let mut vars = embedded::base_runtime_defaults()?;
        inject_runtime_identity(&mut vars, project_name);
        config::save_runtime(&vars, runtime_toml)?;
        println!("Seeded {} from kit defaults", paths::LOCAL_BONES_RUNTIME_TOML);
    }

    Ok(())
}

fn inject_runtime_identity(vars: &mut serde_json::Map<String, serde_json::Value>, project_name: &str) {
    vars.insert("runtime_user".into(), serde_json::Value::String(runtime_user_for(project_name)));
    vars.insert("runtime_group".into(), serde_json::Value::String(runtime_group_for(project_name)));
    vars.insert("release_group".into(), serde_json::Value::String(release_group_for(project_name)));
}

fn collect_from_seed(
    project_name_hint: &str,
    existing_config: Option<&config::Bones>,
    args: &InitArgs,
) -> Result<config::Bones> {
    let project_name = cli_or_prompt(
        args.project_name.as_ref(),
        existing_config.and_then(|cfg| init_config::non_empty(&cfg.project_name)),
        || prompts::prompt_project_name(project_name_hint, existing_config),
    )?;
    let branch = cli_or_prompt(args.branch.as_ref(), None, || prompts::prompt_branch(existing_config))?;
    let remote_name = cli_or_prompt(args.remote.as_ref(), None, || prompts::prompt_remote_name(existing_config))?;
    let inferred_remote =
        if git::remote_exists(&remote_name)? { git::infer_remote_connection_details(&remote_name)? } else { None };
    let host =
        cli_or_prompt(args.host.as_ref(), None, || prompts::prompt_host(existing_config, inferred_remote.as_ref()))?;
    let port =
        cli_or_prompt(args.port.as_ref(), None, || prompts::prompt_port(existing_config, inferred_remote.as_ref()))?;
    let repo_path = init_config::resolve_repo_path(&project_name, existing_config, inferred_remote.as_ref());
    let project_root = init_config::seed_path_override(
        existing_config,
        |cfg| &cfg.project_root,
        &project_name,
        config::default_project_root_for,
    );
    let deploy_on_push = existing_config.is_none_or(|cfg| cfg.deploy_on_push);
    let releases_keep = existing_config.map_or(5, |cfg| cfg.releases_keep.max(1));

    let ssl_enabled = existing_config.is_some_and(|cfg| cfg.ssl_enabled);
    let domain = existing_config.map_or_else(String::new, |cfg| cfg.domain.clone());
    let email = existing_config.map_or_else(String::new, |cfg| cfg.email.clone());

    Ok(config::Bones {
        remote_name,
        project_name,
        host,
        port,
        repo_path,
        project_root,
        branch,
        deploy_on_push,
        releases_keep,
        ssl_enabled,
        domain,
        email,
        ..Default::default()
    })
}

#[cfg(test)]
fn collect_non_interactive(
    project_name_hint: &str,
    existing_config: Option<&config::Bones>,
    args: &InitArgs,
) -> Result<config::Bones> {
    init_config::collect_non_interactive(project_name_hint, existing_config, args)
}

fn resolve_project_name(args: &InitArgs) -> Result<String> {
    if let Some(name) = args.project_name.as_ref().filter(|v| !v.is_empty()) {
        return Ok(name.trim().to_string());
    }
    if args.non_interactive {
        bail!(
            "--project-name is required in non-interactive mode.\nUsage: bonesdeploy init --non-interactive --project-name <name> --host <host>"
        );
    }
    let hint = config::repo_directory_name()?;
    prompts::prompt_project_name(&hint, None)
}

fn cli_or_prompt(
    cli_value: Option<&String>,
    existing_value: Option<String>,
    prompt: impl FnOnce() -> Result<String>,
) -> Result<String> {
    match cli_value {
        Some(v) if !v.is_empty() => Ok(v.trim().to_string()),
        _ => existing_value.map_or_else(prompt, Ok),
    }
}

fn load_or_collect_config(bones_toml: &Path, args: &InitArgs) -> Result<config::Bones> {
    if bones_toml.exists() {
        let existing = config::load(bones_toml)?;
        if config::is_configured(&existing) {
            println!("Loading existing config from {}...", paths::LOCAL_BONES_TOML);
            return Ok(existing);
        }
        let project_name = config::repo_directory_name()?;
        if args.non_interactive {
            return init_config::collect_non_interactive(&project_name, Some(&existing), args);
        }
        return collect_from_seed(&project_name, Some(&existing), args);
    }

    let project_name = config::repo_directory_name()?;

    if args.non_interactive {
        return init_config::collect_non_interactive(&project_name, None, args);
    }

    collect_from_seed(&project_name, None, args)
}

fn update_gitignore() -> Result<()> {
    let gitignore = Path::new(".gitignore");
    let entry = paths::LOCAL_BONES_DIR;

    if gitignore.exists() {
        let content = fs::read_to_string(gitignore)?;
        if content.lines().any(|line| line.trim() == entry) {
            return Ok(());
        }
        let separator = if content.ends_with('\n') { "" } else { "\n" };
        fs::write(gitignore, format!("{content}{separator}{entry}\n"))?;
    } else {
        fs::write(gitignore, format!("{entry}\n"))?;
    }

    println!("Added .bones to .gitignore");
    Ok(())
}

pub(crate) fn symlink_pre_push() -> Result<()> {
    let hooks_dir = Path::new(paths::GIT_HOOKS_DIR);
    fs::create_dir_all(hooks_dir)?;

    let link = hooks_dir.join(paths::PRE_PUSH_HOOK_NAME);
    let target = Path::new(paths::PRE_PUSH_HOOK_TARGET);

    if fs::symlink_metadata(&link).is_ok() {
        fs::remove_file(&link).with_context(|| format!("Failed to remove existing {}", link.display()))?;
    }

    unix_fs::symlink(target, &link).with_context(|| format!("Failed to symlink {}", link.display()))?;

    println!("Symlinked {} -> {}", paths::GIT_PRE_PUSH_HOOK, paths::PRE_PUSH_HOOK_TARGET);
    Ok(())
}

fn ensure_local_remote(cfg: &config::Bones) -> Result<()> {
    if git::remote_exists(&cfg.remote_name)? {
        return Ok(());
    }

    let remote_url = format!("{}@{}:{}", default_deploy_user(), cfg.host, cfg.repo_path);
    git::add_remote(&cfg.remote_name, &remote_url)?;
    println!("Configured local git remote {} -> {}", cfg.remote_name, remote_url);
    Ok(())
}

#[cfg(test)]
#[path = "tests/test_init_project.rs"]
mod test_init_project;

```

`crates/bonesdeploy/src/commands/manage.rs`:

```rs
use std::path::Path;
use std::process::Command;

use anyhow::{Context, Result, bail};

use crate::config;
use shared::config::default_deploy_user;
use shared::paths;

pub fn run() -> Result<()> {
    let bones_toml = Path::new(paths::LOCAL_BONES_TOML);
    let cfg = config::load(bones_toml)?;

    let remote_bones_toml = cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).repo_bones_toml;
    let remote_command = format!("bonesremote manage --config {}", shell_quote_single(&remote_bones_toml));

    let target = format!("{}@{}", default_deploy_user(), cfg.host);

    let status = Command::new("ssh")
        .arg("-t")
        .arg("-p")
        .arg(&cfg.port)
        .arg(&target)
        .arg(&remote_command)
        .status()
        .context("Failed to launch ssh for remote manage session")?;

    if !status.success() {
        bail!("Remote manage session failed with status {status}");
    }

    Ok(())
}

fn shell_quote_single(value: &str) -> String {
    format!("'{}'", value.replace('\'', "'\"'\"'"))
}

#[cfg(test)]
mod tests {
    use super::shell_quote_single;
    use shared::paths;

    /// Wraps a plain value in single quotes to prevent whitespace and token splitting.
    #[test]
    fn shell_quote_single_wraps_plain_value_in_single_quotes() {
        let path = paths::default_project_root_for("acme");
        assert_eq!(shell_quote_single(&path), format!("'{path}'"));
    }

    /// Escapes embedded single quotes safely for remote shell execution.
    #[test]
    fn shell_quote_single_escapes_embedded_single_quotes() {
        assert_eq!(shell_quote_single("it'works"), "'it'\"'\"'works'");
    }

    /// Returns an explicit empty string for empty input, not a zero-length argument.
    #[test]
    fn shell_quote_single_handles_empty_string() {
        assert_eq!(shell_quote_single(""), "''");
    }
}

```

`crates/bonesdeploy/src/commands/mod.rs`:

```rs
pub(crate) mod config;
pub(crate) mod init_config;

pub mod deploy_project;
pub mod doctor;
pub mod init_project;
pub mod manage;
pub mod pull_state;
pub mod push_state;
pub mod remote_data;
pub mod remote_runtime;
pub mod remote_setup;
pub mod remote_ssl;
pub mod rollback;
pub mod update;
pub mod update_release;
pub mod version;

pub use crate::cli::args::Cli;
pub use crate::cli::dispatch::run;

```

`crates/bonesdeploy/src/commands/pull_state.rs`:

```rs
use std::fs;
use std::os::unix::fs as unix_fs;
use std::path::Path;

use anyhow::{Context, Result, bail};
use console::style;

use crate::config;
use crate::infra::git;
use crate::infra::rsync;
use shared::config::default_deploy_user;
use shared::paths;

use crate::commands::init_project;

pub fn run() -> Result<()> {
    git::ensure_git_repository()?;

    let target = resolve_pull_target()?;
    let remote_bones = format!("{}@{}:{}/{}/", target.user, target.host, target.repo_path, paths::BONES_DIR);

    println!("Pulling .bones/ from {remote_bones}...");

    let bones_dir = Path::new(paths::LOCAL_BONES_DIR);
    if !bones_dir.exists() {
        let project_name = config::repo_directory_name()?;
        let config_dir = config::bones_config_dir(&project_name);
        if config_dir.exists() && !config_dir.is_dir() {
            fs::remove_file(&config_dir)
                .with_context(|| format!("Stale file at {}, cannot create directory", config_dir.display()))?;
        }
        fs::create_dir_all(&config_dir)?;
        unix_fs::symlink(&config_dir, bones_dir)?;
    }

    rsync_bones(&target)?;
    init_project::symlink_pre_push()?;

    println!("\n{} .bones/ pulled from remote.", style("Done!").green().bold());
    Ok(())
}

fn resolve_pull_target() -> Result<git::RemoteConnectionDetails> {
    let bones_toml = Path::new(paths::LOCAL_BONES_TOML);
    if bones_toml.exists() {
        let cfg = config::load(bones_toml)?;
        return Ok(git::RemoteConnectionDetails {
            user: default_deploy_user(),
            host: cfg.host,
            port: cfg.port,
            repo_path: cfg.repo_path,
        });
    }

    let remote_name = resolve_remote_name()?;
    let details = git::infer_remote_connection_details(&remote_name)?
        .with_context(|| format!("Remote '{remote_name}' must use an SSH-style URL ending in .git"))?;

    Ok(details)
}

fn resolve_remote_name() -> Result<String> {
    if git::remote_exists("production")? {
        return Ok(String::from("production"));
    }

    let remotes = git::list_remotes()?;
    match remotes.as_slice() {
        [] => bail!("No git remotes configured. Add a deployment remote before running bonesdeploy pull."),
        [remote] => Ok(remote.clone()),
        _ => {
            bail!("Multiple git remotes configured. Keep .bones/bones.toml or name the deployment remote 'production'.")
        }
    }
}

fn rsync_bones(target: &git::RemoteConnectionDetails) -> Result<()> {
    let source = format!("{}@{}:{}/{}/", target.user, target.host, target.repo_path, paths::BONES_DIR);
    let ssh_arg = format!("ssh -p {} -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null", target.port);
    let dest = format!("{}/", paths::LOCAL_BONES_DIR);
    let status = rsync::status(&["-av", "--delete", "-e", &ssh_arg, &source, &dest])?;

    if !status.success() {
        bail!("rsync failed");
    }

    Ok(())
}

```

`crates/bonesdeploy/src/commands/push_state.rs`:

```rs
use std::path::Path;

use anyhow::{Result, bail};
use console::style;

use crate::config;
use crate::infra::rsync;
use crate::infra::ssh;
use shared::config::default_deploy_user;
use shared::paths;

pub async fn run() -> Result<()> {
    let bones_toml = Path::new(paths::LOCAL_BONES_TOML);
    let cfg = config::load(bones_toml)?;

    let repo_path = &cfg.repo_path;
    let remote_bones = format!("{repo_path}/{}/", paths::BONES_DIR);

    // rsync .bones/ to remote
    println!("Syncing .bones/ to {remote_bones}...");
    sync_bones_directory(&cfg)?;

    // Connect via SSH for post-rsync setup
    let session = ssh::connect(&cfg).await?;

    println!("Cleaning sample hooks from remote...");
    let cmd = format!("find {repo_path}/{}/ -maxdepth 1 -name '*.sample' -delete 2>/dev/null; true", paths::HOOKS_DIR);
    ssh::run_cmd(&session, &cmd).await?;

    println!("Symlinking hooks...");
    let cmd = format!(
        "for hook in {repo_path}/{}/{}/{}; do \
            name=$(basename \"$hook\"); \
            ln -sf \"$hook\" \"{repo_path}/{}/$name\"; \
          done",
        paths::BONES_DIR,
        paths::HOOKS_DIR,
        "*",
        paths::HOOKS_DIR
    );
    ssh::run_cmd(&session, &cmd).await?;

    session.close().await?;

    println!("\n{} .bones/ synced to remote.", style("Done!").green().bold());

    Ok(())
}

pub(crate) fn sync_bones_directory(cfg: &config::Bones) -> Result<()> {
    let user = default_deploy_user();
    let host = &cfg.host;
    let port = &cfg.port;
    let repo_path = &cfg.repo_path;
    let dest = format!("{user}@{host}:{repo_path}/{}/", paths::BONES_DIR);

    let ssh_arg = format!("ssh -p {port} -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null");
    let source = format!("{}/", paths::LOCAL_BONES_DIR);
    let status = rsync::status(&["-av", "--delete", "-e", &ssh_arg, &source, &dest])?;

    if !status.success() {
        bail!("rsync failed");
    }

    Ok(())
}

```

`crates/bonesdeploy/src/commands/remote_data.rs`:

```rs
use anyhow::Result;
use serde_json::{Map, Value};
use shared::config as shared_config;
use shared::paths::{ssl_certificate_key_path, ssl_certificate_path};

use crate::config;

pub(super) fn base(cfg: &config::Bones, web_root: &str) -> Result<Map<String, Value>> {
    let paths = cfg.deployment_paths(web_root);
    let mut vars = Map::new();

    vars.insert(String::from("ssh_port"), Value::String(cfg.port.clone()));
    vars.insert(String::from("deploy_user"), Value::String(shared_config::default_deploy_user()));
    vars.insert(String::from("runtime_user"), Value::String(shared_config::runtime_user_for(&cfg.project_name)));
    vars.insert(String::from("runtime_group"), Value::String(shared_config::runtime_group_for(&cfg.project_name)));
    vars.insert(String::from("release_group"), Value::String(shared_config::release_group_for(&cfg.project_name)));
    vars.insert(String::from("project_root_parent"), Value::String(paths.project_root_parent.clone()));
    vars.insert(String::from("project_root"), Value::String(cfg.project_root.clone()));
    vars.insert(String::from("web_root"), Value::String(web_root.to_string()));
    vars.insert(String::from("project_name"), Value::String(cfg.project_name.clone()));
    vars.insert(String::from("preview_domain"), Value::String(cfg.preview_domain.clone()));
    vars.insert(String::from("repo_path"), Value::String(cfg.repo_path.clone()));
    vars.insert(String::from("paths"), serde_json::to_value(paths)?);

    Ok(vars)
}

pub fn ssl(cfg: &config::Bones, web_root: &str, domain: &str, email: &str) -> Result<Value> {
    let mut vars = base(cfg, web_root)?;
    vars.insert(String::from("ssl_domain"), Value::String(domain.to_string()));
    vars.insert(String::from("ssl_email"), Value::String(email.to_string()));
    vars.insert(String::from("nginx_ssl_certificate_path"), Value::String(ssl_certificate_path(domain)));
    vars.insert(String::from("nginx_ssl_certificate_key_path"), Value::String(ssl_certificate_key_path(domain)));
    Ok(Value::Object(vars))
}

#[cfg(test)]
mod tests {
    use crate::config::Bones;

    use super::{base, ssl};

    fn test_cfg() -> Bones {
        Bones {
            project_name: String::from("test"),
            repo_path: String::from("/home/git/test.git"),
            project_root: String::from("/srv/test"),
            host: String::from("example.com"),
            port: String::from("22"),
            branch: String::from("master"),
            remote_name: String::from("production"),
            deploy_on_push: true,
            ..Default::default()
        }
    }

    /// Passes the SSL domain and email into the deploy data sent to bonesinfra
    #[test]
    fn ssl_data_includes_domain_and_email() -> anyhow::Result<()> {
        let cfg = test_cfg();
        let vars = ssl(&cfg, "public", "app.example.com", "ops@example.com")?;

        assert_eq!(vars.get("ssl_domain"), Some(&serde_json::Value::String(String::from("app.example.com"))));
        assert_eq!(vars.get("ssl_email"), Some(&serde_json::Value::String(String::from("ops@example.com"))));
        Ok(())
    }

    #[test]
    fn base_data_includes_preview_domain() -> anyhow::Result<()> {
        let mut cfg = test_cfg();
        cfg.preview_domain = String::from("test-example-com.nip.io");

        let vars = base(&cfg, "public")?;

        assert_eq!(
            vars.get("preview_domain"),
            Some(&serde_json::Value::String(String::from("test-example-com.nip.io")))
        );
        Ok(())
    }
}

```

`crates/bonesdeploy/src/commands/remote_runtime.rs`:

```rs
use std::path::Path;

use anyhow::{Result, bail};

use crate::infra::bonesinfra_cli;
use crate::infra::git;
use crate::ui::prompts;
use shared::paths;

pub fn run() -> Result<()> {
    git::ensure_git_repository()?;

    let runtime_toml = Path::new(paths::LOCAL_BONES_RUNTIME_TOML);
    if !runtime_toml.exists() {
        bail!("{} does not exist. Run `bonesdeploy init` first.", paths::LOCAL_BONES_RUNTIME_TOML);
    }

    if !prompts::confirm_remote_runtime()? {
        println!("Skipped remote runtime apply.");
        return Ok(());
    }

    let bones_toml = Path::new(paths::LOCAL_BONES_TOML);
    println!("Applying runtime using local bonesinfra ...");

    bonesinfra_cli::run(&[
        "runtime",
        "apply",
        "--config",
        bones_toml.to_str().unwrap_or(".bones/bones.toml"),
        "--runtime-config",
        runtime_toml.to_str().unwrap_or(".bones/runtime.toml"),
    ])?;

    println!("Runtime apply completed.");
    Ok(())
}

```

`crates/bonesdeploy/src/commands/remote_setup.rs`:

```rs
use std::path::Path;

use anyhow::{Context, Result};
use console::style;
use serde_json::Value;

use shared::config as shared_config;
use shared::paths;

use super::remote_data;
use crate::config;
use crate::infra::bonesinfra_cli;
use crate::infra::bootstrap_ssh;

pub fn run() -> Result<()> {
    let bones_toml = Path::new(paths::LOCAL_BONES_TOML);
    let cfg = config::load(bones_toml)?;
    let runtime = shared_config::load_runtime(Path::new(paths::LOCAL_BONES_DIR))?;

    let ssh_user = bootstrap_ssh::resolve(Some(&cfg.ssh_user));

    let mut deploy_data = Value::Object(remote_data::base(&cfg, &runtime.web_root)?);
    let host = cfg.host;
    if let Value::Object(ref mut map) = deploy_data {
        map.insert(String::from("ssh_user"), Value::String(ssh_user));
        map.insert(String::from("host"), Value::String(host));
    }

    let json = serde_json::to_string(&deploy_data).context("Failed to serialize deploy data")?;
    bonesinfra_cli::run_with_stdin(
        &["setup", "apply", "--config", bones_toml.to_str().unwrap_or(".bones/bones.toml")],
        &json,
    )?;

    println!("{} Remote setup complete.", style("Done!").green().bold());

    Ok(())
}

```

`crates/bonesdeploy/src/commands/remote_ssl.rs`:

```rs
use std::path::Path;

use anyhow::{Context, Result, bail};
use console::style;
use serde_json::Value;

use shared::config as shared_config;
use shared::paths;

use super::push_state;
use super::remote_data;
use crate::config;
use crate::infra::bonesinfra_cli;
use crate::infra::bootstrap_ssh;
use crate::ui::prompts;

pub fn run(domain: Option<String>, email: Option<String>) -> Result<()> {
    let bones_toml = Path::new(paths::LOCAL_BONES_TOML);
    let mut cfg = config::load(bones_toml)?;
    let runtime = shared_config::load_runtime(Path::new(paths::LOCAL_BONES_DIR))?;

    if let Some(value) = domain {
        cfg.domain = value.trim().to_string();
    } else if cfg.domain.is_empty() {
        cfg.domain = prompts::prompt_ssl_domain(Some(&cfg))?;
    }

    if let Some(value) = email {
        cfg.email = value.trim().to_string();
    } else if cfg.email.is_empty() {
        cfg.email = prompts::prompt_ssl_email(Some(&cfg))?;
    }

    if cfg.domain.is_empty() {
        bail!("SSL domain is missing. Pass --domain or set domain in .bones/bones.toml");
    }

    if cfg.email.is_empty() {
        bail!("SSL email is missing. Pass --email or set email in .bones/bones.toml");
    }

    config::save(&cfg, bones_toml)?;

    if !prompts::confirm_remote_ssl()? {
        println!("Skipped remote SSL setup.");
        return Ok(());
    }

    println!(
        "Running {} against {} for {}...",
        style("remote ssl").cyan().bold(),
        style(&cfg.host).cyan(),
        style(&cfg.domain).cyan(),
    );

    let ssh_user = bootstrap_ssh::resolve(Some(&cfg.ssh_user));
    let mut deploy_data = remote_data::ssl(&cfg, &runtime.web_root, &cfg.domain, &cfg.email)?;
    if let Value::Object(ref mut map) = deploy_data {
        map.insert(String::from("ssh_user"), Value::String(ssh_user));
        map.insert(String::from("host"), Value::String(cfg.host.clone()));
        map.insert(String::from("ssh_port"), Value::String(cfg.port.clone()));
    }

    let json = serde_json::to_string(&deploy_data).context("Failed to serialize deploy data")?;
    bonesinfra_cli::run_with_stdin(
        &["ssl", "apply", "--config", bones_toml.to_str().unwrap_or(".bones/bones.toml")],
        &json,
    )?;

    config::save(&cfg, bones_toml)?;
    push_state::sync_bones_directory(&cfg)?;

    println!("\n{} SSL setup complete.", style("Done!").green().bold());

    Ok(())
}

```

`crates/bonesdeploy/src/commands/rollback.rs`:

```rs
use std::path::Path;

use anyhow::Result;
use console::style;

use crate::config;
use crate::infra::ssh;
use shared::paths;

pub async fn run() -> Result<()> {
    let bones_toml = Path::new(paths::LOCAL_BONES_TOML);
    let cfg = config::load(bones_toml)?;

    let remote_bones_toml = cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).repo_bones_toml;

    println!("Rolling back {} on {}...", style(&cfg.project_name).cyan().bold(), style(&cfg.host).cyan());

    let session = ssh::connect(&cfg).await?;
    let command = format!("bonesremote release rollback --config '{remote_bones_toml}'");
    ssh::stream_cmd(&session, &command).await?;
    session.close().await?;

    println!("\n{} Rollback complete.", style("Done!").green().bold());

    Ok(())
}

```

`crates/bonesdeploy/src/commands/tests/test_init_project.rs`:

```rs
use std::env;
use std::fs;
use std::path::{Path, PathBuf};
use std::process::Command;
use std::sync::{Mutex, MutexGuard, OnceLock};

use super::{collect_non_interactive, run};
use crate::commands::init_config::InitArgs;

use anyhow::{Result, bail};
use shared::paths;
use tempfile::TempDir;

use crate::config::Bones;

fn test_lock() -> &'static Mutex<()> {
    static LOCK: OnceLock<Mutex<()>> = OnceLock::new();
    LOCK.get_or_init(|| Mutex::new(()))
}

struct TestEnvironment {
    _lock: MutexGuard<'static, ()>,
    original_dir: PathBuf,
    original_home: Option<String>,
}

impl TestEnvironment {
    fn enter(repo_dir: &Path, home_dir: &Path) -> Result<Self> {
        let lock = test_lock().lock().map_err(|_| anyhow::anyhow!("test lock poisoned"))?;
        let original_dir = env::current_dir()?;
        let original_home = env::var("HOME").ok();

        env::set_current_dir(repo_dir)?;

        // Safety: these tests serialize access with a process-wide mutex and restore HOME on drop.
        unsafe {
            env::set_var("HOME", home_dir);
        }

        Ok(Self { _lock: lock, original_dir, original_home })
    }
}

impl Drop for TestEnvironment {
    fn drop(&mut self) {
        let _ = env::set_current_dir(&self.original_dir);

        match &self.original_home {
            Some(home) => {
                // Safety: these tests serialize access with a process-wide mutex and restore HOME on drop.
                unsafe {
                    env::set_var("HOME", home);
                }
            }
            None => {
                // Safety: these tests serialize access with a process-wide mutex and restore HOME on drop.
                unsafe {
                    env::remove_var("HOME");
                }
            }
        }
    }
}

fn init_args() -> InitArgs {
    InitArgs {
        non_interactive: true,
        setup_remote: false,
        project_name: Some(String::from("atlas")),
        branch: None,
        remote: None,
        host: Some(String::from("deploy.example.com")),
        port: None,
    }
}

fn create_git_repo(path: &Path) -> Result<()> {
    let status = Command::new("git").args(["init", "--quiet"]).current_dir(path).status()?;
    if !status.success() {
        bail!("git init failed with status {status}");
    }
    Ok(())
}

fn with_temp_repo(test: impl FnOnce(&Path, &Path) -> Result<()>) -> Result<()> {
    let temp = TempDir::new()?;
    let repo_dir = temp.path().join("repo");
    let home_dir = temp.path().join("home");

    fs::create_dir_all(&repo_dir)?;
    fs::create_dir_all(&home_dir)?;
    create_git_repo(&repo_dir)?;

    let _environment = TestEnvironment::enter(&repo_dir, &home_dir)?;

    test(&repo_dir, &home_dir)
}

fn incomplete_seed(project_name: &str) -> Bones {
    Bones {
        remote_name: String::from("production"),
        project_name: String::from(project_name),
        host: String::new(),
        port: String::from("22"),
        repo_path: String::new(),
        project_root: String::new(),
        branch: String::from("main"),
        deploy_on_push: true,
        ..Default::default()
    }
}

/// Uses seed config and CLI values without prompting when non-interactive mode is active.
#[test]
fn collect_non_interactive_uses_seed_and_cli_values_without_prompting() -> Result<()> {
    let seed = incomplete_seed("atlas");
    let args = InitArgs {
        non_interactive: true,
        setup_remote: false,
        project_name: None,
        branch: None,
        remote: None,
        host: Some(String::from("deploy.example.com")),
        port: None,
    };

    let cfg = collect_non_interactive("workspace", Some(&seed), &args)?;

    assert_eq!(cfg.project_name, "atlas");
    assert_eq!(cfg.host, "deploy.example.com");
    assert_eq!(cfg.branch, "main");
    assert_eq!(cfg.remote_name, "production");
    assert_eq!(cfg.repo_path, paths::default_repo_path_for("atlas"));

    Ok(())
}

/// Requires a host when neither seed config nor CLI provide one.
#[test]
fn collect_non_interactive_requires_host_when_seed_and_cli_are_missing_it() -> Result<()> {
    let seed = incomplete_seed("atlas");
    let args = InitArgs {
        non_interactive: true,
        setup_remote: false,
        project_name: None,
        branch: None,
        remote: None,
        host: None,
        port: None,
    };

    let result = collect_non_interactive("workspace", Some(&seed), &args);
    let Err(err) = result else {
        bail!("missing host should fail");
    };
    assert!(err.to_string().contains("--host is required"));

    Ok(())
}

/// Materializes the base bonesdeploy kit and runtime config during init.
#[test]
fn init_materializes_base_bones_assets() -> Result<()> {
    with_temp_repo(|repo_dir, _home_dir| {
        run(&init_args())?;

        let bones_dir = repo_dir.join(".bones");
        assert!(bones_dir.join("bones.toml").is_file());
        assert!(bones_dir.join("runtime.toml").is_file());
        assert!(bones_dir.join("hooks/hooks.sh").is_file());
        assert!(bones_dir.join("deployment/01_install_build_deps.sh").is_file());
        assert!(bones_dir.join("deployment/02_run_build.sh").is_file());
        let runtime_toml = fs::read_to_string(bones_dir.join("runtime.toml"))?;
        assert!(runtime_toml.contains("runtime_user = \"atlas\""));
        assert!(runtime_toml.contains("permissions"));
        assert!(runtime_toml.contains("shared"));

        let config_root = paths::bones_config_root().join("atlas.bones");
        assert!(config_root.join("hooks/hooks.sh").is_file());

        Ok(())
    })
}

/// Keeps an already materialized local bones scaffold intact when init is run again.
#[test]
fn init_rerun_preserves_existing_bones_assets() -> Result<()> {
    with_temp_repo(|repo_dir, _home_dir| {
        run(&init_args())?;

        let sentinel = repo_dir.join(".bones/hooks/hooks.sh");
        let original = fs::read_to_string(&sentinel)?;

        run(&init_args())?;

        assert!(sentinel.is_file());
        assert_eq!(fs::read_to_string(&sentinel)?, original);

        Ok(())
    })
}

/// Repairs a dangling .bones symlink instead of failing with EEXIST.
#[test]
fn init_repairs_dangling_bones_symlink() -> Result<()> {
    with_temp_repo(|repo_dir, home_dir| {
        let config_root = home_dir.join(".config/bonesdeploy");
        fs::create_dir_all(&config_root)?;
        std::os::unix::fs::symlink(config_root.join("missing.bones"), repo_dir.join(".bones"))?;

        run(&init_args())?;

        let bones_dir = repo_dir.join(".bones");
        assert!(bones_dir.join("bones.toml").is_file());
        assert_eq!(fs::read_link(&bones_dir)?, paths::bones_config_root().join("atlas.bones"));

        Ok(())
    })
}

```

`crates/bonesdeploy/src/commands/update.rs`:

```rs
use std::fs;
use std::os::unix::fs::PermissionsExt;
use std::path::{Path, PathBuf};
use std::process::Command;

use anyhow::{Context, Result, bail};
use console::style;
use tempfile::TempDir;

use super::update_release;
use shared::paths;

const SOURCE_REPO_URL: &str = "https://github.com/AlextheYounga/bonesdeploy.git";
const SOURCE_BRANCH: &str = "master";

#[derive(Clone, Copy)]
pub struct Options {
    pub skip_local: bool,
    pub skip_remote: bool,
}

pub async fn run(options: Options) -> Result<()> {
    println!("{}", style("bonesdeploy update").bold());

    let current_local = update_release::current_local_version();
    let current_remote = update_release::current_remote_version();

    println!("Current local version: {}", style(&current_local).cyan());
    println!("Current remote version: {}", style(&current_remote).cyan());

    if options.skip_local && options.skip_remote {
        println!("{} Nothing to update.", style("Done!").green());
        return Ok(());
    }

    println!("Source branch: {}", style(SOURCE_BRANCH).cyan());

    let temp_dir = TempDir::new().context("Failed to create temp directory")?;
    let temp_path = temp_dir.path();

    println!("Checking master version from {}...", style(SOURCE_REPO_URL).cyan());
    let source_dir = clone_master_source(temp_path)?;
    let master_versions = read_master_versions(&source_dir)?;
    println!("Master bonesdeploy version: {}", style(&master_versions.bonesdeploy).cyan());
    println!("Master bonesremote version: {}", style(&master_versions.bonesremote).cyan());

    if !options.skip_local {
        if current_local == master_versions.bonesdeploy {
            println!("{} Local bonesdeploy is already current.", style("Done!").green());
        } else {
            println!("{}", style("Updating local bonesdeploy...").cyan());
            update_release::update_local_from_source(SOURCE_REPO_URL)?;
            println!("{} Local update complete.", style("Done!").green());
        }

        refresh_local_bones_from_source(&source_dir, Path::new(paths::LOCAL_BONES_DIR))?;
    }

    if !options.skip_remote {
        if current_remote == master_versions.bonesremote {
            println!("{} Remote bonesremote is already current.", style("Done!").green());
        } else {
            println!("{}", style("Updating remote bonesremote...").cyan());
            update_release::update_remote_from_source(SOURCE_REPO_URL, &master_versions.bonesremote).await?;
            println!("{} Remote update complete.", style("Done!").green());
        }
    }

    println!("\n{} All updates complete.", style("Done!").green());

    Ok(())
}

fn clone_master_source(temp_path: &Path) -> Result<PathBuf> {
    let source_dir = temp_path.join("source");

    let clone_status = Command::new("git")
        .args(["clone", "--depth", "1", "--branch", SOURCE_BRANCH, SOURCE_REPO_URL])
        .arg(&source_dir)
        .status()
        .context("Failed to clone bonesdeploy repository")?;

    if !clone_status.success() {
        bail!("Failed to clone {SOURCE_REPO_URL} branch {SOURCE_BRANCH}");
    }

    Ok(source_dir)
}

struct MasterVersions {
    bonesdeploy: String,
    bonesremote: String,
}

fn read_master_versions(source_dir: &Path) -> Result<MasterVersions> {
    let bonesdeploy = read_package_version(&source_dir.join("crates/bonesdeploy/Cargo.toml"))?;
    let bonesremote = read_package_version(&source_dir.join("crates/bonesremote/Cargo.toml"))?;

    Ok(MasterVersions { bonesdeploy, bonesremote })
}

fn read_package_version(manifest: &Path) -> Result<String> {
    let content = fs::read_to_string(manifest).with_context(|| format!("Failed to read {}", manifest.display()))?;
    parse_package_version(&content)
        .with_context(|| format!("Failed to parse package version from {}", manifest.display()))
}

fn parse_package_version(manifest: &str) -> Result<String> {
    let value: toml::Value = toml::from_str(manifest)?;
    value
        .get("package")
        .and_then(|package| package.get("version"))
        .and_then(toml::Value::as_str)
        .filter(|version| !version.is_empty())
        .map(String::from)
        .ok_or_else(|| anyhow::anyhow!("missing [package] version"))
}

fn refresh_local_bones_from_source(source_dir: &Path, bones_dir: &Path) -> Result<()> {
    if !bones_dir.exists() {
        return Ok(());
    }

    println!("{}", style("Refreshing local .bones scaffold...").cyan());

    let kit_root = source_dir.join("crates/bonesdeploy/kit");
    sync_tree(&kit_root.join("hooks"), &bones_dir.join("hooks"), true)?;
    sync_tree(&deployment_source_root(source_dir, bones_dir), &bones_dir.join("deployment"), true)?;

    println!("{} Local .bones scaffold refreshed.", style("Done!").green());
    Ok(())
}

fn deployment_source_root(source_dir: &Path, bones_dir: &Path) -> PathBuf {
    let runtime_toml = bones_dir.join("runtime.toml");
    let Some(template) = selected_runtime_template(&runtime_toml) else {
        return source_dir.join("crates/bonesdeploy/kit/deployment");
    };

    let runtime_deployment = source_dir.join("crates/bonesdeploy/runtimes").join(template).join("deployment");
    if runtime_deployment.is_dir() { runtime_deployment } else { source_dir.join("crates/bonesdeploy/kit/deployment") }
}

fn selected_runtime_template(runtime_toml: &Path) -> Option<String> {
    let content = fs::read_to_string(runtime_toml).ok()?;
    let value: toml::Value = toml::from_str(&content).ok()?;
    value.get("template")?.as_str().map(String::from)
}

fn sync_tree(source_root: &Path, dest_root: &Path, executable: bool) -> Result<()> {
    if !source_root.is_dir() {
        return Ok(());
    }

    for entry in fs::read_dir(source_root).with_context(|| format!("Failed to read {}", source_root.display()))? {
        let entry = entry.with_context(|| format!("Failed to read entry in {}", source_root.display()))?;
        let file_type =
            entry.file_type().with_context(|| format!("Failed to read file type for {}", entry.path().display()))?;
        let source_path = entry.path();
        let dest_path = dest_root.join(entry.file_name());

        if file_type.is_dir() {
            fs::create_dir_all(&dest_path).with_context(|| format!("Failed to create {}", dest_path.display()))?;
            sync_tree(&source_path, &dest_path, executable)?;
            continue;
        }

        copy_file(&source_path, &dest_path, executable)?;
    }

    Ok(())
}

fn copy_file(source: &Path, dest: &Path, executable: bool) -> Result<()> {
    if let Some(parent) = dest.parent() {
        fs::create_dir_all(parent).with_context(|| format!("Failed to create {}", parent.display()))?;
    }

    fs::copy(source, dest).with_context(|| format!("Failed to copy {} to {}", source.display(), dest.display()))?;

    if executable {
        fs::set_permissions(dest, fs::Permissions::from_mode(0o755))
            .with_context(|| format!("Failed to set permissions on {}", dest.display()))?;
    }

    Ok(())
}

#[cfg(test)]
mod tests {
    use std::fs;
    use std::os::unix::fs::PermissionsExt;
    use std::path::Path;

    use anyhow::Result;
    use tempfile::TempDir;

    use super::{SOURCE_BRANCH, SOURCE_REPO_URL, parse_package_version, refresh_local_bones_from_source};

    /// Verifies the update source repository and branch constants are set to the canonical values.
    #[test]
    fn update_uses_master_branch_source_repository() {
        assert_eq!(SOURCE_REPO_URL, "https://github.com/AlextheYounga/bonesdeploy.git");
        assert_eq!(SOURCE_BRANCH, "master");
    }

    /// Extracts the package version from the `[package]` section of a Cargo manifest.
    #[test]
    fn parses_package_version_from_manifest_package_section() -> anyhow::Result<()> {
        let manifest = r#"
[package]
name = "bonesdeploy"
version = "0.2.8"
edition = "2024"

[dependencies]
version = "not-this"
"#;

        assert_eq!(parse_package_version(manifest)?, "0.2.8");
        Ok(())
    }

    /// Returns an error when the manifest has no `[package]` section with a version field.
    #[test]
    fn rejects_manifest_without_package_version() {
        let result = parse_package_version("[dependencies]\nversion = \"0.2.8\"\n");
        assert!(result.is_err());
    }

    /// Refreshes .bones scaffold assets from the cloned source tree without overwriting local config files.
    #[test]
    fn refresh_local_bones_updates_scaffold_without_touching_configs() -> Result<()> {
        let temp = TempDir::new()?;
        let source_dir = temp.path().join("source");
        let bones_dir = temp.path().join(".bones");

        write(&source_dir.join("crates/bonesdeploy/kit/hooks/pre-push"), "new hook")?;
        write(&source_dir.join("crates/bonesdeploy/kit/deployment/01_build.sh"), "generic deploy")?;
        write(&source_dir.join("crates/bonesdeploy/runtimes/laravel/deployment/01_build.sh"), "laravel deploy")?;

        write(&bones_dir.join("bones.toml"), "keep = 'config'\n")?;
        write(&bones_dir.join("runtime.toml"), "template = 'laravel'\n")?;

        refresh_local_bones_from_source(&source_dir, &bones_dir)?;

        assert_eq!(fs::read_to_string(bones_dir.join("bones.toml"))?, "keep = 'config'\n");
        assert_eq!(fs::read_to_string(bones_dir.join("runtime.toml"))?, "template = 'laravel'\n");
        assert_eq!(fs::read_to_string(bones_dir.join("hooks/pre-push"))?, "new hook");
        assert_eq!(fs::read_to_string(bones_dir.join("deployment/01_build.sh"))?, "laravel deploy");

        let hook_mode = fs::metadata(bones_dir.join("hooks/pre-push"))?.permissions().mode() & 0o777;
        let deploy_mode = fs::metadata(bones_dir.join("deployment/01_build.sh"))?.permissions().mode() & 0o777;
        assert_eq!(hook_mode, 0o755);
        assert_eq!(deploy_mode, 0o755);

        Ok(())
    }

    fn write(path: &Path, content: &str) -> Result<()> {
        if let Some(parent) = path.parent() {
            fs::create_dir_all(parent)?;
        }
        fs::write(path, content)?;
        Ok(())
    }
}

```

`crates/bonesdeploy/src/commands/update_release.rs`:

```rs
use std::path::Path;
use std::process::Command;

use anyhow::{Context, Result, bail};
use shared::paths;

use crate::config;
use crate::infra::ssh;
use shared::config::{default_deploy_user, parse_port};

pub fn current_local_version() -> String {
    env!("CARGO_PKG_VERSION").to_string()
}

pub fn current_remote_version() -> String {
    let bones_toml = Path::new(paths::LOCAL_BONES_TOML);
    if !bones_toml.exists() {
        return String::from("unknown");
    }

    let Ok(cfg) = config::load(bones_toml) else {
        return String::from("unknown");
    };

    let host = format!("{}@{}", default_deploy_user(), cfg.host);
    let output = Command::new("ssh").args(["-p", &cfg.port]).args([&host, "bonesremote", "version"]).output();

    match output {
        Ok(output) if output.status.success() => {
            String::from_utf8_lossy(&output.stdout).trim().strip_prefix("bonesremote ").unwrap_or("unknown").to_string()
        }
        _ => String::from("unknown"),
    }
}

pub fn update_local_from_source(repo_url: &str) -> Result<()> {
    let status = Command::new("cargo")
        .args(["install", "--git", repo_url, paths::BONESDEPLOY_BINARY, "--force"])
        .status()
        .context("Failed to run cargo install for bonesdeploy")?;

    if !status.success() {
        bail!("Failed to install bonesdeploy from {repo_url}");
    }

    Ok(())
}

pub async fn update_remote_from_source(repo_url: &str, _version: &str) -> Result<()> {
    let bones_toml = Path::new(paths::LOCAL_BONES_TOML);
    if !bones_toml.exists() {
        bail!("No .bones/bones.toml found. Run from a bonesdeploy project directory.");
    }

    let cfg = config::load(bones_toml)?;
    let port = parse_port(&cfg.port)?;
    let session = ssh::connect_as("root", &cfg.host, port).await?;

    let install_root = paths::USR_LOCAL_BIN.trim_end_matches("/bin");
    println!("Building bonesremote from source on remote...");
    ssh::stream_cmd(&session, &format!("cargo install --git {repo_url} bonesremote --force --root {install_root}"))
        .await?;

    ssh::stream_cmd(
        &session,
        &format!(
            "mkdir -p {root} && chown root:root {root} && chmod 711 {root}",
            root = paths::DEFAULT_PROJECT_ROOT_PARENT
        ),
    )
    .await?;

    session.close().await?;

    Ok(())
}

```

`crates/bonesdeploy/src/commands/version.rs`:

```rs
pub fn run() {
    println!("bonesdeploy {}", env!("CARGO_PKG_VERSION"));
}

```

`crates/bonesdeploy/src/config.rs`:

```rs
use std::env;
use std::fs;
use std::path::{Path, PathBuf};

use anyhow::{Context, Result};
use serde_json::{Map, Value};
use shared::config as shared_config;
use shared::paths;

pub use shared::config::{Bones, load};

pub fn is_configured(config: &Bones) -> bool {
    !config.remote_name.is_empty()
        && !config.project_name.is_empty()
        && !config.host.is_empty()
        && !config.repo_path.is_empty()
}

pub fn default_project_root_for(project_name: &str) -> String {
    paths::default_project_root_for(project_name)
}

pub fn bones_config_dir(project_name: &str) -> PathBuf {
    paths::bones_config_root().join(format!("{project_name}.bones"))
}

pub fn repo_directory_name() -> Result<String> {
    let cwd = env::current_dir()?;
    Ok(cwd.file_name().map_or_else(|| String::from("project"), |n| n.to_string_lossy().to_string()))
}

pub fn save(config: &Bones, path: &Path) -> Result<()> {
    let mut to_serialize = config.clone();
    shared_config::apply_derived_defaults(&mut to_serialize);

    let toml_str = toml::to_string(&to_serialize).context("Failed to serialize bones config")?;
    fs::write(path, toml_str).with_context(|| format!("Failed to write {}", path.display()))?;
    Ok(())
}

pub fn save_runtime(runtime: &Map<String, Value>, path: &Path) -> Result<()> {
    let toml_str = toml::to_string(runtime).context("Failed to serialize runtime config")?;
    fs::write(path, toml_str).with_context(|| format!("Failed to write {}", path.display()))?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use std::env::temp_dir;
    use std::fs;
    use std::path::{Path, PathBuf};
    use std::process;
    use std::time::{SystemTime, UNIX_EPOCH};

    use anyhow::Result;
    use shared::paths;

    use super::{Bones, default_project_root_for, save};
    use shared::config::load;

    fn temp_path(file_name: &str) -> PathBuf {
        let nanos = SystemTime::now().duration_since(UNIX_EPOCH).map_or(0, |duration| duration.as_nanos());
        temp_dir().join(format!("bonesdeploy_config_test_{}_{}_{}", process::id(), nanos, file_name))
    }

    fn minimal_toml(project_name: &str) -> String {
        format!(
            "remote_name = \"production\"\nproject_name = \"{project_name}\"\nhost = \"deploy.example.com\"\nport = \"22\"\nrepo_path = \"{}\"\nbranch = \"master\"\ndeploy_on_push = true\n",
            paths::default_repo_path_for(project_name)
        )
    }

    fn sample_config(project_name: &str) -> Bones {
        Bones {
            remote_name: String::from("production"),
            project_name: String::from(project_name),
            host: String::from("deploy.example.com"),
            port: String::from("22"),
            repo_path: paths::default_repo_path_for(project_name),
            project_root: default_project_root_for(project_name),
            branch: String::from("master"),
            deploy_on_push: true,
            ..Default::default()
        }
    }

    #[test]
    fn load_applies_default_repo_path_from_project_name() -> Result<()> {
        let path = temp_path("repo_path.toml");
        fs::write(&path, minimal_toml("atlas"))?;

        let cfg = load(&path)?;
        assert_eq!(cfg.repo_path, paths::default_repo_path_for("atlas"));

        fs::remove_file(path)?;
        Ok(())
    }

    #[test]
    fn load_applies_default_project_root_from_project_name() -> Result<()> {
        let path = temp_path("project_root.toml");
        fs::write(&path, minimal_toml("atlas"))?;

        let cfg = load(&path)?;
        assert_eq!(cfg.project_root, paths::default_project_root_for("atlas"));

        fs::remove_file(path)?;
        Ok(())
    }

    #[test]
    fn save_includes_derived_repo_and_project_root() -> Result<()> {
        let config = sample_config("phoenix");
        let path = temp_path("save_derived_defaults.toml");

        save(&config, &path)?;
        let content = fs::read_to_string(&path)?;

        assert!(content.contains("repo_path ="), "save should include repo_path");
        assert!(content.contains("project_root ="), "save should include project_root");

        fs::remove_file(path)?;
        Ok(())
    }

    #[test]
    fn save_persists_ssl_settings() -> Result<()> {
        let mut config = sample_config("phoenix");
        config.ssl_enabled = true;
        config.domain = String::from("app.example.com");
        config.email = String::from("ops@example.com");

        let path = temp_path("save_ssl_settings.toml");
        save(&config, &path)?;
        let content = fs::read_to_string(&path)?;

        assert!(content.contains("ssl_enabled = true"));
        assert!(content.contains("domain = \"app.example.com\""));
        assert!(content.contains("email = \"ops@example.com\""));

        fs::remove_file(path)?;
        Ok(())
    }

    #[test]
    fn load_preserves_explicit_repo_and_project_root_overrides() -> Result<()> {
        let path = temp_path("overrides.toml");
        let toml = format!(
            "remote_name = \"production\"\nproject_name = \"app\"\nhost = \"deploy.example.com\"\nport = \"22\"\nrepo_path = \"{}\"\nproject_root = \"/custom/deploy\"\nbranch = \"master\"\ndeploy_on_push = false\n",
            paths::default_repo_path_for("app")
        );

        fs::write(&path, toml)?;
        let cfg = load(Path::new(&path))?;

        assert_eq!(cfg.repo_path, paths::default_repo_path_for("app"));
        assert_eq!(cfg.project_root, "/custom/deploy");

        fs::remove_file(path)?;
        Ok(())
    }
}

```

`crates/bonesdeploy/src/infra/bonesinfra.rs`:

```rs
use std::fs;
use std::path::{Path, PathBuf};
use std::process::Command;

use anyhow::{Context, Result, bail};
use shared::paths;

const REPOSITORY_URL: &str = "https://github.com/AlextheYounga/bonesinfra.git";
const CHECKOUT_DIR: &str = "bonesinfra";

pub fn prefetch() -> Result<()> {
    ensure_available().map(|_| ())
}

pub(super) fn executable_path() -> Result<PathBuf> {
    ensure_available()
}

fn ensure_available() -> Result<PathBuf> {
    let checkout = checkout_dir();
    let venv_python = checkout.join(".venv").join("bin").join("python");

    if let Ok(metadata) = fs::symlink_metadata(&checkout) {
        if !metadata.file_type().is_dir() {
            reset_checkout(&checkout)?;
        }
    }

    if !checkout.is_dir() {
        install_checkout(&checkout)?;
    }

    setup_venv(&checkout)?;

    if venv_python.is_file() {
        return Ok(venv_python);
    }

    let contents: Vec<_> = fs::read_dir(&checkout)
        .into_iter()
        .flatten()
        .filter_map(Result::ok)
        .map(|e| e.path().display().to_string())
        .collect();
    if contents.is_empty() {
        bail!("bonesinfra setup finished but checkout is empty at {}.", checkout.display());
    }

    bail!(
        "bonesinfra setup finished at {}, but {} is missing.\nContents of checkout:\n  {}",
        checkout.display(),
        venv_python.display(),
        contents.join("\n  ")
    );
}

fn reset_checkout(checkout: &Path) -> Result<()> {
    let metadata = fs::symlink_metadata(checkout)
        .with_context(|| format!("Failed to inspect stale bonesinfra checkout at {}", checkout.display()))?;

    if metadata.file_type().is_dir() {
        fs::remove_dir_all(checkout)
            .with_context(|| format!("Failed to remove stale bonesinfra checkout at {}", checkout.display()))?;
        return Ok(());
    }

    fs::remove_file(checkout)
        .with_context(|| format!("Failed to remove stale bonesinfra checkout at {}", checkout.display()))?;
    Ok(())
}

fn install_checkout(checkout: &Path) -> Result<()> {
    if let Some(parent) = checkout.parent() {
        fs::create_dir_all(parent).with_context(|| format!("Failed to create {}", parent.display()))?;
    }

    let status = Command::new("git")
        .args(["clone", "--depth", "1", REPOSITORY_URL, &checkout.to_string_lossy()])
        .status()
        .context("Failed to run git clone for bonesinfra install")?;

    if !status.success() {
        bail!("Failed to install bonesinfra from {} into {}.", REPOSITORY_URL, checkout.display());
    }

    Ok(())
}

fn setup_venv(checkout: &Path) -> Result<()> {
    let venv_python = checkout.join(".venv").join("bin").join("python");

    if !venv_python.is_file() {
        let status = Command::new("python3")
            .args(["-m", "venv", ".venv"])
            .current_dir(checkout)
            .status()
            .with_context(|| format!("Failed to create venv in {}", checkout.display()))?;

        if !status.success() {
            bail!("Failed to create venv in {}.", checkout.display());
        }
    }

    let status = Command::new(&venv_python)
        .args(["-m", "pip", "install", "--upgrade", "pip"])
        .status()
        .with_context(|| format!("Failed to upgrade pip in {}", checkout.display()))?;

    if !status.success() {
        bail!("Failed to upgrade pip in {}.", checkout.display());
    }

    let status = Command::new(&venv_python)
        .args(["-m", "pip", "install", "-e", "."])
        .current_dir(checkout)
        .status()
        .with_context(|| format!("Failed to install bonesinfra dependencies in {}", checkout.display()))?;

    if !status.success() {
        bail!("Failed to install bonesinfra dependencies in {}.", checkout.display());
    }

    Ok(())
}

fn checkout_dir() -> PathBuf {
    paths::bones_config_root().join(CHECKOUT_DIR)
}

#[cfg(test)]
mod tests {
    use std::fs;

    use anyhow::Result;
    use shared::paths;
    use tempfile::TempDir;

    use super::{checkout_dir, reset_checkout};

    #[test]
    fn checkout_dir_lives_under_bones_config_root() {
        assert_eq!(checkout_dir(), paths::bones_config_root().join("bonesinfra"));
    }

    #[test]
    fn reset_checkout_removes_stale_directory() -> Result<()> {
        let temp_dir = TempDir::new()?;
        let checkout = temp_dir.path().join("bonesinfra");
        fs::create_dir_all(checkout.join("nested"))?;

        reset_checkout(&checkout)?;

        assert!(!checkout.exists());
        Ok(())
    }

    #[test]
    fn reset_checkout_removes_stale_file() -> Result<()> {
        let temp_dir = TempDir::new()?;
        let checkout = temp_dir.path().join("bonesinfra");
        fs::write(&checkout, "stale")?;

        reset_checkout(&checkout)?;

        assert!(!checkout.exists());
        Ok(())
    }

}

```

`crates/bonesdeploy/src/infra/bonesinfra_cli.rs`:

```rs
use std::io::Write;
use std::path::Path;
use std::process::{Command, Stdio};

use anyhow::{Context, Result, bail};
use serde_json::Value;

pub fn run(args: &[&str]) -> Result<String> {
    let executable = super::bonesinfra::executable_path()?;

    run_interactive(&executable, args, None)
}

pub fn run_with_stdin(args: &[&str], stdin_json: &str) -> Result<String> {
    let executable = super::bonesinfra::executable_path()?;

    run_interactive(&executable, args, Some(stdin_json))
}
pub fn run_json(args: &[&str]) -> Result<Value> {
    let executable = super::bonesinfra::executable_path()?;
    let stdout = run_captured(&executable, args)?;
    parse_json_output(&stdout)
}

fn parse_json_output(stdout: &str) -> Result<Value> {
    serde_json::from_str(stdout).context("Failed to parse JSON output from bonesinfra")
}

fn base_command(executable: &Path) -> Command {
    let mut cmd = Command::new(executable);
    cmd.args(["-m", "bonesinfra"]);
    cmd
}

fn run_interactive(executable: &Path, args: &[&str], stdin_json: Option<&str>) -> Result<String> {
    let mut command = base_command(executable);
    command.args(args);
    if stdin_json.is_some() {
        command.stdin(Stdio::piped());
    }

    let mut child = command
        .spawn()
        .with_context(|| format!("Failed to run bonesinfra {} from {}", args.join(" "), executable.display()))?;

    if let Some(stdin_json) = stdin_json {
        let mut stdin = child.stdin.take().context("Failed to capture bonesinfra stdin")?;
        stdin.write_all(stdin_json.as_bytes()).context("Failed to write JSON data to bonesinfra stdin")?;
    }

    let status = child
        .wait()
        .with_context(|| format!("Failed to wait on bonesinfra {} from {}", args.join(" "), executable.display()))?;

    if !status.success() {
        bail!("bonesinfra failed");
    }

    Ok(String::new())
}

fn run_captured(executable: &Path, args: &[&str]) -> Result<String> {
    let output = base_command(executable)
        .args(args)
        .output()
        .with_context(|| format!("Failed to run bonesinfra {} from {}", args.join(" "), executable.display()))?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        bail!("bonesinfra failed:\n{}", stderr.trim());
    }

    Ok(String::from_utf8_lossy(&output.stdout).to_string())
}

/// Returns the questions for a given runtime from bonesinfra.
pub fn runtime_questions(runtime: &str) -> Result<Value> {
    run_json(&["runtime", "questions", runtime])
}

#[cfg(test)]
mod tests {
    use std::path::Path;

    use anyhow::Result;

    use super::{base_command, parse_json_output};

    #[test]
    fn base_command_launches_venv_python_with_module_flag() {
        let command = base_command(Path::new("/tmp/bonesinfra/.venv/bin/python"));

        assert_eq!(command.get_program().to_string_lossy(), "/tmp/bonesinfra/.venv/bin/python");
        let args: Vec<_> = command.get_args().map(|a| a.to_string_lossy().to_string()).collect();
        assert_eq!(args, vec!["-m", "bonesinfra"]);
    }

    #[test]
    fn parse_json_output_reads_cli_stdout() -> Result<()> {
        let parsed = parse_json_output("[\"django\",\"rails\"]")?;
        assert_eq!(parsed, serde_json::json!(["django", "rails"]));
        Ok(())
    }
}

```

`crates/bonesdeploy/src/infra/bootstrap_ssh.rs`:

```rs
use std::env;

pub(crate) fn resolve(config_ssh_user: Option<&str>) -> String {
    // env override takes highest precedence
    if let Ok(env_user) = env::var("BONES_BOOTSTRAP_SSH_USER") {
        let trimmed = env_user.trim().to_string();
        if !trimmed.is_empty() {
            return trimmed;
        }
    }
    resolve_from(config_ssh_user)
}

fn resolve_from(value: Option<&str>) -> String {
    value
        .and_then(|raw| {
            let trimmed = raw.trim().to_string();
            if trimmed.is_empty() { None } else { Some(trimmed) }
        })
        .unwrap_or_else(|| String::from("root"))
}

#[cfg(test)]
mod tests {
    use super::resolve_from;

    #[test]
    fn defaults_to_root() {
        let user = resolve_from(None);
        assert_eq!(user, "root");
    }

    #[test]
    fn uses_config_value() {
        let user = resolve_from(Some("ubuntu"));
        assert_eq!(user, "ubuntu");
    }

    #[test]
    fn trims_and_rejects_blank_values() {
        let user = resolve_from(Some("   "));
        assert_eq!(user, "root");

        let user = resolve_from(Some("  ubuntu  "));
        assert_eq!(user, "ubuntu");
    }
}

```

`crates/bonesdeploy/src/infra/embedded.rs`:

```rs
use std::collections::BTreeSet;
use std::fs;
use std::os::unix::fs::PermissionsExt;
use std::path::Path;

use anyhow::{Context, Result, anyhow, bail};
use rust_embed::Embed;
use serde_json::{Map, Value};

use shared::paths;

#[derive(Embed)]
#[folder = "./kit/"]
struct Kit;

#[derive(Embed)]
#[folder = "./runtimes/"]
struct RuntimeAssets;

pub fn scaffold(bones_dir: &Path) -> Result<()> {
    for file_path in Kit::iter() {
        let Some(asset) = Kit::get(&file_path) else {
            continue;
        };
        write_asset(bones_dir, file_path.as_ref(), asset.data.as_ref())?;
    }

    Ok(())
}

pub fn runtime_names() -> Vec<String> {
    RuntimeAssets::iter()
        .filter_map(|path| path.split('/').next().map(str::to_string))
        .collect::<BTreeSet<_>>()
        .into_iter()
        .collect()
}

pub fn base_runtime_defaults() -> Result<Map<String, Value>> {
    runtime_defaults_from_bytes("kit/runtime.toml", Kit::get("runtime.toml").map(|asset| asset.data))
}

pub fn runtime_defaults(runtime: &str) -> Result<Map<String, Value>> {
    let asset_path = format!("{runtime}/runtime.toml");
    runtime_defaults_from_bytes(&asset_path, RuntimeAssets::get(&asset_path).map(|asset| asset.data))
}

pub fn scaffold_runtime_deployment(runtime: &str, bones_dir: &Path) -> Result<()> {
    let runtime_prefix = format!("{runtime}/");

    for file_path in RuntimeAssets::iter() {
        let Some(stripped) = file_path.strip_prefix(&runtime_prefix) else {
            continue;
        };

        if !stripped.starts_with(paths::KIT_DEPLOYMENT_DIR) {
            continue;
        }

        let Some(asset) = RuntimeAssets::get(&file_path) else {
            continue;
        };

        write_asset(bones_dir, stripped, asset.data.as_ref())?;
    }

    Ok(())
}

fn runtime_defaults_from_bytes(asset_path: &str, bytes: Option<impl AsRef<[u8]>>) -> Result<Map<String, Value>> {
    let Some(bytes) = bytes else {
        bail!("Missing embedded runtime defaults at {asset_path}");
    };

    let content = std::str::from_utf8(bytes.as_ref())
        .with_context(|| format!("Embedded asset {asset_path} is not valid UTF-8"))?;
    let toml_value: toml::Value = toml::from_str(content)
        .with_context(|| format!("Failed to parse embedded runtime defaults at {asset_path}"))?;
    let json_value = serde_json::to_value(toml_value)
        .with_context(|| format!("Failed to convert embedded runtime defaults at {asset_path} to JSON"))?;

    json_value
        .as_object()
        .cloned()
        .ok_or_else(|| anyhow!("Embedded runtime defaults at {asset_path} are not a TOML table"))
}

fn write_asset(bones_dir: &Path, relative_path: &str, bytes: &[u8]) -> Result<()> {
    let dest = bones_dir.join(relative_path);

    if let Some(parent) = dest.parent() {
        fs::create_dir_all(parent).with_context(|| format!("Failed to create {}", parent.display()))?;
    }

    fs::write(&dest, bytes).with_context(|| format!("Failed to write {}", dest.display()))?;

    if relative_path.starts_with(paths::KIT_HOOKS_DIR) || relative_path.starts_with(paths::KIT_DEPLOYMENT_DIR) {
        fs::set_permissions(&dest, fs::Permissions::from_mode(0o755))
            .with_context(|| format!("Failed to set permissions on {}", dest.display()))?;
    }

    Ok(())
}

#[cfg(test)]
mod tests {
    use std::fs;

    use anyhow::Result;
    use tempfile::TempDir;

    use super::{base_runtime_defaults, runtime_defaults, runtime_names, scaffold_runtime_deployment};
    use serde_json::Value;

    #[test]
    fn runtime_names_come_from_embedded_assets() {
        let runtimes = runtime_names();

        assert!(runtimes.contains(&String::from("laravel")));
        assert!(runtimes.contains(&String::from("next")));
    }

    #[test]
    fn runtime_defaults_read_local_runtime_toml() -> Result<()> {
        let defaults = runtime_defaults("laravel")?;

        assert_eq!(defaults.get("template"), Some(&Value::String(String::from("laravel"))));
        assert_eq!(defaults.get("php_version"), Some(&Value::String(String::from("8.5"))));
        Ok(())
    }

    #[test]
    fn base_runtime_defaults_read_embedded_kit_runtime() -> Result<()> {
        let defaults = base_runtime_defaults()?;

        assert!(defaults.contains_key("permissions"));
        assert!(defaults.contains_key("shared"));
        Ok(())
    }

    #[test]
    fn scaffold_runtime_deployment_writes_runtime_scripts() -> Result<()> {
        let temp = TempDir::new()?;

        scaffold_runtime_deployment("laravel", temp.path())?;

        let script = temp.path().join("deployment/02_run_build.sh");
        let content = fs::read_to_string(script)?;
        assert!(content.contains("composer install"));
        Ok(())
    }
}

```

`crates/bonesdeploy/src/infra/git.rs`:

```rs
use std::path::Path;
use std::process::Command;

use anyhow::{Context, Result, bail};

#[derive(Debug, Clone)]
pub struct RemoteConnectionDetails {
    pub user: String,
    pub host: String,
    pub port: String,
    pub repo_path: String,
}

#[derive(Debug, Clone)]
pub struct RemoteInfo {
    pub name: String,
    pub url: String,
}

pub fn ensure_git_repository() -> Result<()> {
    let output =
        Command::new("git").args(["rev-parse", "--is-inside-work-tree"]).output().context("Failed to run git")?;

    if !output.status.success() {
        bail!("Not a git repository");
    }

    Ok(())
}

pub fn remote_exists(remote_name: &str) -> Result<bool> {
    let output = Command::new("git").args(["remote", "get-url", remote_name]).output().context("Failed to run git")?;
    Ok(output.status.success())
}

pub fn add_remote(remote_name: &str, remote_url: &str) -> Result<()> {
    let status = Command::new("git")
        .args(["remote", "add", remote_name, remote_url])
        .status()
        .with_context(|| format!("Failed to add git remote '{remote_name}'"))?;

    if !status.success() {
        bail!("Failed to add git remote '{remote_name}'");
    }

    Ok(())
}

pub fn list_remotes() -> Result<Vec<String>> {
    let output = Command::new("git").args(["remote"]).output().context("Failed to run git")?;

    if !output.status.success() {
        bail!("Failed to list git remotes");
    }

    let remotes = String::from_utf8_lossy(&output.stdout)
        .lines()
        .map(str::trim)
        .filter(|name| !name.is_empty())
        .map(ToOwned::to_owned)
        .collect::<Vec<_>>();

    Ok(remotes)
}

pub fn list_remotes_with_urls() -> Result<Vec<RemoteInfo>> {
    let output = Command::new("git").args(["remote", "-v"]).output().context("Failed to run git")?;

    if !output.status.success() {
        bail!("Failed to list git remotes");
    }

    let mut remotes = Vec::new();
    for line in String::from_utf8_lossy(&output.stdout).lines() {
        let mut parts = line.split_whitespace();
        let Some(name) = parts.next() else {
            continue;
        };
        let Some(url) = parts.next() else {
            continue;
        };
        let Some(kind) = parts.next() else {
            continue;
        };
        if kind != "(fetch)" {
            continue;
        }
        remotes.push(RemoteInfo { name: name.to_string(), url: url.to_string() });
    }

    Ok(remotes)
}

pub fn remote_url(remote_name: &str) -> Result<String> {
    let output = Command::new("git")
        .args(["remote", "get-url", remote_name])
        .output()
        .with_context(|| format!("Failed to read URL for remote '{remote_name}'"))?;

    if !output.status.success() {
        bail!("Failed to read URL for remote '{remote_name}'");
    }

    let url = String::from_utf8_lossy(&output.stdout).trim().to_string();
    if url.is_empty() {
        bail!("Git remote '{remote_name}' has an empty URL");
    }

    Ok(url)
}

pub fn infer_remote_connection_details(remote_name: &str) -> Result<Option<RemoteConnectionDetails>> {
    let url = remote_url(remote_name)?;
    Ok(parse_remote_url(&url))
}

fn parse_remote_url(url: &str) -> Option<RemoteConnectionDetails> {
    parse_ssh_style_url(url.trim()).or_else(|| parse_scp_style_url(url.trim()))
}

fn parse_ssh_style_url(url: &str) -> Option<RemoteConnectionDetails> {
    if !url.starts_with("ssh://") {
        return None;
    }

    let without_scheme = &url[6..];
    let slash_index = without_scheme.find('/')?;
    let authority = without_scheme[..slash_index].trim();
    let path = without_scheme[slash_index..].trim();

    let host_port = authority.rsplit_once('@').map_or(authority, |(_, host)| host);
    let (host, port) = match host_port.split_once(':') {
        Some((host, port)) if !host.trim().is_empty() && !port.trim().is_empty() => {
            (host.trim().to_string(), port.trim().to_string())
        }
        _ => (host_port.trim().to_string(), String::from("22")),
    };

    if host.is_empty() || !has_git_extension(path) {
        return None;
    }

    Some(RemoteConnectionDetails { user: parse_user(authority), host, port, repo_path: path.to_string() })
}

fn parse_scp_style_url(url: &str) -> Option<RemoteConnectionDetails> {
    if url.contains("://") {
        return None;
    }

    let (left, right) = url.split_once(':')?;
    let host = left.rsplit_once('@').map_or(left, |(_, host)| host).trim();
    let repo_path = right.trim();
    if !repo_path.starts_with('/') {
        return None;
    }
    let repo_path = repo_path.to_string();

    if host.is_empty() || !has_git_extension(&repo_path) {
        return None;
    }

    Some(RemoteConnectionDetails {
        user: parse_user(left),
        host: host.to_string(),
        port: String::from("22"),
        repo_path,
    })
}

fn parse_user(authority: &str) -> String {
    authority.rsplit_once('@').map_or_else(|| String::from("git"), |(user, _)| user.to_string())
}

fn has_git_extension(path: &str) -> bool {
    Path::new(path).extension().is_some_and(|ext| ext.eq_ignore_ascii_case("git"))
}

#[cfg(test)]
mod tests {
    use shared::paths;

    use super::{parse_remote_url, parse_scp_style_url, parse_ssh_style_url};

    fn repo_path(name: &str) -> String {
        paths::default_repo_path_for(name)
    }

    #[test]
    fn parse_ssh_style_url_parses_host_port_and_repo_path() {
        let details = parse_ssh_style_url(&format!("ssh://git@example.com:2222{}", repo_path("myapp")));
        assert!(details.is_some());
        if let Some(details) = details {
            assert_eq!(details.user, "git");
            assert_eq!(details.host, "example.com");
            assert_eq!(details.port, "2222");
            assert_eq!(details.repo_path, repo_path("myapp"));
        }
    }

    #[test]
    fn parse_ssh_style_url_defaults_port_to_22() {
        let details = parse_ssh_style_url(&format!("ssh://git@example.com{}", repo_path("myapp")));
        assert!(details.is_some());
        if let Some(details) = details {
            assert_eq!(details.user, "git");
            assert_eq!(details.host, "example.com");
            assert_eq!(details.port, "22");
            assert_eq!(details.repo_path, repo_path("myapp"));
        }
    }

    #[test]
    fn parse_scp_style_url_parses_absolute_repo_path() {
        let details = parse_scp_style_url(&format!("git@example.com:{}", repo_path("myapp")));
        assert!(details.is_some());
        if let Some(details) = details {
            assert_eq!(details.user, "git");
            assert_eq!(details.host, "example.com");
            assert_eq!(details.port, "22");
            assert_eq!(details.repo_path, repo_path("myapp"));
        }
    }

    #[test]
    fn parse_scp_style_url_trims_surrounding_whitespace() {
        let details = parse_scp_style_url("git@example.com : /home/git/myapp.git");
        assert!(details.is_some());
        if let Some(details) = details {
            assert_eq!(details.user, "git");
            assert_eq!(details.host, "example.com");
            assert_eq!(details.port, "22");
            assert_eq!(details.repo_path, "/home/git/myapp.git");
        }
    }

    #[test]
    fn parse_remote_url_rejects_non_git_paths() {
        let non_git_path = repo_path("myapp").trim_end_matches(".git").to_string();
        assert!(parse_remote_url(&format!("ssh://git@example.com:22{non_git_path}")).is_none());
        assert!(parse_remote_url(&format!("git@example.com:{non_git_path}")).is_none());
    }

    #[test]
    fn parse_remote_url_rejects_relative_scp_paths() {
        assert!(parse_remote_url("git@example.com:myapp.git").is_none());
    }

    #[test]
    fn parse_remote_url_rejects_non_ssh_urls() {
        assert!(parse_remote_url("https://example.com/org/repo.git").is_none());
    }
}

```

`crates/bonesdeploy/src/infra/mod.rs`:

```rs
pub mod bonesinfra;
pub mod bonesinfra_cli;
pub mod bootstrap_ssh;
pub mod embedded;
pub mod git;
pub mod rsync;
pub mod ssh;

```

`crates/bonesdeploy/src/infra/rsync.rs`:

```rs
use std::process::{Command, ExitStatus, Output};

use anyhow::{Context, Result};

pub fn output(args: &[&str]) -> Result<Output> {
    Command::new("rsync").args(args).output().context("Failed to run rsync — is it installed?")
}

pub fn status(args: &[&str]) -> Result<ExitStatus> {
    Ok(output(args)?.status)
}

```

`crates/bonesdeploy/src/infra/ssh.rs`:

```rs
use anyhow::{Context, Result, bail};
use openssh::{KnownHosts, Session, SessionBuilder, Stdio};
use tokio::io::{AsyncBufReadExt, BufReader};

use crate::config::Bones;
use shared::config::{default_deploy_user, parse_port};

pub async fn connect(config: &Bones) -> Result<Session> {
    let host = &config.host;
    let port = parse_port(&config.port)?;
    let user = default_deploy_user();

    connect_as(&user, host, port).await
}

pub async fn connect_as(user: &str, host: &str, port: u16) -> Result<Session> {
    SessionBuilder::default()
        .known_hosts_check(KnownHosts::Accept)
        .user(user.into())
        .port(port)
        .connect(host)
        .await
        .with_context(|| format!("Failed to connect to {user}@{host}:{port}"))
}

pub async fn run_cmd(session: &Session, cmd: &str) -> Result<String> {
    let output = session
        .command("bash")
        .arg("-c")
        .arg(cmd)
        .output()
        .await
        .with_context(|| format!("Failed to execute remote command: {cmd}"))?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        bail!("Remote command failed: {cmd}\n{stderr}");
    }

    Ok(String::from_utf8_lossy(&output.stdout).to_string())
}

pub async fn stream_cmd(session: &Session, cmd: &str) -> Result<()> {
    let mut child = session
        .command("bash")
        .arg("-c")
        .arg(cmd)
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .await
        .with_context(|| format!("Failed to execute remote command: {cmd}"))?;

    let stdout = child.stdout().take().ok_or_else(|| anyhow::anyhow!("stdout was not piped"))?;
    let stderr = child.stderr().take().ok_or_else(|| anyhow::anyhow!("stderr was not piped"))?;

    let stdout_task = tokio::spawn(async move {
        let reader = BufReader::new(stdout);
        let mut lines = reader.lines();
        while let Ok(Some(line)) = lines.next_line().await {
            println!("{line}");
        }
    });

    let stderr_task = tokio::spawn(async move {
        let reader = BufReader::new(stderr);
        let mut lines = reader.lines();
        while let Ok(Some(line)) = lines.next_line().await {
            eprintln!("{line}");
        }
    });

    // Drain both streams concurrently before checking exit status
    let _ = tokio::join!(stdout_task, stderr_task);

    let status = child.wait().await.context("Failed to wait for remote command")?;

    if !status.success() {
        bail!("Remote command failed: {cmd}");
    }

    Ok(())
}

```

`crates/bonesdeploy/src/main.rs`:

```rs
mod cli;
mod commands;
mod config;

mod infra;

mod ui;

use anyhow::Result;
use clap::Parser;
use commands::Cli;

#[tokio::main]
async fn main() -> Result<()> {
    let cli = Cli::parse();
    commands::run(&cli).await
}

```

`crates/bonesdeploy/src/ui/mod.rs`:

```rs
pub mod prompts;

```

`crates/bonesdeploy/src/ui/prompts.rs`:

```rs
use anyhow::{Result, anyhow, bail};
use console::style;
use inquire::{Confirm, Select, Text};

use crate::config::Bones;
use crate::infra::git;

fn config_default<'a>(
    existing_config: Option<&'a Bones>,
    accessor: impl Fn(&'a Bones) -> &'a str,
    fallback: &'a str,
) -> &'a str {
    existing_config
        .and_then(|cfg| {
            let value = accessor(cfg);
            (!value.is_empty()).then_some(value)
        })
        .unwrap_or(fallback)
}

pub fn prompt_runtime_questions(
    questions: &serde_json::Value,
    defaults: &serde_json::Value,
) -> Result<serde_json::Value> {
    let mut answers = defaults.clone();
    let questions = questions.as_array().cloned().unwrap_or_default();

    for question in questions {
        let key = question["key"].as_str().unwrap_or("");
        if key.is_empty() {
            continue;
        }
        let label = question["label"].as_str().unwrap_or(key);
        let question_type = question["type"].as_str().unwrap_or("text");
        let default = answers.get(key).or(question.get("default")).cloned();

        let answer: serde_json::Value = match question_type {
            "bool" => {
                let default_bool = default.as_ref().and_then(serde_json::Value::as_bool).unwrap_or(false);
                let choice = Confirm::new(label).with_default(default_bool).prompt().map_err(|err| anyhow!(err))?;
                serde_json::Value::Bool(choice)
            }
            "choice" => {
                let choices: Vec<String> = question["choices"]
                    .as_array()
                    .map(|arr| arr.iter().filter_map(|v| v.as_str().map(String::from)).collect())
                    .unwrap_or_default();
                if choices.is_empty() {
                    default.unwrap_or(serde_json::Value::Null)
                } else {
                    let default_idx = default
                        .as_ref()
                        .and_then(|v| v.as_str())
                        .and_then(|d| choices.iter().position(|c| c == d))
                        .unwrap_or(0);
                    let choice = Select::new(label, choices.clone())
                        .with_starting_cursor(default_idx)
                        .prompt()
                        .map_err(|err| anyhow!(err))?;
                    serde_json::Value::String(choice)
                }
            }
            _ => {
                let default_str = default.as_ref().and_then(|v| v.as_str()).unwrap_or("");
                let input = Text::new(label).with_default(default_str).prompt().map_err(|err| anyhow!(err))?;
                serde_json::Value::String(input)
            }
        };
        answers[key] = answer;
    }

    Ok(answers)
}

pub fn choose_template(available_templates: &[String]) -> Result<Option<String>> {
    if available_templates.is_empty() {
        return Ok(None);
    }

    let choice = Select::new(
        "Would you like to use a template or build from scratch?",
        vec![String::from("Use a template"), String::from("Build from scratch")],
    )
    .with_help_message("Pick a stack to scaffold, or start from scratch")
    .prompt()?;

    if choice == "Build from scratch" {
        return Ok(None);
    }

    let template_name = Select::new("Which template stack would you like to use?", available_templates.to_vec())
        .with_help_message("Choose the framework stack to scaffold")
        .prompt()?;

    Ok(Some(template_name))
}

pub fn prompt_project_name(project_name_hint: &str, existing_config: Option<&Bones>) -> Result<String> {
    let default_project_name = config_default(existing_config, |cfg| cfg.project_name.as_str(), project_name_hint);
    Text::new("Project name:")
        .with_default(default_project_name)
        .prompt()
        .map(|value| value.trim().to_string())
        .map_err(|err| anyhow!(err))
}

pub fn prompt_branch(existing_config: Option<&Bones>) -> Result<String> {
    let default_branch = config_default(existing_config, |cfg| cfg.branch.as_str(), "main");
    Text::new("Branch:")
        .with_default(default_branch)
        .prompt()
        .map(|value| value.trim().to_string())
        .map_err(|err| anyhow!(err))
}

pub fn prompt_remote_name(existing_config: Option<&Bones>) -> Result<String> {
    const CREATE_REMOTE_OPTION: &str = "Create new deployment remote";

    let remotes = git::list_remotes_with_urls()?;
    if remotes.is_empty() {
        return prompt_remote_name_text(existing_config);
    }

    let default_remote = existing_config.and_then(|cfg| {
        let value = cfg.remote_name.as_str();
        (!value.is_empty()).then(|| cfg.remote_name.clone())
    });

    let preferred = default_remote.or_else(|| {
        let has_production = remotes.iter().any(|r| r.name == "production");
        if has_production { Some(String::from("production")) } else { None }
    });

    let mut ordered_remotes = Vec::with_capacity(remotes.len());
    if let Some(ref pref) = preferred
        && let Some(pos) = remotes.iter().position(|r| r.name == *pref)
    {
        ordered_remotes.push(remotes[pos].clone());
        ordered_remotes.extend(remotes.iter().enumerate().filter(|(i, _)| *i != pos).map(|(_, r)| r.clone()));
    }
    if ordered_remotes.is_empty() {
        ordered_remotes = remotes;
    }

    let mut display_options: Vec<String> = ordered_remotes.iter().map(remote_display_label).collect();
    display_options.push(String::from(CREATE_REMOTE_OPTION));

    let choice = Select::new("Deployment remote:", display_options)
        .with_help_message(
            "Choose the git remote that points to a fresh VPS for production deployment. Do not use 'origin' — that is your code host, not a deployment target.",
        )
        .raw_prompt()
        .map_err(|err| anyhow!(err))?;

    if choice.index == ordered_remotes.len() {
        return prompt_remote_name_text(existing_config);
    }

    let chosen = ordered_remotes[choice.index].name.clone();

    if chosen == "origin" {
        println!();
        println!("{}", style("WARNING:").yellow().bold());
        println!("You selected 'origin' as your deployment remote.");
        println!("'origin' typically points to your code host (e.g. GitHub, GitLab) — not to a VPS");
        println!("where bonesdeploy can deploy your application. Using it here will likely misconfigure");
        println!("deployment and push deployment infrastructure to the wrong place.");
        println!();
        let proceed = Confirm::new("Use 'origin' anyway?")
            .with_default(false)
            .with_help_message("Choose 'No' and create a new deployment remote instead")
            .prompt()
            .map_err(|err| anyhow!(err))?;
        if !proceed {
            bail!("Aborted: choose a remote that points to a fresh VPS, or create a new one.");
        }
    }

    Ok(chosen)
}

fn remote_display_label(remote: &git::RemoteInfo) -> String {
    if remote.name == "origin" {
        format!("{} ({}) — not a deployment remote", remote.name, remote.url)
    } else {
        format!("{} ({})", remote.name, remote.url)
    }
}

pub fn prompt_host(
    existing_config: Option<&Bones>,
    inferred_remote: Option<&git::RemoteConnectionDetails>,
) -> Result<String> {
    if let Some(details) = inferred_remote {
        return Ok(details.host.clone());
    }

    let default_host = config_default(existing_config, |cfg| cfg.host.as_str(), "");
    Text::new("Server host or IP:")
        .with_default(default_host)
        .with_help_message("e.g. deploy.example.com or 203.0.113.10")
        .prompt()
        .map(|value| value.trim().to_string())
        .map_err(|err| anyhow!(err))
}

pub fn prompt_port(
    existing_config: Option<&Bones>,
    inferred_remote: Option<&git::RemoteConnectionDetails>,
) -> Result<String> {
    if let Some(details) = inferred_remote {
        return Ok(details.port.clone());
    }

    let default_port = config_default(existing_config, |cfg| cfg.port.as_str(), "22");
    Text::new("SSH port:")
        .with_default(default_port)
        .prompt()
        .map(|value| value.trim().to_string())
        .map_err(|err| anyhow!(err))
}

pub fn confirm_remote_setup() -> Result<bool> {
    println!();
    for line in remote_setup_prompt_lines() {
        println!("{line}");
    }
    println!();
    Confirm::new("Set up the server now?").with_default(false).prompt().map_err(|err| anyhow!(err))
}

pub fn confirm_remote_runtime() -> Result<bool> {
    println!();
    for line in remote_runtime_prompt_lines() {
        println!("{line}");
    }
    println!();
    Confirm::new("Apply the runtime on the server now?").with_default(false).prompt().map_err(|err| anyhow!(err))
}

#[cfg(test)]
fn is_affirmative(answer: &str) -> bool {
    matches!(answer.trim().to_ascii_lowercase().as_str(), "y" | "yes")
}

fn remote_setup_prompt_lines() -> [&'static str; 12] {
    [
        "Remote setup",
        "This is intended for a fresh VPS, but is idempotent (can be run multiple times).",
        "You can use this to set up as many sites on your VPS as you would like. Run this once per site.",
        "",
        "This step will:",
        "  - Ensure necessary prerequisite packages are installed the server.",
        "  - Ensure correct user groups, roles, and firewalls are configured the server.",
        "  - Set up a git bare repo for this project on the server.",
        "  - Create the appropriate deployment and release directories for your project.",
        "  - Install the bonesremote binary on the server, used to facilitate deployments.",
        "",
        "For more information, check the local bonesinfra install managed by bonesdeploy.",
    ]
}

fn remote_runtime_prompt_lines() -> [&'static str; 9] {
    [
        "Remote runtime",
        "This applies per-site runtime configurations to the server.",
        "",
        "It will:",
        "  - Ensure runtime-specific packages are installed.",
        "  - Provision runtime-specific services, like PHP-FPM, Python, or Ruby, depending on your runtime template.",
        "  - Configure AppArmor, nginx, and systemd services are configured for this site.",
        "",
        "For more information, check the local bonesinfra install managed by bonesdeploy.",
    ]
}

pub fn confirm_remote_ssl() -> Result<bool> {
    println!();
    for line in remote_ssl_prompt_lines() {
        println!("{line}");
    }
    println!();
    Confirm::new("Set up HTTPS now?").with_default(false).prompt().map_err(|err| anyhow!(err))
}

fn remote_ssl_prompt_lines() -> [&'static str; 5] {
    [
        "Remote SSL setup",
        "This applies per-site SSL configurations to allow HTTPS traffic to your site.",
        "Before beginning this step, please ensure you have set up the appropriate A or CNAME DNS record on your DNS provider which points to this server.",
        "Common DNS providers are Namecheap, GoDaddy, Cloudflare, etc.",
        "If you have not completed this step, certificate creation will fail on this step.",
    ]
}

fn prompt_remote_name_text(existing_config: Option<&Bones>) -> Result<String> {
    let default_remote =
        existing_config.map(|cfg| cfg.remote_name.as_str()).filter(|value| !value.is_empty()).unwrap_or("production");
    Text::new("Deployment remote name:")
        .with_default(default_remote)
        .with_help_message("bonesdeploy will add this local git remote if it does not exist")
        .prompt()
        .map(|value| value.trim().to_string())
        .map_err(|err| anyhow!(err))
}

pub fn prompt_ssl_domain(existing_config: Option<&Bones>) -> Result<String> {
    let default_domain = config_default(existing_config, |cfg| cfg.domain.as_str(), "");
    Text::new("SSL domain:")
        .with_default(default_domain)
        .with_help_message("e.g. app.example.com")
        .prompt()
        .map(|value| value.trim().to_string())
        .map_err(|err| anyhow!(err))
}

pub fn prompt_ssl_email(existing_config: Option<&Bones>) -> Result<String> {
    let default_email = config_default(existing_config, |cfg| cfg.email.as_str(), "");
    Text::new("SSL email:")
        .with_default(default_email)
        .with_help_message("e.g. ops@example.com")
        .prompt()
        .map(|value| value.trim().to_string())
        .map_err(|err| anyhow!(err))
}

#[cfg(test)]
mod tests {
    use super::{is_affirmative, remote_runtime_prompt_lines, remote_setup_prompt_lines};

    /// Accepts common yes values like y, yes, and YES.
    #[test]
    fn confirmation_parser_accepts_common_yes_values() {
        assert!(is_affirmative("y"));
        assert!(is_affirmative(" yes "));
        assert!(is_affirmative("YES"));
    }

    /// Rejects non-affirmative values like empty string, n, and no.
    #[test]
    fn confirmation_parser_rejects_non_affirmative_values() {
        assert!(!is_affirmative(""));
        assert!(!is_affirmative("n"));
        assert!(!is_affirmative("no"));
    }

    /// Describes firewall configuration in the remote setup prompt.
    #[test]
    fn remote_setup_prompt_lines_include_firewall_configuration() {
        let joined = remote_setup_prompt_lines().join("\n");

        assert!(joined.contains("firewalls"), "remote setup prompt should describe firewall configuration\n{joined}");
    }

    /// Describes `AppArmor` and nginx in the remote runtime prompt.
    #[test]
    fn remote_runtime_prompt_lines_include_site_runtime_concerns() {
        let joined = remote_runtime_prompt_lines().join("\n");

        assert!(joined.contains("AppArmor") || joined.contains("nginx"));
    }
}

```

`crates/bonesremote/Cargo.toml`:

```toml
[package]
name = "bonesremote"
version = "0.4.2"
edition = "2024"


[dependencies]
anyhow = "1.0.102"
clap = { version = "4.6.1", features = ["derive"] }
console = "0.16.3"
nix = { version = "0.31.2", features = ["user"] }
serde = { version = "1.0.228", features = ["derive"] }
toml = "0.8"
time = { version = "0.3.47", features = ["formatting", "macros"] }
walkdir = "2.5.0"
shared = { path = "../shared" }

[lints.clippy]
# broad groups (lower priority so individual lint overrides take effect)
correctness = { level = "deny", priority = -1 }
suspicious = { level = "deny", priority = -1 }
complexity = { level = "warn", priority = -1 }
style = { level = "warn", priority = -1 }
perf = { level = "warn", priority = -1 }
pedantic = { level = "warn", priority = -1 }

# readability / naming
similar_names = "warn"
many_single_char_names = "warn"
module_name_repetitions = "warn"
enum_variant_names = "warn"
struct_field_names = "warn"
disallowed_names = "deny"
wildcard_imports = "warn"
module_inception = "warn"

# complexity / API readability
cognitive_complexity = "warn"
too_many_arguments = "deny"
fn_params_excessive_bools = "warn"
large_types_passed_by_value = "warn"
trivially_copy_pass_by_ref = "warn"

# panic / debug leftovers
unwrap_used = "deny"
expect_used = "deny"
panic = "deny"
todo = "deny"
unimplemented = "deny"
dbg_macro = "deny"
# This is a CLI binary: stdout/stderr output is the intended UX.
print_stdout = "allow"
print_stderr = "allow"

# docs / contracts
missing_panics_doc = "deny"
missing_errors_doc = "deny"
missing_safety_doc = "deny"
undocumented_unsafe_blocks = "deny"

# numeric safety
cast_possible_truncation = "warn"
cast_sign_loss = "warn"
cast_possible_wrap = "warn"
checked_conversions = "warn"

# anti-mess / consistency
absolute_paths = "warn"
allow_attributes = "deny"
redundant_clone = "warn"
implicit_clone = "warn"
semicolon_if_nothing_returned = "warn"
match_same_arms = "warn"
needless_pass_by_value = "warn"
cloned_instead_of_copied = "warn"
flat_map_option = "warn"
from_iter_instead_of_collect = "warn"
inefficient_to_string = "warn"
manual_let_else = "warn"
manual_ok_or = "warn"
map_unwrap_or = "warn"
unnecessary_wraps = "warn"

```

`crates/bonesremote/src/cli/args.rs`:

```rs
use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(name = "bonesremote", about = "Remote release deployment tool")]
pub struct Cli {
    #[command(subcommand)]
    pub command: Command,
}

#[derive(Subcommand)]
pub enum Command {
    /// Install sudoers drop-in for passwordless bonesremote
    Init,
    /// Check server environment health
    Doctor,
    /// Run the full remote deployment lifecycle
    Deploy {
        /// Path to bones.toml config file
        #[arg(long)]
        config: String,
        /// Exact revision to check out into the build workspace
        #[arg(long)]
        revision: Option<String>,
    },
    /// Release lifecycle operations
    Release {
        #[command(subcommand)]
        command: ReleaseCommand,
    },
    /// Narrow privileged service operations (requires root)
    Service {
        #[command(subcommand)]
        command: ServiceCommand,
    },
    /// Get a config value from a TOML file
    Config {
        /// Path to TOML config file
        #[arg(long)]
        file: String,
        /// Key to read
        key: String,
    },
    /// Print the version
    Version,
}

#[derive(Subcommand)]
pub enum ReleaseCommand {
    /// Stage a new release before checkout
    Stage {
        #[arg(long)]
        config: String,
    },
    /// Wire shared paths into the build workspace
    Wire {
        #[arg(long)]
        config: String,
    },
    /// Atomically activate staged release
    Activate {
        #[arg(long)]
        config: String,
    },
    /// Drop a failed staged release and clear state
    DropFailed {
        #[arg(long)]
        config: String,
    },
    /// Repoint current to the previous release
    Rollback {
        #[arg(long)]
        config: String,
    },
}

#[derive(Subcommand)]
pub enum ServiceCommand {
    /// Restart the per-site nginx service
    Restart {
        #[arg(long)]
        config: String,
    },
}

```

`crates/bonesremote/src/cli/dispatch.rs`:

```rs
use anyhow::Result;

use crate::cli::args::{Cli, Command, ReleaseCommand, ServiceCommand};
use crate::commands::{
    activate_release, config, deploy, doctor, drop_failed_release, init, rollback, service, stage_release, version,
    wire_release,
};

pub fn run(cli: &Cli) -> Result<()> {
    match &cli.command {
        Command::Init => init::run(),
        Command::Doctor => doctor::run(),
        Command::Deploy { config, revision } => deploy::run_full(config, revision.as_deref()),
        Command::Release { command } => match command {
            ReleaseCommand::Stage { config } => stage_release::run(config),
            ReleaseCommand::Wire { config } => wire_release::run(config),
            ReleaseCommand::Activate { config } => activate_release::run(config),
            ReleaseCommand::DropFailed { config } => drop_failed_release::run(config),
            ReleaseCommand::Rollback { config } => rollback::run(config),
        },
        Command::Service { command } => match command {
            ServiceCommand::Restart { config } => service::run(config),
        },
        Command::Config { file, key } => config::run(file, key),
        Command::Version => {
            version::run();
            Ok(())
        }
    }
}

```

`crates/bonesremote/src/cli/mod.rs`:

```rs
pub mod args;
pub mod dispatch;

```

`crates/bonesremote/src/commands/activate_release.rs`:

```rs
use std::path::Path;

use anyhow::{Result, bail};
use shared::paths;

use crate::config;
use crate::release_state;

pub fn run(config_path: &str) -> Result<()> {
    let cfg = config::load(Path::new(config_path))?;
    let release_name = release_state::read_staged_release(&cfg)?;
    let release_dir = release_state::release_dir(&cfg, &release_name);
    let current_link = std::path::PathBuf::from(cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).current);

    if !release_dir.exists() {
        anyhow::bail!("Staged release directory does not exist: {}", release_dir.display());
    }

    if current_link.exists() && !current_link.is_symlink() {
        bail!("current exists and is not a symlink: {}", current_link.display());
    }

    release_state::point_symlink_atomically(&current_link, &release_dir)?;

    release_state::clear_staged_release(&cfg)?;

    println!("Activated release: {release_name}");

    Ok(())
}

```

`crates/bonesremote/src/commands/config.rs`:

```rs
use std::fs;

use anyhow::{Context, Result, bail};

pub fn run(file: &str, key: &str) -> Result<()> {
    let content = fs::read_to_string(file).with_context(|| format!("Failed to read config file: {file}"))?;
    let value: toml::Value = toml::from_str(&content).with_context(|| format!("Failed to parse TOML: {file}"))?;

    let result = value.get(key);
    let Some(toml_value) = result else {
        bail!("Key '{key}' not found in {file}");
    };

    match toml_value {
        toml::Value::String(s) => print!("{s}"),
        toml::Value::Boolean(b) => print!("{b}"),
        toml::Value::Integer(i) => print!("{i}"),
        toml::Value::Float(f) => print!("{f}"),
        _ => bail!("Unsupported value type for key '{key}'"),
    }

    Ok(())
}

```

`crates/bonesremote/src/commands/deploy.rs`:

```rs
use std::fs;
use std::path::{Path, PathBuf};
use std::process::Command;

use anyhow::{Context, Result, bail};
use shared::config as shared_config;
use shared::paths;

use crate::config;
use crate::release_state;

#[path = "../release/scripts.rs"]
mod deploy_output;

use super::activate_release;
use super::doctor;
use super::drop_failed_release;
use super::post_deploy;
use super::post_receive;
use super::stage_release;
use super::wire_release;

pub fn run_full(config_path: &str, revision: Option<&str>) -> Result<()> {
    doctor::run()?;
    stage_release::run(config_path)?;

    let deploy_result = (|| {
        post_receive::run(config_path, revision)?;
        wire_release::run(config_path)?;
        run(config_path)?;
        restart_services(config_path)?;
        post_deploy::run(config_path)
    })();

    if let Err(error) = deploy_result {
        if let Err(cleanup_error) = drop_failed_release::run(config_path) {
            return Err(
                error.context(format!("Failed to clean up staged release after deployment failure: {cleanup_error}"))
            );
        }
        return Err(error);
    }

    Ok(())
}

pub fn run(config_path: &str) -> Result<()> {
    let cfg = config::load(Path::new(config_path))?;
    let release_name = release_state::read_staged_release(&cfg)?;
    let release_path = release_state::release_dir(&cfg, &release_name);
    let build_root = PathBuf::from(cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).build_root);
    let runtime = shared_config::load_runtime(Path::new(config_path).parent().unwrap_or_else(|| Path::new(".")))?;
    let deployment_paths = cfg.deployment_paths(&runtime.web_root);
    let deployment_dir = PathBuf::from(&deployment_paths.repo_deployment);

    if !release_path.exists() {
        bail!("Staged release directory does not exist: {}", release_path.display());
    }

    if !build_root.exists() {
        bail!("Build workspace does not exist: {}", build_root.display());
    }

    let scripts = list_deployment_scripts(&deployment_dir)?;
    if scripts.is_empty() {
        println!("No deployment scripts found. Skipping deploy scripts.");
    } else {
        for script in scripts {
            let script_name = script.file_name().and_then(|name| name.to_str()).unwrap_or("<unknown>");
            let log_path = deploy_output::deployment_log_path(&deployment_paths, &release_name, script_name);
            println!("Running {script_name}...");
            println!("Log: {}", log_path.display());

            let status = deploy_output::run_deployment_script(
                &script,
                &build_root,
                &log_path,
                &deploy_output::ScriptEnv {
                    project_name: &cfg.project_name,
                    project_root: &cfg.project_root,
                    repo_path: &cfg.repo_path,
                    web_root: &runtime.web_root,
                },
            )
            .with_context(|| format!("Failed to execute deployment script {}", script.display()))?;

            if !status.success() {
                println!("Deployment script {script_name} failed.");
                println!("Log: {}", log_path.display());
                bail!("Deployment script {script_name} failed with status {status}");
            }
        }

        println!("All deployment scripts completed.");
    }

    publish_release_tree(&build_root, &release_path)?;

    activate_release::run(config_path)
}

fn restart_services(config_path: &str) -> Result<()> {
    let status = Command::new("sudo")
        .arg(paths::BONESREMOTE_BINARY)
        .args(["service", "restart", "--config", config_path])
        .status()
        .context("Failed to restart site services")?;

    if !status.success() {
        bail!("Failed to restart site services: status {status}");
    }

    Ok(())
}

fn publish_release_tree(build_root: &Path, release_path: &Path) -> Result<()> {
    clear_directory(release_path)?;

    let copy_source = build_root.join(".");
    let status = Command::new("cp").arg("-a").arg(&copy_source).arg(release_path).status().with_context(|| {
        format!("Failed to copy build workspace {} to release tree {}", build_root.display(), release_path.display())
    })?;

    if !status.success() {
        bail!(
            "Failed to publish release tree from {} to {}: status {status}",
            build_root.display(),
            release_path.display()
        );
    }

    println!("Published release tree: {}", release_path.display());
    Ok(())
}

fn clear_directory(path: &Path) -> Result<()> {
    for entry in fs::read_dir(path).with_context(|| format!("Failed to read directory {}", path.display()))? {
        let entry = entry?;
        let entry_path = entry.path();
        let file_type = entry.file_type().with_context(|| format!("Failed to inspect {}", entry_path.display()))?;

        if file_type.is_dir() {
            fs::remove_dir_all(&entry_path)
                .with_context(|| format!("Failed to remove directory {}", entry_path.display()))?;
        } else {
            fs::remove_file(&entry_path).with_context(|| format!("Failed to remove {}", entry_path.display()))?;
        }
    }

    Ok(())
}

fn list_deployment_scripts(deployment_dir: &Path) -> Result<Vec<PathBuf>> {
    if !deployment_dir.is_dir() {
        return Ok(Vec::new());
    }

    let mut scripts = Vec::new();
    for entry in fs::read_dir(deployment_dir)
        .with_context(|| format!("Failed to read deployment directory {}", deployment_dir.display()))?
    {
        let entry = entry?;
        if entry.file_type()?.is_file() {
            scripts.push(entry.path());
        }
    }

    scripts.sort();
    Ok(scripts)
}

#[cfg(test)]
mod tests {
    use std::env;
    use std::fs;
    use std::path::{Path, PathBuf};
    use std::process;
    use std::time::{SystemTime, UNIX_EPOCH};

    use anyhow::{Result, anyhow};

    use super::{clear_directory, list_deployment_scripts, publish_release_tree};

    fn temp_dir(prefix: &str) -> Result<PathBuf> {
        let nanos = SystemTime::now().duration_since(UNIX_EPOCH).map_or(0_u128, |duration| duration.as_nanos());
        let path = env::temp_dir().join(format!("{prefix}_{}_{}", process::id(), nanos));
        fs::create_dir_all(&path)?;
        Ok(path)
    }

    fn write_file(path: &Path, content: &str) -> Result<()> {
        if let Some(parent) = path.parent() {
            fs::create_dir_all(parent)?;
        }
        fs::write(path, content)?;
        Ok(())
    }

    /// Removes all direct children of a directory without removing the directory itself.
    #[test]
    fn clear_directory_removes_all_direct_children() -> Result<()> {
        let root = temp_dir("bonesremote_deploy_clear")?;
        write_file(&root.join("file.txt"), "hello")?;
        write_file(&root.join("nested/inner.txt"), "world")?;

        clear_directory(&root)?;

        assert!(fs::read_dir(&root)?.next().is_none());

        fs::remove_dir_all(root).ok();
        Ok(())
    }

    /// Returns deployment script files sorted and excludes subdirectories.
    #[test]
    fn list_deployment_scripts_returns_sorted_files_only() -> Result<()> {
        let deployment_dir = temp_dir("bonesremote_deploy_scripts")?;
        write_file(&deployment_dir.join("20_restart.sh"), "#!/usr/bin/env bash\n")?;
        write_file(&deployment_dir.join("10_build.sh"), "#!/usr/bin/env bash\n")?;
        fs::create_dir_all(deployment_dir.join("ignored_dir"))?;

        let scripts = list_deployment_scripts(&deployment_dir)?;
        let script_names: Result<Vec<String>> = scripts
            .into_iter()
            .map(|path| {
                path.file_name()
                    .map(|name| name.to_string_lossy().to_string())
                    .ok_or_else(|| anyhow!("missing file name"))
            })
            .collect();

        assert_eq!(script_names?, vec!["10_build.sh", "20_restart.sh"]);

        fs::remove_dir_all(deployment_dir).ok();
        Ok(())
    }

    /// Replaces the release tree contents with a fresh copy from the build workspace.
    #[test]
    fn publish_release_tree_replaces_release_contents_with_build_workspace() -> Result<()> {
        let root = temp_dir("bonesremote_deploy_publish")?;
        let build_root = root.join("build_workspace");
        let release_root = root.join("release_tree");
        fs::create_dir_all(&build_root)?;
        fs::create_dir_all(&release_root)?;

        write_file(&build_root.join("public/index.html"), "<h1>ok</h1>")?;
        write_file(&build_root.join(".env.example"), "KEY=value")?;
        write_file(&release_root.join("stale.txt"), "old")?;

        publish_release_tree(&build_root, &release_root)?;

        assert!(!release_root.join("stale.txt").exists());
        assert_eq!(fs::read_to_string(release_root.join("public/index.html"))?, "<h1>ok</h1>");
        assert_eq!(fs::read_to_string(release_root.join(".env.example"))?, "KEY=value");

        fs::remove_dir_all(root).ok();
        Ok(())
    }
}

```

`crates/bonesremote/src/commands/doctor.rs`:

```rs
use std::collections::{HashMap, HashSet};
use std::fs;
use std::path::PathBuf;
use std::process::Command;

use anyhow::Result;
use console::style;
use shared::paths;

pub fn run() -> Result<()> {
    println!("{}", style(format!("{} doctor", paths::BONESREMOTE_BINARY)).bold());

    let mut issues: Vec<String> = Vec::new();

    check_supported_distribution(&mut issues);
    check_globally_available(&mut issues);
    check_passwordless_sudo(&mut issues);
    check_apparmor_support(&mut issues);

    if issues.is_empty() {
        println!("\n{} All checks passed.", style("OK").green().bold());
        Ok(())
    } else {
        println!();
        for issue in &issues {
            println!("  {} {issue}", style("!").red().bold());
        }
        anyhow::bail!("Doctor found {} issue{}", issues.len(), if issues.len() == 1 { "" } else { "s" });
    }
}

fn check_supported_distribution(issues: &mut Vec<String>) {
    let os_release = fs::read_to_string(paths::ETC_OS_RELEASE);
    let Ok(os_release) = os_release else {
        issues.push(format!("Failed to read {}; expected Debian or Ubuntu host", paths::ETC_OS_RELEASE));
        return;
    };

    let normalized = os_release.to_lowercase();
    if normalized.contains("id=debian") || normalized.contains("id=ubuntu") {
        return;
    }

    issues.push("Unsupported host OS; bonesremote currently supports Debian/Ubuntu only".to_string());
}

fn check_globally_available(issues: &mut Vec<String>) {
    let result = Command::new(paths::BONESREMOTE_BINARY).arg("version").output();

    match result {
        Ok(output) if output.status.success() => {}
        _ => issues.push(format!("{} is not globally available (not in PATH)", paths::BONESREMOTE_BINARY)),
    }
}

fn check_passwordless_sudo(issues: &mut Vec<String>) {
    let privileged_commands = [[paths::BONESREMOTE_BINARY, "service", "restart", "--config", "/nonexistent"]];

    for command in privileged_commands {
        let result = Command::new("sudo").arg("-n").arg("-l").args(command).output();

        match result {
            Ok(output) if output.status.success() => {}
            _ => issues.push(format!(
                "{} is not allowed via passwordless sudo: {} (run 'sudo {} init')",
                paths::BONESREMOTE_BINARY,
                command.join(" "),
                paths::BONESREMOTE_BINARY
            )),
        }
    }
}

fn check_apparmor_support(issues: &mut Vec<String>) {
    check_apparmor_kernel_enabled(issues);
    check_apparmor_service(issues);

    let Some(profile_names) = check_apparmor_profiles_installed(issues) else {
        return;
    };

    check_apparmor_unit_wiring(&profile_names, issues);
}

fn check_apparmor_kernel_enabled(issues: &mut Vec<String>) {
    let enabled_file = fs::read_to_string(paths::APPARMOR_ENABLED_PARAM);
    let Ok(enabled_value) = enabled_file else {
        issues.push(format!("AppArmor check failed: could not read {}", paths::APPARMOR_ENABLED_PARAM));
        return;
    };

    if !apparmor_kernel_enabled(&enabled_value) {
        issues.push("AppArmor check failed: kernel module is not enabled".to_string());
    }
}

fn check_apparmor_service(issues: &mut Vec<String>) {
    let status = Command::new("systemctl").args(["is-active", "apparmor"]).output();
    match status {
        Ok(output) if output.status.success() && String::from_utf8_lossy(&output.stdout).trim() == "active" => {}
        Ok(output) => {
            let service_status = String::from_utf8_lossy(&output.stdout).trim().to_string();
            issues.push(format!(
                "AppArmor check failed: apparmor service is not active (status: {})",
                if service_status.is_empty() { "unknown" } else { service_status.as_str() }
            ));
        }
        Err(error) => {
            issues.push(format!("AppArmor check failed: could not run systemctl is-active apparmor ({error})"));
        }
    }
}

fn check_apparmor_profiles_installed(issues: &mut Vec<String>) -> Option<Vec<String>> {
    let profiles = fs::read_dir(paths::ETC_APPARMOR_D);
    let Ok(profiles) = profiles else {
        issues.push(format!("AppArmor check failed: could not read {}", paths::ETC_APPARMOR_D));
        return None;
    };

    let profile_files: Vec<String> = profiles
        .filter_map(Result::ok)
        .filter_map(|entry| entry.file_name().into_string().ok())
        .filter(|name| apparmor_profile_filename(name))
        .collect();

    if profile_files.is_empty() {
        issues.push(format!(
            "AppArmor check failed: no bonesdeploy AppArmor profile found under {}",
            paths::ETC_APPARMOR_D
        ));
        return None;
    }

    Some(profile_files)
}

fn check_apparmor_unit_wiring(profile_names: &[String], issues: &mut Vec<String>) {
    let units = fs::read_dir(paths::ETC_SYSTEMD_SYSTEM);
    let Ok(units) = units else {
        issues.push(format!("AppArmor check failed: could not read {}", paths::ETC_SYSTEMD_SYSTEM));
        return;
    };

    let installed_profiles: HashSet<&str> = profile_names.iter().map(String::as_str).collect();
    let expected_unit_names: Vec<String> =
        profile_names.iter().filter_map(|profile_name| apparmor_unit_name_for_profile(profile_name)).collect();

    if expected_unit_names.is_empty() {
        issues.push("AppArmor check failed: no bonesdeploy AppArmor profile matched an expected unit name".to_string());
        return;
    }

    let unit_entries: HashMap<String, PathBuf> = units
        .filter_map(Result::ok)
        .filter_map(|entry| entry.file_name().into_string().ok().map(|name| (name, entry.path())))
        .collect();

    for expected_unit_name in expected_unit_names {
        let Some(path) = unit_entries.get(&expected_unit_name) else {
            issues.push(format!(
                "AppArmor check failed: expected {}/{} for installed bonesdeploy profile",
                paths::ETC_SYSTEMD_SYSTEM,
                expected_unit_name
            ));
            continue;
        };

        let contents = fs::read_to_string(path);

        match contents {
            Ok(contents) => match apparmor_unit_wiring_status(&contents, &installed_profiles) {
                AppArmorUnitWiringStatus::Ok => {}
                AppArmorUnitWiringStatus::MissingOrdering => {
                    issues.push(format!(
                        "AppArmor check failed: {} is missing apparmor.service ordering or dependency",
                        path.display()
                    ));
                }
                AppArmorUnitWiringStatus::MissingProfile => {
                    issues.push(format!("AppArmor check failed: {} is missing AppArmorProfile=", path.display()));
                }
                AppArmorUnitWiringStatus::UnknownProfile(profile_name) => {
                    issues.push(format!(
                        "AppArmor check failed: {} references unknown AppArmor profile {}",
                        path.display(),
                        profile_name
                    ));
                }
            },
            Err(error) => {
                issues.push(format!("AppArmor check failed: could not read {} ({error})", path.display()));
            }
        }
    }
}

fn apparmor_kernel_enabled(contents: &str) -> bool {
    matches!(contents.trim().to_ascii_lowercase().as_str(), "y" | "yes" | "1")
}

fn apparmor_profile_filename(name: &str) -> bool {
    name.starts_with("bonesdeploy-") && name.ends_with("-nginx")
}

fn apparmor_unit_name_for_profile(profile_name: &str) -> Option<String> {
    profile_name
        .strip_prefix("bonesdeploy-")
        .and_then(|name| name.strip_suffix("-nginx"))
        .map(|project_name| format!("{project_name}-nginx.service"))
}

fn systemd_directive_values<'a>(contents: &'a str, directive: &str) -> Vec<&'a str> {
    contents
        .lines()
        .filter_map(|line| line.strip_prefix(directive))
        .filter_map(|value| value.strip_prefix('='))
        .map(str::trim)
        .filter(|value| !value.is_empty())
        .collect()
}

fn systemd_directive_contains_token(contents: &str, directive: &str, token: &str) -> bool {
    systemd_directive_values(contents, directive)
        .into_iter()
        .flat_map(|value| value.split_ascii_whitespace())
        .any(|value| value == token)
}

fn apparmor_profile_binding(contents: &str) -> Option<&str> {
    systemd_directive_values(contents, "AppArmorProfile").into_iter().next()
}

enum AppArmorUnitWiringStatus {
    Ok,
    MissingOrdering,
    MissingProfile,
    UnknownProfile(String),
}

fn apparmor_unit_wiring_status(contents: &str, installed_profiles: &HashSet<&str>) -> AppArmorUnitWiringStatus {
    let has_apparmor_after = systemd_directive_contains_token(contents, "After", "apparmor.service");
    let has_apparmor_requires = systemd_directive_contains_token(contents, "Requires", "apparmor.service");

    if !has_apparmor_after || !has_apparmor_requires {
        return AppArmorUnitWiringStatus::MissingOrdering;
    }

    let Some(profile_name) = apparmor_profile_binding(contents) else {
        return AppArmorUnitWiringStatus::MissingProfile;
    };

    if installed_profiles.contains(profile_name) {
        AppArmorUnitWiringStatus::Ok
    } else {
        AppArmorUnitWiringStatus::UnknownProfile(profile_name.to_string())
    }
}

#[cfg(test)]
#[path = "tests/test_doctor.rs"]
mod test_doctor;

```

`crates/bonesremote/src/commands/drop_failed_release.rs`:

```rs
use std::fs;
use std::path::Path;

use anyhow::{Context, Result};

use crate::config;
use crate::release_state;

pub fn run(config_path: &str) -> Result<()> {
    let cfg = config::load(Path::new(config_path))?;
    let staged_path = release_state::staged_release_path(&cfg);

    if !staged_path.exists() {
        println!("No staged release state found. Nothing to clean.");
        return Ok(());
    }

    let release_name = release_state::read_staged_release(&cfg)?;
    let release_dir = release_state::release_dir(&cfg, &release_name);

    if release_dir.exists() {
        fs::remove_dir_all(&release_dir)
            .with_context(|| format!("Failed to remove failed release {}", release_dir.display()))?;
        println!("Removed failed release: {release_name}");
    }

    release_state::clear_staged_release(&cfg)?;
    println!("Cleared staged release state.");
    Ok(())
}

```

`crates/bonesremote/src/commands/init.rs`:

```rs
use std::fs;
use std::path::{Path, PathBuf};
use std::process::Command;

use anyhow::{Context, Result, bail};
use console::style;

use crate::privileges;
use shared::paths;

pub fn run() -> Result<()> {
    privileges::ensure_root("bonesremote init")?;

    println!("{}", style(format!("{} init", paths::BONESREMOTE_BINARY)).bold());

    let sudoers_path = paths::SUDOERS_PATH;
    let bonesdeploy_path = which_bonesdeploy_remote()?;

    // Only the commands that need ownership or live-state changes run via sudo.
    let sudoers_content = format!(
        "# Installed by bonesremote init\n\
             {} ALL=(root) NOPASSWD: {} service restart --config *\n",
        paths::DEPLOY_USER,
        bonesdeploy_path.display()
    );

    fs::write(sudoers_path, &sudoers_content).with_context(|| format!("Failed to write {sudoers_path}"))?;

    Command::new("chmod").args(["0440", sudoers_path]).status().context("Failed to chmod sudoers drop-in")?;

    let status = Command::new("visudo").args(["-c", "-f", sudoers_path]).status().context("Failed to run visudo")?;

    if !status.success() {
        fs::remove_file(sudoers_path).ok();
        bail!("visudo validation failed — sudoers drop-in removed for safety");
    }

    println!("{} Installed sudoers drop-in at {}", style("Done!").green().bold(), sudoers_path);

    Ok(())
}

fn which_bonesdeploy_remote() -> Result<PathBuf> {
    let output = Command::new("which")
        .arg(paths::BONESREMOTE_BINARY)
        .output()
        .context(format!("Failed to run 'which {}'", paths::BONESREMOTE_BINARY))?;

    if !output.status.success() {
        bail!(
            "{} is not in PATH. \
             Install it globally before running init.",
            paths::BONESREMOTE_BINARY
        );
    }

    let path = PathBuf::from(String::from_utf8_lossy(&output.stdout).trim().to_string());
    let path = fs::canonicalize(&path).with_context(|| format!("Failed to canonicalize {}", path.display()))?;
    if !approved_bonesdeploy_path(&path) {
        bail!("Refusing to write sudoers entry for {}: expected /usr/local/bin or /usr/bin", path.display());
    }

    Ok(path)
}

fn approved_bonesdeploy_path(path: &Path) -> bool {
    path.starts_with("/usr/local/bin") || path.starts_with("/usr/bin")
}

#[cfg(test)]
mod tests {
    use std::path::Path;

    use super::approved_bonesdeploy_path;

    #[test]
    fn approved_bonesdeploy_path_accepts_standard_bin_dirs() {
        assert!(approved_bonesdeploy_path(Path::new("/usr/local/bin/bonesremote")));
        assert!(approved_bonesdeploy_path(Path::new("/usr/bin/bonesremote")));
    }

    #[test]
    fn approved_bonesdeploy_path_rejects_unexpected_dirs() {
        assert!(!approved_bonesdeploy_path(Path::new("/home/alex/.local/bin/bonesremote")));
    }
}

```

`crates/bonesremote/src/commands/mod.rs`:

```rs
pub(crate) mod activate_release;
pub(crate) mod config;
pub(crate) mod deploy;
pub(crate) mod doctor;
pub(crate) mod drop_failed_release;
pub(crate) mod init;
pub(crate) mod post_deploy;
pub(crate) mod post_receive;
pub(crate) mod rollback;
pub(crate) mod service;
pub(crate) mod stage_release;
pub(crate) mod version;
pub(crate) mod wire_release;

pub use crate::cli::args::Cli;
pub use crate::cli::dispatch::run;

```

`crates/bonesremote/src/commands/post_deploy.rs`:

```rs
use std::fs;
use std::path::Path;

use anyhow::{Context, Result};

use crate::config;
use crate::release_state;

pub fn run(config_path: &str) -> Result<()> {
    let config_path = Path::new(config_path);
    let cfg = config::load(config_path)?;

    let pruned = prune_old_releases(&cfg)?;
    if !pruned.is_empty() {
        println!("Pruned releases: {}", pruned.join(", "));
    }

    Ok(())
}

fn prune_old_releases(cfg: &config::Bones) -> Result<Vec<String>> {
    let active_release = release_state::current_release_name(cfg)?;
    let mut releases = release_state::list_releases_sorted(cfg)?;
    let keep = cfg.releases_keep.max(1);

    let mut pruned = Vec::new();
    while releases.len() > keep {
        let oldest = releases.remove(0);
        if oldest == active_release {
            releases.push(oldest);
            releases.sort();
            continue;
        }

        let path = release_state::release_dir(cfg, &oldest);
        if path.exists() {
            fs::remove_dir_all(&path).with_context(|| format!("Failed to prune old release {}", path.display()))?;
            pruned.push(oldest);
        }
    }

    Ok(pruned)
}

#[cfg(test)]
mod tests {
    use std::env;
    use std::fs;
    use std::os::unix::fs::symlink;
    use std::path::{Path, PathBuf};
    use std::process;
    use std::time::{SystemTime, UNIX_EPOCH};

    use anyhow::Result;
    use shared::config::Bones;
    use shared::paths;

    use super::prune_old_releases;

    fn temp_dir(prefix: &str) -> Result<PathBuf> {
        let nanos = SystemTime::now().duration_since(UNIX_EPOCH).map_or(0_u128, |duration| duration.as_nanos());
        let path = env::temp_dir().join(format!("{prefix}_{}_{}", process::id(), nanos));
        fs::create_dir_all(&path)?;
        Ok(path)
    }

    fn config_for(temp_root: &Path, keep: usize) -> Bones {
        Bones {
            remote_name: String::from("production"),
            project_name: String::from("acme"),
            host: String::from("example.com"),
            port: String::from("22"),
            repo_path: temp_root.join("repo.git").to_string_lossy().to_string(),
            project_root: temp_root.join("project_root").to_string_lossy().to_string(),
            branch: String::from("main"),
            deploy_on_push: true,
            releases_keep: keep,
            ..Default::default()
        }
    }

    fn make_release(root: &Path, name: &str) -> Result<()> {
        fs::create_dir_all(root.join("project_root").join(paths::RELEASES_DIR).join(name))?;
        Ok(())
    }

    fn set_current_release(root: &Path, name: &str) -> Result<()> {
        let project_root = root.join("project_root");
        let releases = project_root.join(paths::RELEASES_DIR);
        fs::create_dir_all(&releases)?;
        let target = releases.join(name);
        symlink(&target, project_root.join(paths::CURRENT_LINK))?;
        Ok(())
    }

    /// Prunes the oldest inactive releases when the active release count exceeds the keep limit.
    #[test]
    fn prune_old_releases_removes_oldest_inactive_releases_up_to_keep_limit() -> Result<()> {
        let root = temp_dir("bonesremote_post_deploy_prune")?;
        let cfg = config_for(&root, 2);

        make_release(&root, "20260101_000000")?;
        make_release(&root, "20260102_000000")?;
        make_release(&root, "20260103_000000")?;
        set_current_release(&root, "20260103_000000")?;

        let pruned = prune_old_releases(&cfg)?;

        assert_eq!(pruned, vec!["20260101_000000"]);
        assert!(!root.join("project_root").join(paths::RELEASES_DIR).join("20260101_000000").exists());
        assert!(root.join("project_root").join(paths::RELEASES_DIR).join("20260102_000000").exists());
        assert!(root.join("project_root").join(paths::RELEASES_DIR).join("20260103_000000").exists());

        fs::remove_dir_all(root).ok();
        Ok(())
    }

    /// Keeps all releases when the active release count is within the keep limit.
    #[test]
    fn prune_old_releases_keeps_active_release_when_within_keep_limit() -> Result<()> {
        let root = temp_dir("bonesremote_post_deploy_prune_active")?;
        let cfg = config_for(&root, 2);

        make_release(&root, "20260101_000000")?;
        make_release(&root, "20260102_000000")?;
        set_current_release(&root, "20260101_000000")?;

        let pruned = prune_old_releases(&cfg)?;

        assert!(pruned.is_empty());
        assert!(root.join("project_root").join(paths::RELEASES_DIR).join("20260101_000000").exists());
        assert!(root.join("project_root").join(paths::RELEASES_DIR).join("20260102_000000").exists());

        fs::remove_dir_all(root).ok();
        Ok(())
    }
}

```

`crates/bonesremote/src/commands/post_receive.rs`:

```rs
use std::fs;
use std::io::ErrorKind;
use std::path::Path;
use std::process::Command;

use anyhow::{Context, Result, bail};
use shared::paths;

use crate::config;

pub fn run(config_path: &str, revision: Option<&str>) -> Result<()> {
    let cfg = config::load(Path::new(config_path))?;
    let build_root = std::path::PathBuf::from(cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).build_root);
    ensure_build_workspace_accessible(&build_root)?;

    let checkout_target = revision.unwrap_or(cfg.branch.as_str());
    println!("Checking out {checkout_target} to {}...", build_root.display());

    let status = Command::new("git")
        .arg("--work-tree")
        .arg(&build_root)
        .arg("--git-dir")
        .arg(&cfg.repo_path)
        .arg("checkout")
        .arg("-f")
        .arg(checkout_target)
        .status()
        .with_context(|| {
            format!("Failed to run git checkout for target '{checkout_target}' into {}", build_root.display())
        })?;

    if !status.success() {
        bail!("git checkout failed for target '{checkout_target}': status {status}");
    }

    Ok(())
}

fn ensure_build_workspace_accessible(build_root: &Path) -> Result<()> {
    match fs::metadata(build_root) {
        Ok(metadata) => {
            if metadata.is_dir() {
                Ok(())
            } else {
                bail!("Build workspace is not a directory: {}", build_root.display())
            }
        }
        Err(error) if error.kind() == ErrorKind::NotFound => {
            bail!("Build workspace does not exist: {}", build_root.display())
        }
        Err(error) if error.kind() == ErrorKind::PermissionDenied => {
            bail!("Build workspace is not accessible (permission denied): {}", build_root.display())
        }
        Err(error) => bail!("Failed to inspect build workspace {}: {error}", build_root.display()),
    }
}

#[cfg(test)]
mod tests {
    use std::env;
    use std::fs;
    use std::os::unix::fs::PermissionsExt;
    use std::path::{Path, PathBuf};
    use std::process;
    use std::process::Command;
    use std::time::{SystemTime, UNIX_EPOCH};

    use anyhow::Result;
    use shared::config::Bones;
    use shared::paths;

    use super::run;

    fn temp_dir_path(test_name: &str) -> PathBuf {
        let nanos = SystemTime::now().duration_since(UNIX_EPOCH).map_or(0, |duration| duration.as_nanos());
        env::temp_dir().join(format!("bonesremote_post_receive_test_{}_{}_{}", process::id(), nanos, test_name))
    }

    fn run_command(command: &mut Command, label: &str) -> Result<()> {
        let status = command.status()?;
        anyhow::ensure!(status.success(), "Command failed ({label}) with status {status}");
        Ok(())
    }

    fn write_config(path: &Path, repo_path: &Path, project_root: &Path, branch: &str) -> Result<()> {
        let cfg = Bones {
            remote_name: String::from("production"),
            project_name: String::from("postreceive"),
            host: String::from("localhost"),
            port: String::from("22"),
            repo_path: repo_path.to_string_lossy().to_string(),
            project_root: project_root.to_string_lossy().to_string(),
            branch: branch.to_string(),
            deploy_on_push: true,
            ..Default::default()
        };
        let toml = toml::to_string(&cfg)?;
        fs::write(path, toml)?;
        Ok(())
    }

    fn create_remote_with_master_commit(root: &Path) -> Result<PathBuf> {
        let bare = root.join("repo.git");
        let work = root.join("work");

        run_command(Command::new("git").args(["init", "--bare", bare.to_string_lossy().as_ref()]), "git init --bare")?;
        run_command(Command::new("git").args(["init", work.to_string_lossy().as_ref()]), "git init work")?;
        run_command(
            Command::new("git").args(["-C", work.to_string_lossy().as_ref(), "config", "user.name", "Unit Test"]),
            "git config user.name",
        )?;
        run_command(
            Command::new("git").args([
                "-C",
                work.to_string_lossy().as_ref(),
                "config",
                "user.email",
                "unit@test.local",
            ]),
            "git config user.email",
        )?;

        fs::write(work.join("README.md"), "hello\n")?;
        run_command(Command::new("git").args(["-C", work.to_string_lossy().as_ref(), "add", "."]), "git add")?;
        run_command(
            Command::new("git").args(["-C", work.to_string_lossy().as_ref(), "commit", "-m", "initial"]),
            "git commit",
        )?;
        run_command(
            Command::new("git").args([
                "-C",
                work.to_string_lossy().as_ref(),
                "remote",
                "add",
                "origin",
                bare.to_string_lossy().as_ref(),
            ]),
            "git remote add",
        )?;
        run_command(
            Command::new("git").args(["-C", work.to_string_lossy().as_ref(), "push", "origin", "HEAD:master"]),
            "git push master",
        )?;

        Ok(bare)
    }

    /// `post-receive` fails when the build workspace does not exist.
    #[test]
    fn post_receive_requires_existing_build_workspace() -> Result<()> {
        let root = temp_dir_path("build_workspace_missing");
        fs::create_dir_all(&root)?;

        let bare = create_remote_with_master_commit(&root)?;
        let project_root = root.join("deploy");
        let config_path = root.join("bones.toml");
        write_config(&config_path, &bare, &project_root, "master")?;

        let result = run(config_path.to_string_lossy().as_ref(), None);
        assert!(result.is_err());

        fs::remove_dir_all(root)?;
        Ok(())
    }

    /// `post-receive` checks out the requested revision into the staged build workspace.
    #[test]
    fn post_receive_checks_out_requested_revision_into_build_workspace() -> Result<()> {
        let root = temp_dir_path("checkout_revision");
        fs::create_dir_all(&root)?;

        let bare = create_remote_with_master_commit(&root)?;
        let project_root = root.join("deploy");
        let build_root = project_root.join(paths::BUILD_DIR).join(paths::WORKSPACE_DIR);
        fs::create_dir_all(&build_root)?;

        let config_path = root.join("bones.toml");
        write_config(&config_path, &bare, &project_root, "master")?;

        let config_path_str = config_path.to_string_lossy().to_string();
        let result = run(&config_path_str, Some("master"));

        // Post-receive is responsible for checkout; shared-path wiring happens in a separate command.
        assert!(result.is_ok());
        assert!(build_root.join("README.md").exists());

        fs::remove_dir_all(root)?;
        Ok(())
    }

    /// `post-receive` fails with a permission error when the build workspace is inaccessible.
    #[test]
    fn post_receive_reports_permission_denied_for_inaccessible_workspace() -> Result<()> {
        let root = temp_dir_path("workspace_permission_denied");
        fs::create_dir_all(&root)?;

        let bare = create_remote_with_master_commit(&root)?;
        let project_root = root.join("deploy");
        let build_dir = project_root.join(paths::BUILD_DIR);
        let build_root = build_dir.join(paths::WORKSPACE_DIR);
        fs::create_dir_all(&build_root)?;

        let config_path = root.join("bones.toml");
        write_config(&config_path, &bare, &project_root, "master")?;

        let mut perms = fs::metadata(&build_dir)?.permissions();
        perms.set_mode(0o000);
        fs::set_permissions(&build_dir, perms)?;

        let result = run(config_path.to_string_lossy().as_ref(), Some("master"));

        let mut restore = fs::metadata(&build_dir)?.permissions();
        restore.set_mode(0o755);
        fs::set_permissions(&build_dir, restore)?;

        let Err(error) = result else {
            anyhow::bail!("post-receive should fail when workspace path is inaccessible");
        };
        assert!(error.to_string().to_lowercase().contains("permission denied"));

        fs::remove_dir_all(root)?;
        Ok(())
    }
}

```

`crates/bonesremote/src/commands/rollback.rs`:

```rs
use std::path::Path;

use anyhow::{Context, Result, bail};
use shared::paths;

use crate::config;
use crate::release_state;

pub fn run(config_path: &str) -> Result<()> {
    let cfg = config::load(Path::new(config_path))?;
    let releases = release_state::list_releases_sorted(&cfg)?;
    if releases.len() < 2 {
        bail!("Need at least two releases to perform rollback");
    }

    let current_name = release_state::current_release_name(&cfg)?;
    let current_idx = releases
        .iter()
        .position(|name| name == &current_name)
        .with_context(|| format!("Current release '{current_name}' was not found in releases/"))?;

    if current_idx == 0 {
        bail!("Current release is already the oldest release; cannot roll back");
    }

    let previous_name = releases[current_idx - 1].clone();
    let previous_dir = release_state::release_dir(&cfg, &previous_name);
    let current_link = std::path::PathBuf::from(cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).current);
    release_state::point_symlink_atomically(&current_link, &previous_dir)?;

    println!("Rollback complete: {current_name} -> {previous_name}");
    Ok(())
}

```

`crates/bonesremote/src/commands/service.rs`:

```rs
use std::path::Path;
use std::process::Command;

use anyhow::{Context, Result, bail};

use crate::config;
use crate::privileges;

pub fn run(config_path: &str) -> Result<()> {
    privileges::ensure_root("bonesremote service restart")?;

    let cfg = config::load(Path::new(config_path))?;
    let site_name = &cfg.project_name;

    if !is_valid_site_name(site_name) {
        bail!(
            "invalid site name in config: {site_name}. Must be 1-32 chars, lowercase letters, digits, hyphens, underscores, starting with a letter or underscore."
        );
    }

    let service_name = format!("{site_name}-nginx");

    let status = Command::new("systemctl")
        .args(["restart", &service_name])
        .status()
        .context("Failed to restart nginx service")?;

    if !status.success() {
        bail!("Failed to restart {service_name} service");
    }
    println!("Restarted {service_name} service");

    Ok(())
}

fn is_valid_site_name(name: &str) -> bool {
    if name.is_empty() || name.len() > 32 {
        return false;
    }
    let mut chars = name.chars();
    match chars.next() {
        Some(c) if c.is_ascii_lowercase() || c == '_' => {}
        _ => return false,
    }
    chars.all(|c| c.is_ascii_lowercase() || c.is_ascii_digit() || c == '-' || c == '_')
}

```

`crates/bonesremote/src/commands/stage_release.rs`:

```rs
use std::fs;
use std::path::Path;

use anyhow::{Context, Result, bail};
use shared::paths;
use time::OffsetDateTime;
use time::format_description::FormatItem;
use time::macros::format_description;

use crate::config;
use crate::release_state;

pub fn run(config_path: &str) -> Result<()> {
    let cfg = config::load(Path::new(config_path))?;

    let project_root = Path::new(&cfg.project_root);
    let build_dir = project_root.join(paths::BUILD_DIR);
    let build_root = Path::new(&cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).build_root).to_path_buf();
    let releases_dir = release_state::releases_dir(&cfg);
    let shared_dir = Path::new(&cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).shared).to_path_buf();

    require_dir(project_root, "project_root")?;
    require_dir(&releases_dir, "releases")?;
    require_dir(&build_dir, "build")?;
    require_dir(&shared_dir, "shared")?;

    fs::create_dir_all(&build_root)
        .with_context(|| format!("Failed to create build workspace: {}", build_root.display()))?;

    let release_name = create_release_name()?;
    let staged_release_dir = release_state::release_dir(&cfg, &release_name);
    fs::create_dir_all(&staged_release_dir)
        .with_context(|| format!("Failed to create release dir: {}", staged_release_dir.display()))?;

    release_state::write_staged_release(&cfg, &release_name)?;

    println!("Staged release: {release_name}");
    Ok(())
}

fn require_dir(path: &Path, label: &str) -> Result<()> {
    if !path.is_dir() {
        bail!(
            "Site not provisioned: {} does not exist ({label}). Run 'bonesdeploy remote setup' first.",
            path.display()
        );
    }
    Ok(())
}

fn create_release_name() -> Result<String> {
    static TIMESTAMP_FORMAT: &[FormatItem<'static>] = format_description!("[year][month][day]_[hour][minute][second]");
    let now = OffsetDateTime::now_utc();
    now.format(TIMESTAMP_FORMAT).context("Failed to format release timestamp")
}

```

`crates/bonesremote/src/commands/tests/test_doctor.rs`:

```rs
use std::collections::HashSet;

use super::{
    AppArmorUnitWiringStatus, apparmor_kernel_enabled, apparmor_profile_binding, apparmor_profile_filename,
    apparmor_unit_name_for_profile, apparmor_unit_wiring_status,
};

/// Accepts a yes value as indicating `AppArmor` is enabled in the kernel.
#[test]
fn apparmor_kernel_enabled_accepts_yes() {
    assert!(apparmor_kernel_enabled("Y\n"));
}

/// Rejects a no value as indicating `AppArmor` is not enabled in the kernel.
#[test]
fn apparmor_kernel_enabled_rejects_no() {
    assert!(!apparmor_kernel_enabled("N\n"));
}

/// Accepts a valid bonesdeploy `AppArmor` profile filename.
#[test]
fn apparmor_profile_filename_accepts_bonesdeploy_profile() {
    assert!(apparmor_profile_filename("bonesdeploy-demo-nginx"));
}

/// Rejects a filename that does not match the bonesdeploy profile naming convention.
#[test]
fn apparmor_profile_filename_rejects_unrelated_file() {
    assert!(!apparmor_profile_filename("default"));
}

/// Maps a bonesdeploy `AppArmor` profile name to its corresponding systemd unit name.
#[test]
fn apparmor_unit_name_for_profile_maps_project_unit() {
    assert_eq!(apparmor_unit_name_for_profile("bonesdeploy-demo-nginx"), Some("demo-nginx.service".to_string()));
}

/// Accepts a systemd unit with correctly wired `AppArmor` dependency and profile.
#[test]
fn apparmor_unit_wiring_accepts_expected_unit_with_reordered_after_tokens() {
    let installed_profiles = HashSet::from(["bonesdeploy-demo-nginx"]);

    assert!(matches!(
        apparmor_unit_wiring_status(
            "[Unit]\nAfter=apparmor.service network.target\nRequires=apparmor.service\n[Service]\nAppArmorProfile=bonesdeploy-demo-nginx\n",
            &installed_profiles,
        ),
        AppArmorUnitWiringStatus::Ok
    ));
}

/// Rejects a systemd unit that is missing the `AppArmor` profile binding.
#[test]
fn apparmor_unit_wiring_rejects_missing_profile_binding() {
    let installed_profiles = HashSet::from(["bonesdeploy-demo-nginx"]);

    assert!(matches!(
        apparmor_unit_wiring_status(
            "[Unit]\nAfter=network.target apparmor.service\nRequires=apparmor.service\n[Service]\nType=simple\n",
            &installed_profiles,
        ),
        AppArmorUnitWiringStatus::MissingProfile
    ));
}

/// Rejects a systemd unit that binds an unknown `AppArmor` profile.
#[test]
fn apparmor_unit_wiring_rejects_unknown_profile_binding() {
    let installed_profiles = HashSet::from(["bonesdeploy-demo-nginx"]);

    assert!(matches!(
        apparmor_unit_wiring_status(
            "[Unit]\nAfter=network.target apparmor.service\nRequires=apparmor.service\n[Service]\nAppArmorProfile=bonesdeploy-demo-ngnix\n",
            &installed_profiles,
        ),
        AppArmorUnitWiringStatus::UnknownProfile(profile_name) if profile_name == "bonesdeploy-demo-ngnix"
    ));
}

/// Reads the first `AppArmor` profile assignment from a systemd unit file.
#[test]
fn apparmor_profile_binding_reads_first_profile_assignment() {
    assert_eq!(
        apparmor_profile_binding("[Service]\nAppArmorProfile=bonesdeploy-demo-nginx\n"),
        Some("bonesdeploy-demo-nginx")
    );
}

```

`crates/bonesremote/src/commands/version.rs`:

```rs
use shared::paths;

pub fn run() {
    println!("{} {}", paths::BONESREMOTE_BINARY, env!("CARGO_PKG_VERSION"));
}

```

`crates/bonesremote/src/commands/wire_release.rs`:

```rs
use std::fs;
use std::os::unix::fs::symlink;
use std::path::{Component, Path};

use anyhow::{Context, Result, bail};
use shared::config as shared_config;
use shared::paths;

use crate::config;
use crate::release_state;

use shared::config::Shared;

pub fn run(config_path: &str) -> Result<()> {
    let config_path = Path::new(config_path);
    let cfg = config::load(config_path)?;
    let release_name = release_state::read_staged_release(&cfg)?;
    let build_root = std::path::PathBuf::from(cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).build_root);
    let shared_dir = std::path::PathBuf::from(cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).shared);

    let config_dir = config_path.parent().unwrap_or(Path::new("."));
    let _runtime = shared_config::load_runtime(config_dir)?;
    let runtime_path = config_dir.join("runtime.toml");
    let shared_paths = if runtime_path.exists() {
        let content =
            fs::read_to_string(&runtime_path).with_context(|| format!("Failed to read {}", runtime_path.display()))?;
        let runtime: Shared =
            toml::from_str(&content).with_context(|| format!("Failed to parse {}", runtime_path.display()))?;
        runtime.paths
    } else {
        Vec::new()
    };
    for shared_path in &shared_paths {
        validate_shared_path(&shared_path.path)?;
        wire_path(&build_root, &shared_dir, &shared_path.path)?;
    }

    println!("Wired build workspace for staged release: {release_name}");
    Ok(())
}

fn validate_shared_path(relative_path: &str) -> Result<()> {
    if relative_path.is_empty() {
        bail!("shared path must not be empty");
    }
    for component in Path::new(relative_path).components() {
        match component {
            Component::Normal(_) => {}
            Component::CurDir => bail!("shared path must not contain ."),
            Component::ParentDir => bail!("shared path must not contain .., got: {relative_path}"),
            Component::RootDir | Component::Prefix(_) => {
                bail!("shared path must be relative, got: {relative_path}")
            }
        }
    }
    Ok(())
}

fn wire_path(build_root: &Path, shared_dir: &Path, relative_path: &str) -> Result<()> {
    let release_path = build_root.join(relative_path);
    let shared_path = shared_dir.join(relative_path);

    if fs::symlink_metadata(&shared_path).is_err() {
        bail!(
            "shared path does not exist: {}. Provision it first with 'bonesdeploy remote setup'.",
            shared_path.display()
        );
    }

    ensure_parent_exists(&release_path)?;
    if fs::symlink_metadata(&release_path).is_ok() {
        replace_workspace_path_with_shared_symlink(&release_path)?;
    }

    symlink(&shared_path, &release_path).with_context(|| {
        format!("Failed to create shared symlink {} -> {}", release_path.display(), shared_path.display())
    })?;

    println!("Linked shared path: {} -> {}", release_path.display(), shared_path.display());

    Ok(())
}

fn ensure_parent_exists(path: &Path) -> Result<()> {
    if let Some(parent) = path.parent() {
        fs::create_dir_all(parent)
            .with_context(|| format!("Failed to create parent directory: {}", parent.display()))?;
    }
    Ok(())
}

/// Removes whatever exists at the build workspace path (file, dir, or symlink) so
/// a shared-path symlink can replace it. Only safe to call against the disposable
/// build workspace — never against `current`, `releases/`, or `shared/`.
fn replace_workspace_path_with_shared_symlink(path: &Path) -> Result<()> {
    let metadata = fs::symlink_metadata(path)
        .with_context(|| format!("Failed to inspect path for removal: {}", path.display()))?;

    if metadata.file_type().is_symlink() || metadata.is_file() {
        fs::remove_file(path).with_context(|| format!("Failed to remove path: {}", path.display()))?;
    } else if metadata.is_dir() {
        fs::remove_dir_all(path).with_context(|| format!("Failed to remove directory: {}", path.display()))?;
    }

    Ok(())
}

#[cfg(test)]
mod tests {
    use std::env;
    use std::fs;
    use std::path::PathBuf;
    use std::process;
    use std::time::{SystemTime, UNIX_EPOCH};

    use anyhow::Result;

    use super::{replace_workspace_path_with_shared_symlink, validate_shared_path};

    fn temp_dir_path(test_name: &str) -> PathBuf {
        let nanos = SystemTime::now().duration_since(UNIX_EPOCH).map_or(0, |duration| duration.as_nanos());
        env::temp_dir().join(format!("bonesremote_wire_release_test_{}_{}_{}", process::id(), nanos, test_name))
    }

    /// Removes both files and directories, including nested contents, from the build workspace.
    #[test]
    fn replace_workspace_path_removes_files_and_directories() -> Result<()> {
        let root = temp_dir_path("replace_workspace_path");
        fs::create_dir_all(&root)?;

        let file_path = root.join("tmp.txt");
        fs::write(&file_path, "payload")?;
        replace_workspace_path_with_shared_symlink(&file_path)?;
        assert!(!file_path.exists());

        let dir_path = root.join("tmp_dir");
        fs::create_dir_all(dir_path.join("nested"))?;
        fs::write(dir_path.join("nested").join("file.txt"), "payload")?;
        replace_workspace_path_with_shared_symlink(&dir_path)?;
        assert!(!dir_path.exists());

        fs::remove_dir_all(root)?;
        Ok(())
    }

    /// Rejects empty, absolute, and parent-directory paths.
    /// Allows benign double-dots in filenames (e.g. "my..dir").
    #[test]
    fn validate_shared_path_rejects_unsafe_paths() {
        assert!(validate_shared_path("").is_err());
        assert!(validate_shared_path("/etc").is_err());
        assert!(validate_shared_path("./.env").is_err(), "explicit current-dir is rejected");
        assert!(validate_shared_path("../.env").is_err());
        assert!(validate_shared_path("storage/../.env").is_err());
        assert!(validate_shared_path("storage").is_ok());
        assert!(validate_shared_path("storage/logs").is_ok());
        assert!(validate_shared_path("my..dir").is_ok(), "double-dot filenames are allowed");
        assert!(validate_shared_path("assets..cache/file.txt").is_ok(), "double-dot directory names are allowed");
    }
}

```

`crates/bonesremote/src/config.rs`:

```rs
pub use shared::config::{Bones, load};

#[cfg(test)]
mod tests {
    use std::env;
    use std::fs;
    use std::path::PathBuf;
    use std::process;
    use std::time::{SystemTime, UNIX_EPOCH};

    use anyhow::Result;
    use shared::paths;

    use super::load;

    fn temp_file_path(prefix: &str) -> PathBuf {
        let nanos = SystemTime::now().duration_since(UNIX_EPOCH).map_or(0_u128, |duration| duration.as_nanos());
        env::temp_dir().join(format!("{prefix}_{}_{}.toml", process::id(), nanos))
    }

    #[test]
    fn load_derives_project_root_and_repo_path_from_project_name() -> Result<()> {
        let path = temp_file_path("bonesremote_config_derived_defaults");
        let toml = r#"
project_name = "acme"
host = "example.com"
"#;

        fs::write(&path, toml)?;
        let cfg = load(&path)?;
        fs::remove_file(&path).ok();

        assert_eq!(cfg.repo_path, paths::default_repo_path_for("acme"));
        assert_eq!(cfg.project_root, paths::default_project_root_for("acme"));
        Ok(())
    }

    #[test]
    fn load_preserves_explicit_repo_and_project_root() -> Result<()> {
        let path = temp_file_path("bonesremote_config_explicit_values");
        let toml = r#"
project_name = "acme"
repo_path = "/custom/repo.git"
project_root = "/custom/deploy"
"#;

        fs::write(&path, toml)?;
        let cfg = load(&path)?;
        fs::remove_file(&path).ok();

        assert_eq!(cfg.repo_path, "/custom/repo.git");
        assert_eq!(cfg.project_root, "/custom/deploy");
        Ok(())
    }

    #[test]
    fn load_uses_defaults_for_missing_fields() -> Result<()> {
        let path = temp_file_path("bonesremote_config_missing_fields");
        fs::write(&path, "")?;

        let cfg = load(&path)?;
        fs::remove_file(&path).ok();

        assert_eq!(cfg.port, "22");
        assert_eq!(cfg.branch, "master");
        assert_eq!(cfg.releases_keep, 5);
        Ok(())
    }

    #[test]
    fn load_fails_for_invalid_toml() -> Result<()> {
        let path = temp_file_path("bonesremote_config_invalid_toml");
        fs::write(&path, "[data\n")?;

        let result = load(&path);
        fs::remove_file(&path).ok();

        assert!(result.is_err());
        Ok(())
    }

    #[test]
    fn load_fails_for_missing_file() {
        let path = temp_file_path("bonesremote_config_missing_file");
        let result = load(&path);
        assert!(result.is_err());
    }
}

```

`crates/bonesremote/src/main.rs`:

```rs
mod cli;
mod commands;
mod config;
mod privileges;
mod release_state;

use anyhow::Result;
use clap::Parser;
use commands::Cli;

fn main() -> Result<()> {
    let cli = Cli::parse();
    commands::run(&cli)
}

```

`crates/bonesremote/src/privileges.rs`:

```rs
use anyhow::{Result, bail};
use nix::unistd::geteuid;

pub fn ensure_root(command_name: &str) -> Result<()> {
    if geteuid().is_root() {
        return Ok(());
    }

    bail!("{command_name} must be run as root (sudo)")
}

```

`crates/bonesremote/src/release/scripts.rs`:

```rs
use std::fs;
use std::io::{self, Read, Write};
use std::path::{Path, PathBuf};
use std::process::{Command, ExitStatus, Stdio};
use std::thread;

use anyhow::{Context, Result, bail};
use shared::paths::{self, Deployment};

pub(super) fn deployment_log_path(paths: &Deployment, release_name: &str, script_name: &str) -> PathBuf {
    Path::new(&paths.build_logs).join(format!("{release_name}-{script_name}.log"))
}

pub(super) struct ScriptEnv<'a> {
    pub(super) project_name: &'a str,
    pub(super) project_root: &'a str,
    pub(super) repo_path: &'a str,
    pub(super) web_root: &'a str,
}

pub(super) fn run_deployment_script(
    script: &Path,
    build_root: &Path,
    log_path: &Path,
    env: &ScriptEnv<'_>,
) -> Result<ExitStatus> {
    if let Some(parent) = log_path.parent() {
        fs::create_dir_all(parent).with_context(|| format!("Failed to create log directory {}", parent.display()))?;
    }

    let log_file = fs::OpenOptions::new()
        .create(true)
        .append(true)
        .open(log_path)
        .with_context(|| format!("Failed to open deployment log {}", log_path.display()))?;

    let mut child = Command::new("bash")
        .arg(script)
        .current_dir(build_root)
        .env("PROJECT_NAME", env.project_name)
        .env("PROJECT_ROOT", env.project_root)
        .env("REPO_PATH", env.repo_path)
        .env("WEB_ROOT", env.web_root)
        .env("SERVICE_USER", env.project_name)
        .env("DEPLOY_USER", paths::DEPLOY_USER)
        .env("GROUP", paths::DEFAULT_GROUP)
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .with_context(|| format!("Failed to execute deployment script {}", script.display()))?;

    let stdout = child.stdout.take().context("Failed to capture deployment script stdout")?;
    let stderr = child.stderr.take().context("Failed to capture deployment script stderr")?;

    let stdout_handle =
        spawn_stream(stdout, io::stdout(), log_file.try_clone().context("Failed to clone deployment log")?);
    let stderr_handle = spawn_stream(stderr, io::stderr(), log_file);

    let status = child.wait().with_context(|| format!("Failed to wait for deployment script {}", script.display()))?;

    join_stream(stdout_handle, "stdout")?;
    join_stream(stderr_handle, "stderr")?;

    Ok(status)
}

fn spawn_stream<R, W1, W2>(reader: R, primary: W1, secondary: W2) -> thread::JoinHandle<Result<()>>
where
    R: Read + Send + 'static,
    W1: Write + Send + 'static,
    W2: Write + Send + 'static,
{
    thread::spawn(move || {
        let mut reader = reader;
        let mut primary = primary;
        let mut secondary = secondary;
        let mut buffer = [0_u8; 8192];

        loop {
            let read = reader.read(&mut buffer)?;
            if read == 0 {
                break;
            }
            primary.write_all(&buffer[..read])?;
            secondary.write_all(&buffer[..read])?;
        }

        primary.flush()?;
        secondary.flush()?;
        Ok(())
    })
}

fn join_stream(handle: thread::JoinHandle<Result<()>>, stream_name: &str) -> Result<()> {
    match handle.join() {
        Ok(result) => result,
        Err(_) => bail!("Deployment output thread for {stream_name} panicked"),
    }
}

#[cfg(test)]
mod tests {
    use std::env;
    use std::fs;
    use std::path::{Path, PathBuf};
    use std::time::{SystemTime, UNIX_EPOCH};

    use anyhow::Result;
    use std::os::unix::prelude::PermissionsExt;

    use shared::paths::Deployment;

    use super::{ScriptEnv, deployment_log_path, run_deployment_script};

    fn temp_dir(prefix: &str) -> Result<PathBuf> {
        let nanos = SystemTime::now().duration_since(UNIX_EPOCH).map_or(0_u128, |duration| duration.as_nanos());
        let path = env::temp_dir().join(format!("{prefix}_{nanos}"));
        fs::create_dir_all(&path)?;
        Ok(path)
    }

    fn write_file(path: &Path, content: &str) -> Result<()> {
        if let Some(parent) = path.parent() {
            fs::create_dir_all(parent)?;
        }
        fs::write(path, content)?;
        Ok(())
    }

    #[test]
    fn run_deployment_script_streams_output_to_console_and_log() -> Result<()> {
        let root = temp_dir("bonesremote_deploy_runner_stream")?;
        let build_root = root.join("workspace");
        let logs = root.join("logs");
        fs::create_dir_all(&build_root)?;
        fs::create_dir_all(&logs)?;

        let script = root.join("00_hello.sh");
        write_file(&script, "#!/usr/bin/env bash\necho 'hello-stdout'\necho 'hello-stderr' >&2\n")?;
        fs::set_permissions(&script, PermissionsExt::from_mode(0o755))?;

        let log_path = logs.join("20260612_211412-00_hello.sh.log");
        let status = run_deployment_script(
            &script,
            &build_root,
            &log_path,
            &ScriptEnv {
                project_name: "demo",
                project_root: "/srv/deployments/demo",
                repo_path: "/home/git/demo.git",
                web_root: "public",
            },
        )?;

        assert!(status.success(), "passing script should exit zero");

        let log = fs::read_to_string(&log_path)?;
        assert!(log.contains("hello-stdout"), "log should contain stdout\n{log}");
        assert!(log.contains("hello-stderr"), "log should contain stderr\n{log}");

        fs::remove_dir_all(root).ok();
        Ok(())
    }

    #[test]
    fn run_deployment_script_preserves_failing_exit_status() -> Result<()> {
        let root = temp_dir("bonesremote_deploy_runner_failing")?;
        let build_root = root.join("workspace");
        let logs = root.join("logs");
        fs::create_dir_all(&build_root)?;
        fs::create_dir_all(&logs)?;

        let script = root.join("01_install.sh");
        write_file(&script, "#!/usr/bin/env bash\necho 'about to fail' >&2\nexit 7\n")?;
        fs::set_permissions(&script, PermissionsExt::from_mode(0o755))?;

        let log_path = logs.join("20260612_211412-01_install.sh.log");
        let status = run_deployment_script(
            &script,
            &build_root,
            &log_path,
            &ScriptEnv {
                project_name: "demo",
                project_root: "/srv/deployments/demo",
                repo_path: "/home/git/demo.git",
                web_root: "public",
            },
        )?;

        assert!(!status.success(), "failing script should exit non-zero");
        assert_eq!(status.code(), Some(7), "failing script should preserve exit code 7");
        let log = fs::read_to_string(&log_path)?;
        assert!(log.contains("about to fail"), "log should still be written for failing script\n{log}");

        fs::remove_dir_all(root).ok();
        Ok(())
    }

    #[test]
    fn run_deployment_script_creates_missing_log_directory() -> Result<()> {
        let root = temp_dir("bonesremote_deploy_runner_mkdir")?;
        let build_root = root.join("workspace");
        fs::create_dir_all(&build_root)?;

        let script = root.join("00_pass.sh");
        write_file(&script, "#!/usr/bin/env bash\necho ok\n")?;
        fs::set_permissions(&script, PermissionsExt::from_mode(0o755))?;

        let log_path = root.join("build/logs/20260612_211412-00_pass.sh.log");
        let status = run_deployment_script(
            &script,
            &build_root,
            &log_path,
            &ScriptEnv {
                project_name: "demo",
                project_root: "/srv/deployments/demo",
                repo_path: "/home/git/demo.git",
                web_root: "public",
            },
        )?;

        assert!(status.success());
        assert!(log_path.exists(), "log file should be created even when its directory is missing");
        assert!(fs::read_to_string(&log_path)?.contains("ok"));

        fs::remove_dir_all(root).ok();
        Ok(())
    }

    #[test]
    fn deployment_log_path_lives_under_build_logs() {
        let paths = Deployment::new("demo", "/home/git/demo.git", "/srv/deployments/demo", "public");
        let log = deployment_log_path(&paths, "20260612_211412", "02_run_build.sh");

        assert_eq!(
            log,
            PathBuf::from("/srv/deployments/demo/build/logs/20260612_211412-02_run_build.sh.log"),
            "log path should derive from centralized build_logs directory"
        );
    }
}

```

`crates/bonesremote/src/release_state.rs`:

```rs
use std::fs;
use std::os::unix::fs::symlink;
use std::path::{Path, PathBuf};
use std::process;
use std::time::{SystemTime, UNIX_EPOCH};

use anyhow::{Context, Result, bail};

use crate::config::Bones;
use shared::paths;

pub fn staged_release_path(cfg: &Bones) -> PathBuf {
    Path::new(&cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).repo_bones).join(paths::STAGED_RELEASE_FILE)
}

pub fn read_staged_release(cfg: &Bones) -> Result<String> {
    let path = staged_release_path(cfg);
    let value = fs::read_to_string(&path)
        .with_context(|| format!("Failed to read staged release state at {}", path.display()))?;
    let release = value.trim().to_string();

    if release.is_empty() {
        bail!("Staged release state file is empty: {}", path.display());
    }

    Ok(release)
}

pub fn write_staged_release(cfg: &Bones, release: &str) -> Result<()> {
    let path = staged_release_path(cfg);
    if let Some(parent) = path.parent() {
        fs::create_dir_all(parent)
            .with_context(|| format!("Failed to create staged release state dir: {}", parent.display()))?;
    }

    fs::write(&path, format!("{release}\n"))
        .with_context(|| format!("Failed to write staged release state: {}", path.display()))
}

pub fn clear_staged_release(cfg: &Bones) -> Result<()> {
    let path = staged_release_path(cfg);
    if path.exists() {
        fs::remove_file(&path).with_context(|| format!("Failed to remove staged release state: {}", path.display()))?;
    }
    Ok(())
}

pub fn release_dir(cfg: &Bones, release: &str) -> PathBuf {
    releases_dir(cfg).join(release)
}

pub fn releases_dir(cfg: &Bones) -> PathBuf {
    PathBuf::from(cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).releases)
}

pub fn current_release_dir(cfg: &Bones) -> Result<PathBuf> {
    let current_link = PathBuf::from(cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).current);
    let active_target =
        fs::read_link(&current_link).with_context(|| format!("Failed to read {}", current_link.display()))?;

    Ok(if active_target.is_absolute() {
        active_target
    } else {
        current_link.parent().unwrap_or_else(|| Path::new("/")).join(active_target)
    })
}

pub fn current_release_name(cfg: &Bones) -> Result<String> {
    let current_release = current_release_dir(cfg)?;
    current_release
        .file_name()
        .map(|value| value.to_string_lossy().to_string())
        .ok_or_else(|| anyhow::anyhow!("Failed to resolve current release name from {}", current_release.display()))
}

pub fn list_releases_sorted(cfg: &Bones) -> Result<Vec<String>> {
    let releases_dir = releases_dir(cfg);
    if !releases_dir.exists() {
        return Ok(Vec::new());
    }

    let mut names = Vec::new();
    for entry in fs::read_dir(&releases_dir)
        .with_context(|| format!("Failed to read releases dir: {}", releases_dir.display()))?
    {
        let entry = entry?;
        if entry.file_type()?.is_dir() {
            names.push(entry.file_name().to_string_lossy().to_string());
        }
    }

    names.sort();
    Ok(names)
}

pub fn point_symlink_atomically(link_path: &Path, target_path: &Path) -> Result<()> {
    let Some(parent) = link_path.parent() else {
        bail!("Invalid symlink path: {}", link_path.display());
    };

    fs::create_dir_all(parent).with_context(|| format!("Failed to create symlink parent: {}", parent.display()))?;

    // Generate unique temp symlink name to avoid collisions in concurrent deployments
    let nanos = SystemTime::now().duration_since(UNIX_EPOCH).context("System clock is before UNIX_EPOCH")?.as_nanos();
    let temp_name = format!(".tmp_current_{}_{}", process::id(), nanos);
    let temp_link = parent.join(temp_name);

    if fs::symlink_metadata(&temp_link).is_ok() {
        fs::remove_file(&temp_link)
            .with_context(|| format!("Failed to cleanup stale temp link: {}", temp_link.display()))?;
    }

    symlink(target_path, &temp_link).with_context(|| {
        format!("Failed to create temporary symlink {} -> {}", temp_link.display(), target_path.display())
    })?;

    fs::rename(&temp_link, link_path).with_context(|| {
        format!("Failed to atomically switch symlink {} -> {}", link_path.display(), target_path.display())
    })
}

#[cfg(test)]
mod tests {
    use std::env;
    use std::fs;
    use std::path::{Path, PathBuf};
    use std::process;
    use std::time::{SystemTime, UNIX_EPOCH};

    use anyhow::Result;
    use shared::config::Bones;
    use shared::paths;

    use super::{
        clear_staged_release, current_release_name, list_releases_sorted, point_symlink_atomically,
        read_staged_release, releases_dir, staged_release_path, write_staged_release,
    };

    fn temp_dir_path(test_name: &str) -> PathBuf {
        let nanos = SystemTime::now().duration_since(UNIX_EPOCH).map_or(0, |duration| duration.as_nanos());
        env::temp_dir().join(format!("bonesremote_release_state_test_{}_{}_{}", process::id(), nanos, test_name))
    }

    fn sample_config(root: &Path) -> Bones {
        let project = "unitapp";
        Bones {
            remote_name: String::from("production"),
            project_name: String::from(project),
            host: String::from("deploy.example.com"),
            port: String::from("22"),
            repo_path: root.join("repo.git").to_string_lossy().to_string(),
            project_root: root.join("deploy").to_string_lossy().to_string(),
            branch: String::from("master"),
            deploy_on_push: true,
            ..Default::default()
        }
    }

    #[test]
    fn write_then_read_staged_release_round_trips() -> Result<()> {
        let root = temp_dir_path("round_trip");
        fs::create_dir_all(&root)?;
        let cfg = sample_config(&root);

        write_staged_release(&cfg, "20260507_151500")?;
        let release_name = read_staged_release(&cfg)?;
        assert_eq!(release_name, "20260507_151500");

        fs::remove_dir_all(root)?;
        Ok(())
    }

    #[test]
    fn read_staged_release_rejects_empty_file() -> Result<()> {
        let root = temp_dir_path("empty_state");
        fs::create_dir_all(&root)?;
        let cfg = sample_config(&root);

        let state_path = staged_release_path(&cfg);
        if let Some(parent) = state_path.parent() {
            fs::create_dir_all(parent)?;
        }
        fs::write(&state_path, " \n")?;

        let result = read_staged_release(&cfg);
        assert!(result.is_err());

        fs::remove_dir_all(root)?;
        Ok(())
    }

    #[test]
    fn clear_staged_release_removes_state_file() -> Result<()> {
        let root = temp_dir_path("clear_state");
        fs::create_dir_all(&root)?;
        let cfg = sample_config(&root);

        write_staged_release(&cfg, "20260507_151501")?;
        clear_staged_release(&cfg)?;
        assert!(!staged_release_path(&cfg).exists());

        fs::remove_dir_all(root)?;
        Ok(())
    }

    #[test]
    fn point_symlink_atomically_creates_parent_dirs_and_points_to_target() -> Result<()> {
        let root = temp_dir_path("point_symlink_parent");
        fs::create_dir_all(&root)?;

        let target = root.join("target_dir");
        fs::create_dir_all(&target)?;

        let link_path = root.join("nested/path/current");
        point_symlink_atomically(&link_path, &target)?;

        assert!(link_path.exists());
        let linked = fs::read_link(&link_path)?;
        assert_eq!(linked, target);

        fs::remove_dir_all(root)?;
        Ok(())
    }

    #[test]
    fn point_symlink_atomically_repoints_existing_link() -> Result<()> {
        let root = temp_dir_path("point_symlink_repoint");
        fs::create_dir_all(&root)?;

        let target_a = root.join("target_a");
        let target_b = root.join("target_b");
        fs::create_dir_all(&target_a)?;
        fs::create_dir_all(&target_b)?;

        let link_path = root.join(paths::CURRENT_LINK);
        point_symlink_atomically(&link_path, &target_a)?;
        point_symlink_atomically(&link_path, &target_b)?;

        let linked = fs::read_link(&link_path)?;
        assert_eq!(linked, target_b);

        fs::remove_dir_all(root)?;
        Ok(())
    }

    #[test]
    fn list_releases_sorted_returns_only_directories_in_order() -> Result<()> {
        let root = temp_dir_path("list_releases");
        fs::create_dir_all(&root)?;
        let cfg = sample_config(&root);

        let releases = releases_dir(&cfg);
        fs::create_dir_all(&releases)?;
        fs::create_dir_all(releases.join("20260507_120000"))?;
        fs::create_dir_all(releases.join("20260507_110000"))?;
        fs::write(releases.join("notes.txt"), "not a release")?;

        let items = list_releases_sorted(&cfg)?;
        assert_eq!(items, vec![String::from("20260507_110000"), String::from("20260507_120000")]);

        fs::remove_dir_all(root)?;
        Ok(())
    }

    #[test]
    fn current_release_name_resolves_from_current_symlink() -> Result<()> {
        let root = temp_dir_path("current_release_name");
        fs::create_dir_all(&root)?;
        let cfg = sample_config(&root);

        let releases_dir = releases_dir(&cfg);
        let release = releases_dir.join("20260507_170000");
        fs::create_dir_all(&release)?;

        let current = PathBuf::from(cfg.deployment_paths(paths::DEFAULT_WEB_ROOT).current);
        point_symlink_atomically(&current, &release)?;

        let name = current_release_name(&cfg)?;
        assert_eq!(name, "20260507_170000");

        fs::remove_dir_all(root)?;
        Ok(())
    }
}

```

`crates/shared/Cargo.toml`:

```toml
[package]
name = "shared"
version = "0.1.0"
edition = "2021"

[dependencies]
anyhow = "1.0.102"
serde = { version = "1", features = ["derive"] }
toml = "0.8"

[lints.clippy]
# broad groups (lower priority so individual lint overrides take effect)
correctness = { level = "deny", priority = -1 }
suspicious = { level = "deny", priority = -1 }
complexity = { level = "warn", priority = -1 }
style = { level = "warn", priority = -1 }
perf = { level = "warn", priority = -1 }
pedantic = { level = "warn", priority = -1 }

# readability / naming
similar_names = "warn"
many_single_char_names = "warn"
module_name_repetitions = "warn"
enum_variant_names = "warn"
struct_field_names = "warn"
disallowed_names = "deny"
wildcard_imports = "warn"
module_inception = "warn"

# complexity / API readability
cognitive_complexity = "warn"
too_many_arguments = "deny"
fn_params_excessive_bools = "warn"
large_types_passed_by_value = "warn"
trivially_copy_pass_by_ref = "warn"

# panic / debug leftovers
unwrap_used = "deny"
expect_used = "deny"
panic = "deny"
todo = "deny"
unimplemented = "deny"
dbg_macro = "deny"
# This is a CLI binary: stdout/stderr output is the intended UX.
print_stdout = "allow"
print_stderr = "allow"

# docs / contracts
missing_panics_doc = "deny"
missing_errors_doc = "deny"
missing_safety_doc = "deny"
undocumented_unsafe_blocks = "deny"

# numeric safety
cast_possible_truncation = "warn"
cast_sign_loss = "warn"
cast_possible_wrap = "warn"
checked_conversions = "warn"

# anti-mess / consistency
absolute_paths = "warn"
allow_attributes = "deny"
redundant_clone = "warn"
implicit_clone = "warn"
semicolon_if_nothing_returned = "warn"
match_same_arms = "warn"
needless_pass_by_value = "warn"
cloned_instead_of_copied = "warn"
flat_map_option = "warn"
from_iter_instead_of_collect = "warn"
inefficient_to_string = "warn"
manual_let_else = "warn"
manual_ok_or = "warn"
map_unwrap_or = "warn"
unnecessary_wraps = "warn"


```

`crates/shared/src/config.rs`:

```rs
use std::fs;
use std::path::Path;

use anyhow::{bail, Context, Result};
use serde::{Deserialize, Serialize};

use crate::paths::{self, Deployment};

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(default)]
pub struct Bones {
    pub remote_name: String,
    pub project_name: String,
    pub ssh_user: String,
    pub host: String,
    pub port: String,
    #[serde(skip_serializing_if = "String::is_empty")]
    pub repo_path: String,
    #[serde(skip_serializing_if = "String::is_empty")]
    pub project_root: String,
    #[serde(skip_serializing_if = "String::is_empty")]
    pub branch: String,
    #[serde(skip_serializing_if = "String::is_empty")]
    pub preview_domain: String,
    pub deploy_on_push: bool,
    #[serde(rename = "releases")]
    pub releases_keep: usize,
    pub ssl_enabled: bool,
    pub domain: String,
    pub email: String,
}

impl Default for Bones {
    fn default() -> Self {
        Self {
            remote_name: String::new(),
            project_name: String::new(),
            ssh_user: String::from("root"),
            host: String::new(),
            port: "22".into(),
            repo_path: String::new(),
            project_root: String::new(),
            branch: "master".into(),
            preview_domain: String::new(),
            deploy_on_push: false,
            releases_keep: 5,
            ssl_enabled: false,
            domain: String::new(),
            email: String::new(),
        }
    }
}

impl Bones {
    #[must_use]
    pub fn deployment_paths(&self, web_root: &str) -> Deployment {
        Deployment::new(&self.project_name, &self.repo_path, &self.project_root, web_root)
    }
}

#[must_use]
pub fn default_deploy_user() -> String {
    paths::DEPLOY_USER.to_string()
}

#[must_use]
pub fn parse_port(port: &str) -> Result<u16> {
    port.parse().with_context(|| format!("Invalid port: {port}"))
}

pub fn validate_host(host: &str) -> Result<()> {
    let host = host.trim();
    if host.is_empty() {
        return Ok(());
    }

    if host.chars().all(|ch| ch.is_ascii_alphanumeric() || matches!(ch, '.' | '-')) {
        return Ok(());
    }

    bail!("Invalid host: {host}")
}

#[must_use]
pub fn runtime_user_for(project_name: &str) -> String {
    project_name.to_string()
}

#[must_use]
pub fn runtime_group_for(project_name: &str) -> String {
    project_name.to_string()
}

#[must_use]
pub fn release_group_for(project_name: &str) -> String {
    format!("{project_name}-release")
}

#[derive(Clone, Debug, Default, Serialize, Deserialize)]
#[serde(default)]
pub struct Shared {
    pub paths: Vec<SharedPath>,
}

#[derive(Clone, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub struct SharedPath {
    pub path: String,
    #[serde(rename = "type")]
    pub path_type: PathType,
}

#[derive(Clone, Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
pub enum PathType {
    File,
    Dir,
}

#[must_use]
pub fn default_repo_path_for(project_name: &str) -> String {
    paths::default_repo_path_for(project_name)
}

#[must_use]
pub fn default_preview_domain_for(project_name: &str, host: &str) -> String {
    let project = sanitize_domain_label(project_name);
    let host = sanitize_domain_label(host);

    if project.is_empty() || host.is_empty() {
        return String::new();
    }

    format!("{project}-{host}.nip.io")
}

fn sanitize_domain_label(value: &str) -> String {
    value
        .trim()
        .chars()
        .map(|ch| if ch.is_ascii_alphanumeric() { ch.to_ascii_lowercase() } else { '-' })
        .collect::<String>()
        .trim_matches('-')
        .to_string()
}

const RUNTIME_TOML: &str = "runtime.toml";

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Runtime {
    #[serde(default = "paths::default_web_root")]
    pub web_root: String,
    #[serde(default)]
    pub runtime_user: String,
    #[serde(default)]
    pub runtime_group: String,
    #[serde(default)]
    pub release_group: String,
}

/// Loads the runtime configuration from a TOML file, falling back to defaults.
///
/// # Errors
///
/// Returns an error if the file exists but cannot be read or parsed.
pub fn load_runtime(config_dir: &Path) -> Result<Runtime> {
    let path = config_dir.join(RUNTIME_TOML);
    if path.exists() {
        let content = fs::read_to_string(&path).with_context(|| format!("Failed to read {}", path.display()))?;
        Ok(toml::from_str(&content).with_context(|| format!("Failed to parse {}", path.display()))?)
    } else {
        Ok(Runtime {
            web_root: paths::default_web_root(),
            runtime_user: String::new(),
            runtime_group: String::new(),
            release_group: String::new(),
        })
    }
}

pub fn apply_derived_defaults(config: &mut Bones) {
    let project_name = &config.project_name;

    if config.ssh_user.is_empty() {
        config.ssh_user = String::from("root");
    }
    if config.repo_path.is_empty() {
        config.repo_path = default_repo_path_for(project_name);
    }
    if config.project_root.is_empty() {
        config.project_root = paths::default_project_root_for(project_name);
    }
    if config.preview_domain.is_empty() {
        config.preview_domain = default_preview_domain_for(project_name, &config.host);
    }
}

/// Loads and parses a `bones.toml` configuration file, applying derived defaults.
///
/// # Errors
///
/// Returns an error if the file cannot be read or the TOML is invalid.
pub fn load(path: &Path) -> Result<Bones> {
    let content = fs::read_to_string(path).with_context(|| format!("Failed to read {}", path.display()))?;
    let mut config: Bones = toml::from_str(&content).with_context(|| format!("Failed to parse {}", path.display()))?;
    apply_derived_defaults(&mut config);
    validate_host(&config.host)?;
    Ok(config)
}

#[cfg(test)]
mod tests {
    use super::validate_host;

    #[test]
    fn validate_host_accepts_hostnames_and_ips() {
        assert!(validate_host("deploy.example.com").is_ok());
        assert!(validate_host("192.0.2.10").is_ok());
        assert!(validate_host("").is_ok());
    }

    #[test]
    fn validate_host_rejects_shell_metacharacters() {
        assert!(validate_host("deploy.example.com;rm -rf /").is_err());
    }
}

```

`crates/shared/src/lib.rs`:

```rs
pub mod config;
pub mod paths;

```

`crates/shared/src/paths.rs`:

```rs
use std::env;
use std::path::{Path, PathBuf};

use serde::{Deserialize, Serialize};

pub const DEFAULT_REPO_PARENT: &str = "/home/git";
pub const DEFAULT_PROJECT_ROOT_PARENT: &str = "/srv/sites";
pub const DEFAULT_CONF_ROOT_PARENT: &str = "/srv/conf";
pub const DEFAULT_WEB_ROOT: &str = "public";

pub const DEPLOY_USER: &str = "git";
pub const DEFAULT_GROUP: &str = "www-data";

pub const ETC_NGINX: &str = "/etc/nginx";
pub const ETC_NGINX_SITES_AVAILABLE: &str = "/etc/nginx/sites-available";
pub const ETC_NGINX_SITES_ENABLED: &str = "/etc/nginx/sites-enabled";
pub const ETC_SYSTEMD_SYSTEM: &str = "/etc/systemd/system";
pub const ETC_APPARMOR_D: &str = "/etc/apparmor.d";
pub const ETC_LETSENCRYPT_LIVE: &str = "/etc/letsencrypt/live";
pub const ETC_SUDOERS_D: &str = "/etc/sudoers.d";
pub const ETC_OS_RELEASE: &str = "/etc/os-release";
pub const APPARMOR_ENABLED_PARAM: &str = "/sys/module/apparmor/parameters/enabled";
pub const APPARMOR_PROFILES: &str = "/sys/kernel/security/apparmor/profiles";
pub const PROC_MODULES: &str = "/proc/modules";
pub const ETC_MODPROBE_D: &str = "/etc/modprobe.d";
pub const USR_LOCAL_BIN: &str = "/usr/local/bin";
pub const OPT_BONESDEPLOY: &str = "/opt/bonesdeploy";
pub const TMP_ROOT: &str = "/tmp";

pub const LOCAL_BONES_DIR: &str = ".bones";
pub const LOCAL_BONES_TOML: &str = ".bones/bones.toml";
pub const LOCAL_BONES_HOOKS_DIR: &str = ".bones/hooks";
pub const LOCAL_BONES_HOOKS_SCRIPT: &str = ".bones/hooks/hooks.sh";
pub const LOCAL_BONES_DEPLOYMENT_DIR: &str = ".bones/deployment";
pub const LOCAL_BONES_RUNTIME_TOML: &str = ".bones/runtime.toml";

pub const BONES_DIR: &str = "bones";
pub const BONES_TOML: &str = "bones.toml";
pub const NGINX_CONF: &str = "nginx.conf";
pub const INDEX_HTML: &str = "index.html";
pub const GIT_HEAD: &str = "HEAD";
pub const DEPLOYMENT_DIR: &str = "deployment";
pub const RELEASES_DIR: &str = "releases";
pub const SHARED_DIR: &str = "shared";
pub const BUILD_DIR: &str = "build";
pub const WORKSPACE_DIR: &str = "workspace";
pub const LOGS_DIR: &str = "logs";
pub const CURRENT_LINK: &str = "current";
pub const INSTALL_VERSIONS_DIR: &str = "versions";
pub const INSTALL_CURRENT_LINK: &str = "current";
pub const BONESDEPLOY_SWAP_LINK: &str = ".bonesdeploy_swap";
pub const BONESREMOTE_SWAP_LINK_PREFIX: &str = ".bonesremote_swap_";
pub const PLACEHOLDER_RELEASE_NAME: &str = "19700101_000000";
pub const STAGED_RELEASE_FILE: &str = ".staged_release";
pub const SUDOERS_FILE: &str = "bonesdeploy";
pub const SUDOERS_PATH: &str = "/etc/sudoers.d/bonesdeploy";
pub const BONESDEPLOY_BINARY: &str = "bonesdeploy";
pub const BONESREMOTE_BINARY: &str = "bonesremote";
pub const NGINX_SOCKET: &str = "nginx.sock";
pub const NGINX_PID: &str = "nginx.pid";
pub const PHP_FPM_SOCKET: &str = "php-fpm.sock";
pub const DEFAULT_NGINX_SITE: &str = "default";

pub const GIT_HOOKS_DIR: &str = ".git/hooks";
pub const GIT_PRE_PUSH_HOOK: &str = ".git/hooks/pre-push";
pub const PRE_PUSH_HOOK_NAME: &str = "pre-push";
pub const PRE_PUSH_HOOK_TARGET: &str = "../../.bones/hooks/pre-push";
pub const HOOKS_DIR: &str = "hooks";
pub const KIT_HOOKS_DIR: &str = "hooks/";
pub const KIT_DEPLOYMENT_DIR: &str = "deployment/";

const RUNTIME_SOCKET_PARENT: &str = "/run";

#[must_use]
pub fn default_repo_path_for(project_name: &str) -> String {
    Path::new(DEFAULT_REPO_PARENT).join(format!("{project_name}.git")).display().to_string()
}

#[must_use]
pub fn default_project_root_for(project_name: &str) -> String {
    Path::new(DEFAULT_PROJECT_ROOT_PARENT).join(project_name).display().to_string()
}

#[must_use]
pub fn default_web_root() -> String {
    DEFAULT_WEB_ROOT.to_string()
}

#[must_use]
pub fn ssl_certificate_path(domain: &str) -> String {
    Path::new(ETC_LETSENCRYPT_LIVE).join(domain).join("fullchain.pem").display().to_string()
}

#[must_use]
pub fn ssl_certificate_key_path(domain: &str) -> String {
    Path::new(ETC_LETSENCRYPT_LIVE).join(domain).join("privkey.pem").display().to_string()
}

#[must_use]
pub fn bonesremote_staging_path(version: &str) -> String {
    Path::new(TMP_ROOT).join(format!("{BONESREMOTE_BINARY}-{version}")).display().to_string()
}

#[must_use]
pub fn install_root() -> PathBuf {
    PathBuf::from(OPT_BONESDEPLOY)
}

#[must_use]
pub fn install_versions_dir() -> PathBuf {
    install_root().join(INSTALL_VERSIONS_DIR)
}

#[must_use]
pub fn install_current_dir() -> PathBuf {
    install_root().join(INSTALL_CURRENT_LINK)
}

#[must_use]
pub fn bonesdeploy_global_link() -> PathBuf {
    Path::new(USR_LOCAL_BIN).join(BONESDEPLOY_BINARY)
}

#[must_use]
pub fn bonesremote_global_link() -> PathBuf {
    Path::new(USR_LOCAL_BIN).join(BONESREMOTE_BINARY)
}

#[derive(Clone, Debug, Serialize, Deserialize, PartialEq, Eq)]
pub struct Deployment {
    pub repo: String,
    pub repo_parent: String,
    pub repo_head: String,
    pub repo_bones: String,
    pub repo_bones_toml: String,
    pub repo_deployment: String,
    pub site_nginx_config: String,
    pub conf_root: String,
    pub project_root: String,
    pub project_root_parent: String,
    pub releases: String,
    pub shared: String,
    pub build_root: String,
    pub build_logs: String,
    pub current: String,
    pub current_web_root: String,
    pub placeholder_release: String,
    pub placeholder_web_root: String,
    pub placeholder_index: String,
    pub nginx_site_available: String,
    pub nginx_site_enabled: String,
    pub nginx_default_site_enabled: String,
    pub systemd_site_nginx_service: String,
    pub apparmor_profile_path: String,
    pub runtime_socket_dir: String,
    pub runtime_nginx_socket: String,
    pub runtime_nginx_pid: String,
    pub runtime_php_fpm_socket: String,
    pub sudoers_path: String,
    pub usr_local_bin: String,
    pub bonesremote_global_link: String,
    pub apparmor_enabled_param: String,
    pub apparmor_profiles: String,
}

impl Deployment {
    #[must_use]
    pub fn new(project_name: &str, repo_path: &str, project_root: &str, web_root: &str) -> Self {
        let repo = repo_path.to_string();
        let project_root = project_root.to_string();
        let placeholder_release = Path::new(&project_root).join(RELEASES_DIR).join(PLACEHOLDER_RELEASE_NAME);
        let current = Path::new(&project_root).join(CURRENT_LINK);
        let runtime_socket_dir = Path::new(RUNTIME_SOCKET_PARENT).join(project_name);
        let repo_bones = Path::new(&repo).join(BONES_DIR);
        let conf_root = Path::new(DEFAULT_CONF_ROOT_PARENT).join(project_name);

        Self {
            repo: repo.clone(),
            repo_parent: parent_or_default(&repo, DEFAULT_REPO_PARENT),
            repo_head: Path::new(&repo).join(GIT_HEAD).display().to_string(),
            repo_bones: repo_bones.display().to_string(),
            repo_bones_toml: repo_bones.join(BONES_TOML).display().to_string(),
            site_nginx_config: conf_root.join(NGINX_CONF).display().to_string(),
            repo_deployment: repo_bones.join(DEPLOYMENT_DIR).display().to_string(),
            conf_root: conf_root.display().to_string(),
            project_root: project_root.clone(),
            project_root_parent: parent_or_default(&project_root, DEFAULT_PROJECT_ROOT_PARENT),
            releases: Path::new(&project_root).join(RELEASES_DIR).display().to_string(),
            shared: Path::new(&project_root).join(SHARED_DIR).display().to_string(),
            build_root: Path::new(&project_root).join(BUILD_DIR).join(WORKSPACE_DIR).display().to_string(),
            build_logs: Path::new(&project_root).join(BUILD_DIR).join(LOGS_DIR).display().to_string(),
            current: current.display().to_string(),
            current_web_root: current.join(web_root).display().to_string(),
            placeholder_release: placeholder_release.display().to_string(),
            placeholder_web_root: placeholder_release.join(web_root).display().to_string(),
            placeholder_index: placeholder_release.join(web_root).join(INDEX_HTML).display().to_string(),
            nginx_site_available: Path::new(ETC_NGINX_SITES_AVAILABLE)
                .join(format!("{project_name}.conf"))
                .display()
                .to_string(),
            nginx_site_enabled: Path::new(ETC_NGINX_SITES_ENABLED)
                .join(format!("{project_name}.conf"))
                .display()
                .to_string(),
            nginx_default_site_enabled: Path::new(ETC_NGINX_SITES_ENABLED)
                .join(DEFAULT_NGINX_SITE)
                .display()
                .to_string(),
            systemd_site_nginx_service: Path::new(ETC_SYSTEMD_SYSTEM)
                .join(format!("{project_name}-nginx.service"))
                .display()
                .to_string(),
            apparmor_profile_path: Path::new(ETC_APPARMOR_D)
                .join(format!("bonesdeploy-{project_name}-nginx"))
                .display()
                .to_string(),
            runtime_socket_dir: runtime_socket_dir.display().to_string(),
            runtime_nginx_socket: runtime_socket_dir.join(NGINX_SOCKET).display().to_string(),
            runtime_nginx_pid: runtime_socket_dir.join(NGINX_PID).display().to_string(),
            runtime_php_fpm_socket: runtime_socket_dir.join(PHP_FPM_SOCKET).display().to_string(),
            sudoers_path: Path::new(ETC_SUDOERS_D).join(SUDOERS_FILE).display().to_string(),
            usr_local_bin: USR_LOCAL_BIN.to_string(),
            bonesremote_global_link: Path::new(USR_LOCAL_BIN).join(BONESREMOTE_BINARY).display().to_string(),
            apparmor_enabled_param: APPARMOR_ENABLED_PARAM.to_string(),
            apparmor_profiles: APPARMOR_PROFILES.to_string(),
        }
    }
}

fn parent_or_default(path: &str, fallback: &str) -> String {
    Path::new(path)
        .parent()
        .filter(|parent| !parent.as_os_str().is_empty())
        .map_or_else(|| fallback.to_string(), |parent| parent.display().to_string())
}

fn home_dir() -> PathBuf {
    env::var("HOME").map_or_else(|_| PathBuf::from("/root"), PathBuf::from)
}

#[must_use]
pub fn bones_config_root() -> PathBuf {
    if let Some(dir) = env::var("XDG_CONFIG_HOME").ok().filter(|v| !v.is_empty()) {
        Path::new(&dir).join("bonesdeploy")
    } else {
        home_dir().join(".config/bonesdeploy")
    }
}

#[must_use]
pub fn bones_state_root() -> PathBuf {
    if let Some(dir) = env::var("XDG_STATE_HOME").ok().filter(|v| !v.is_empty()) {
        Path::new(&dir).join("bonesdeploy")
    } else {
        home_dir().join(".local/state/bonesdeploy")
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn bones_config_root_uses_xdg_config_home() {
        let home = home_dir();
        let expected = home.join(".config/bonesdeploy");
        assert_eq!(bones_config_root(), expected);
    }

    #[test]
    fn bones_state_root_uses_xdg_state_home() {
        let home = home_dir();
        let expected = home.join(".local/state/bonesdeploy");
        assert_eq!(bones_state_root(), expected);
    }
}

```

`docker/Dockerfile`:

```
FROM debian:stable

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        bash \
        git \
        rsync \
        sudo \
        openssh-server \
    && rm -rf /var/lib/apt/lists/*

```

`docker/docker-compose.yml`:

```yml
services:
  bonesdeploy-test-server:
    privileged: true
    build:
      context: .
    container_name: bonesdeploy-test-server
    ports:
      - "2222:22"
    working_dir: /workspace
    volumes:
      - ./:/workspace
      - ${HOME}/.ssh/id_rsa.pub:/tmp/host_key.pub:ro
    tmpfs:
      - /var/lib/bonesdeploy-test-server
    command: >
      /bin/bash -lc "
      mkdir -p /run/sshd /root/.ssh &&
      cat /tmp/host_key.pub > /root/.ssh/authorized_keys &&
      chmod 700 /root/.ssh &&
      chmod 600 /root/.ssh/authorized_keys &&
      /usr/sbin/sshd -D -e
      "

```

`docs/PROJECT.md`:

```md
# BonesDeploy v3

A remote release deployment tool for simple Linux servers. It produces two executables: `bonesdeploy` (local CLI for setup, provisioning, deployment, and management) and `bonesremote` (server-side release lifecycle executor, installed on the deployment host). Git remains supported as an optional trigger, but it does not own the deployment model. **We only handle Debian/Ubuntu machines.**

We keep detailed documentation of each command at: `docs/commands/*.md:`

## Deployment Methodology
We have an SSH deployment user (normally `git`) that handles deployment concerns. This user has a home folder, restricted sudo ability, but no password login. We also have a per-project service user named after the project. This is not a shared `applications` user; it must be a dedicated user per project so isolation works on a shared server. This user has no home folder, no login, and no sudo ability. This is ultimately who we want to own our project files to limit attack scope.

### Just-in-Time Concerns
This project should prefer just-in-time mutations.

A concern should only be handled at the last responsible moment: immediately before the system would fail if that mutation did not occur. We should not widen permissions, rewrite symlinks, mutate shared state, or otherwise touch live project state early just because a later step might need it. The idea here is to limit the surface of attack time, so that potential vulnerabilities are not created by "jumping the gun" to solve a problem too early, long before it arises.

This principle exists to keep deployment behavior coherent and safe:

- the pre-deploy steps (doctor, stage, checkout, wire) should validate and prepare isolated state, not mutate live state.
- build steps should operate on isolated workspace state whenever possible.
- activation concerns should happen at activation time.
- permission hardening should happen after a successful activation, not before.
- if a deploy fails, it should not leave behind broadened access or half-applied live mutations.

In practice, this means we should prefer:
- isolated staging over speculative live-state mutation
- narrow, local changes over recursive ownership changes
- exact, just-before-use fixes over broad upfront rewrites
- failure-safe sequencing over convenience

If a mutation can be delayed safely, it should be delayed.
If a mutation affects live state, it must be justified by an immediate need.

### Common Problems
- Shared groups have too many logic traps. My apps should not have 660 or 770 permissions on all files so that a `git` user can have read/write.
- I don't like ACLs; they're far too opaque.
- Setting up inotify systems are cumbersome.

### Permission Model

Permissions are a **provisioning-time contract**, not a deployment-time repair. The ownership layout is established once during `bonesdeploy remote setup` and never rewritten by deploy commands.

**Three identity classes:**

| Identity | Owner of | Scope |
|----------|----------|-------|
| `git` (deploy user) | Bare repo, release dirs, build workspace | Creates immutable release artifacts |
| `<site>` (runtime user) | Shared files, `/run/<site>`, writable paths | Mutates runtime state |
| `root` | System units, config dirs, users/groups | Provisions and restarts services |

**Key mechanics:**

- `releases/` has the setgid bit (`2750`) so group `foo-release` is inherited by new release dirs without chown.
- `shared/` is owned by the runtime user (`foo:foo 0711`) — only the app writes here.
- `build/` is private to the deploy user (`git:git 0700`) — invisible to other processes.
- `bonesremote service restart` is the only command that needs `sudo` — a narrow sudoers drop-in allows it.
- No deploy step calls `chown`, `chmod -R`, or otherwise mutates ownership after provisioning.

## Bones Scaffolding
```
.bones
├── bones.toml
├── runtime.toml
├── hooks
│   ├── hooks.sh                      # shared hook library, sourced by every hook
│   ├── post-receive
│   └── pre-push
├── deployment
│   ├── 01_install_build_deps.sh
│   └── 02_run_build.sh
```

Python infra scripts and templates are managed separately by the hidden `bonesinfra` checkout; see `crates/bonesdeploy/src/infra/bonesinfra.rs`.

### Bones TOML
This stores crucial data we will need and is collected on running `bonesdeploy init` via user prompts.  
Collects the following project information from the user:
- `project_name`: str
- `branch`: str
- `remote_name`: existing remote selection when available, otherwise prompted; defaults to `production`. Must point to a fresh VPS, not a code host like GitHub.
- `host`: prompted when not inferable from selected remote
- `port`: defaults to `22`, prompt shown when remote inference is unavailable
- `repo_path`: inferred from selected remote URL when possible, else defaults to `/home/git/{project_name}.git`

Everything else is defaulted or derived for Debian/Ubuntu-first usability:
- `project_root`: defaults to `/srv/sites/{project_name}`
- `ssh_user`: defaults to `root`
- `deploy_on_push`: defaults to `false`
- `releases.keep`: defaults to `5`

`web_root`, `runtime_user`, `runtime_group`, and `release_group` live in `.bones/runtime.toml`. Those identity values default to `{project_name}`, `{project_name}`, and `{project_name}-release` respectively.

Users can override any default by editing `.bones/bones.toml` after init.

Example `bones.toml`:
```toml
remote_name = "production"
project_name = "lawsnipe"
ssh_user = "root"
host = "deploy.example.com"
port = "22"
repo_path = "/home/git/lawsnipe.git"
project_root = "/srv/sites/lawsnipe"
branch = "master"
preview_domain = "lawsnipe-deploy-example-com.nip.io"
domain = "app.example.com"
email = "ops@example.com"
deploy_on_push = false
ssl_enabled = true
releases = 5
```

### Hooks
Hooks are static shell scripts embedded in the `bonesdeploy` binary. They are written to `.bones/hooks/` once during `bonesdeploy init`, and they source shared functions from `.bones/hooks/hooks.sh`. After that, they belong to the user and can be edited freely. They are synced to the remote bare repo via `bonesdeploy push` and can be restored locally with `bonesdeploy pull`.

- `pre-push` => Local hook, symlinked to `.git/hooks/pre-push`. This checks to see if we are pushing to our bonesdeploy designated remote. If so, then we run `bonesdeploy doctor --local` and we fail if the doctor command expresses any warning or errors.
- `post-receive` => Resolves the configured deployment ref from stdin, then runs a single `bonesremote deploy --config "$BONES_TOML" --revision <newrev>` command. This unified command orchestrates the full pipeline: doctor → stage_release → post_receive (git checkout) → wire_release → deploy (scripts + activate) → service restart → post_deploy (prune). If the push didn't touch the configured branch, or the branch was deleted, post-receive exits without deploying.

### Deployment Folder
This folder stores deployment scripts that are run by `bonesremote deploy`. Files in this folder must be ordered sequentially like `01_install_deps.sh`, `02_run_build.sh`. They are named in numerical order and all of these scripts are always run.

## Crate Structure
This Cargo workspace has three crates under `crates/`:
- `bonesdeploy` for the local CLI binary
- `bonesremote` for the server-side binary
- `shared` for code that must be common to both binaries

### Path Centralization
All product-owned paths must live in `crates/shared/src/paths.rs`.

Other modules may derive subpaths by joining values from `shared::paths`, but they must not introduce their own independent path roots, filenames, or install locations.

This applies to Rust code, pyinfra deploy scripts, Jinja2 templates, and docs examples that describe the system layout.

```
bonesdeploy/
├── Cargo.toml                  # workspace root
├── crates/
│   ├── bonesdeploy/
│   │   ├── kit/                # embedded scaffolding templates and hooks
│   │   └── src/
│   │       ├── cli/            # clap args + dispatch
│   │       ├── commands/       # CLI command implementations
│   │       ├── infra/          # ssh, git, embedded assets, bonesinfra wrapper
│   │       ├── ui/             # prompt helpers
│   │       ├── config.rs
│   │       └── main.rs
│   ├── bonesremote/
│   │   └── src/
│   │       ├── cli/            # clap args + dispatch
│   │       ├── commands/       # remote release lifecycle steps
│   │       ├── config.rs
│   │       ├── privileges.rs   # sudoers drop-in install + privilege checks
│   │       ├── release/
│   │       ├── release_state.rs
│   │       └── main.rs
│   └── shared/                 # config schema + central paths
└── docs/
```

### Per-Framework Templates
Runtime templates ship starter overlays that `bonesdeploy remote runtime` uses when scaffolding infrastructure for a matching framework. Each template lives in the `bonesinfra` repo (`https://github.com/AlextheYounga/bonesinfra.git`) — framework runtime assets (`operations.py`, Jinja2 templates) stay together:

- `runtimes/laravel/`        → Laravel (PHP + PHP-FPM)

Templates inherit the same `bones.toml` schema and customize permissions paths, deployment scripts, and the runtime operations captured in the `bonesinfra` repo.

### BonesDeploy CLI Commands
- **init**:
  - Gets or creates the `.bones` folder with our default scaffolding.
  - Updates `.gitignore` to add .bones folder.
  - Loads existing config from `.bones/bones.toml` or collects user input via prompts.
  - Creates local deployment remote if missing using `{deploy_user}@{host}:{repo_path}`, constructed from the production VPS target configured during prompts.
  - Prints next-step guidance to run `bonesdeploy remote setup` and `bonesdeploy remote runtime` before first deploy.
  - Saves config to `.bones/bones.toml`.

- **doctor**
  - This command checks all concerns in your local environment.
  - Loads config from `.bones/bones.toml`
  - Runs local checks:
    - `.bones` folder is set up correctly. Deployment scripts are named appropriately.
    - Local `pre-push` hook is symlinked properly when `deploy_on_push = true`.
  - Runs remote checks (skipped with `--local`):
    - `bonesremote` executable exists on remote and can be run globally.
    - `{project_name}.git/bones` folder exists on remote (needs `bonesdeploy push` warning)
    - `{project_name}.git/bones/hooks` matches with `{project_name}.git/hooks` inside the remote bare repo when `deploy_on_push = true`.
  - The `--local` flag skips all remote checks. The `pre-push` hook uses this flag because it is only a local guard before optional git-triggered deploys.

- **push**
  - Uses an `rsync -av --delete` command to push up our local `.bones` folder to the bare repo.
  - We will create a `bones` folder under our `{project_name}.git/` folder so that everything is self-contained inside git.
  - Deletes sample git hooks in bare repo, so that our files will be the only files to worry about in the `{project_name}.git/hooks` folder.
  - Runs commands on remote that symlinks our `{project_name}.git/bones/hooks` files are symlinked with `{project_name}.git/hooks` properly.

- **pull**
  - Uses an `rsync -av --delete` command to pull the remote `{project_name}.git/bones/` folder back into local `.bones/`.
  - Recreates the local `.git/hooks/pre-push` symlink so the repository regains its pre-push check after recovery.

- **deploy**
  - SSHes into the configured host and runs `bonesremote deploy --config <remote_bones_toml>` directly, without pushing commits or using git hooks.
  - Omits the `--revision` flag, so `bonesremote deploy` uses the configured branch from `bones.toml`.

- ****remote setup****
  - runs the setup script from the hidden `bonesinfra` checkout via `pyinfra` against the configured host as root (or `BONES_BOOTSTRAP_SSH_USER`).
  - Passes `bones.toml` deployment values plus computed paths and variables as pyinfra data.
  - Initializes bare git repository at `repo_path`.
  - Creates initial placeholder release with default page.
  - Installs `bonesremote` from source and runs `bonesremote init`.
  - Provisions machine-level dependencies (users, groups, firewall, system packages).

- **remote runtime**:
  - Prompts for a framework template, refreshes `.bones/runtime/`, and writes `.bones/runtime.toml`.
  - Reapplies template-specific defaults into `.bones/bones.toml` only when they still match generic or previous-template values.
  - After a `y/N` confirmation, runs the runtime script from the hidden `bonesinfra` checkout via `pyinfra` against the configured host as the deploy user.
  - Loads the template's `operations.py` at runtime to install framework-specific packages and services.
  - Configures per-site runtime assets: AppArmor profile, nginx router + per-site config + systemd service, and runs `bonesremote doctor`.
  - Does not handle SSL; use `remote ssl` for TLS configuration.

- **remote ssl**
  - Runs the SSL script from the hidden `bonesinfra` checkout via `pyinfra` against the configured host as root.
  - Uses certbot with a webroot challenge to obtain/renew certificates for the configured domain.
  - Re-renders the per-site runtime nginx router with TLS enabled, listening on 443 and redirecting HTTP to HTTPS.
  - Separate from `remote runtime` to keep certificate management decoupled from app runtime concerns.

- **rollback**
  - SSHes into the configured host and runs `bonesremote release rollback --config ...`, which repoints `current` to the previous release without rebuilding.

- **version**:
  - Echoes the installed `bonesdeploy` version.

### BonesRemote CLI Commands
- **Release commands** live under `bonesremote release ...`
- **Service commands** live under `bonesremote service ...`
- **deploy**:
  - Runs the full deployment lifecycle as a single command (the primary entrypoint used by both `post-receive` hook and `bonesdeploy deploy`).
  - Orchestrates: doctor → stage_release → post_receive (git checkout) → wire_release → deploy scripts → activate → service restart → post_deploy.
  - On failure, automatically drops the staged release.
  - `--config <path>`: path to `bones.toml`
  - `--revision <rev>`: optional exact commit to check out; defaults to configured branch
- **init**:
  - Must be run as sudo.
  - Installs a drop-in file at `/etc/sudoers.d/bonesdeploy` to allow only `sudo bonesremote service restart --config *` without requiring password.
- **doctor**:
  - Checks to see if the server is set up properly:
    - `bonesremote` is globally available.
    - AppArmor support is available on the host.
    - Sudoers drop-in is correctly configured.
- **release stage**
	- Creates a staged release tree under `releases/`, ensures `build/workspace` and `shared/`, then writes staged release state before checkout.
- **release wire**
	- Wires shared paths into `build/workspace` after checkout, replacing any existing build workspace paths with symlinks to the shared directory.
- **release activate**
	- Atomically switches `current` to the staged release and clears staged release state.
- **release drop-failed**
	- Deletes a failed staged release and clears staged release state.
- **release rollback**
	- Repoints `current` to the previous release.
- **service restart**
	- Restarts the per-site nginx systemd service. This is the only `bonesremote` command that requires root privileges.
- **version**:
  - Echoes the installed `bonesremote` version.

## Security Notes
- Sudo access for the deployment user is strictly limited to passwordless execution of `bonesremote service restart --config *` via the `/etc/sudoers.d/bonesdeploy` drop-in installed by `bonesremote init`.
- No broader sudo privileges are granted — the deploy user cannot run arbitrary commands as root, read root-owned files, or write outside their owned directories.
- All release artifacts are created with the setgid bit on `releases/` so the runtime group inherits read access without needing a post-deploy chown.
- The build workspace (`build/`) is private to the deploy user (`0700`), invisible to other processes.
- Runtime processes are sandboxed via systemd `ProtectSystem=strict`, `NoNewPrivileges=yes`, `PrivateTmp=yes`, and AppArmor profiles — limiting blast radius even if a service is compromised.
- Per-project systemd services run as the dedicated runtime user, not a shared `www-data` — so service isolation is enforced at the OS level, not just the application level.

## Flow
- User runs `bonesdeploy init`, and the procedures outlined above are executed.
- User can make any changes to their deployment scripts or hooks in `.bones/` (e.g., customizing `deployment/` files or adding project-specific logic).
- User runs `bonesdeploy push` to sync the `.bones/` folder to the remote bare repo.
- User runs `bonesdeploy deploy` to perform the actual remote release deployment.

### Primary Deploy Flow

1. `bonesdeploy deploy` SSHes into the configured host.
2. It runs `bonesremote deploy --config <remote_bones_toml>`.
3. `bonesremote deploy` orchestrates the full pipeline:
   - **doctor** — Check server environment
   - **stage_release** — Create timestamped release dir, ensure build workspace
   - **post_receive** — `git checkout -f <branch>` into `build/workspace`
   - **wire_release** — Symlink shared paths from `runtime.toml` into workspace
   - **deploy** (inner) — Run deployment scripts, copy to release, activate symlink
   - **restart_services** — `sudo bonesremote service restart --config ...`
   - **post_deploy** — Prune old releases beyond `releases.keep`
   - On failure: **drop_failed_release** — Clean up staged release

### Hook Event Order on `git push`

`pre-push -> post-receive`

1. **pre-push** (local): Runs `bonesdeploy doctor --local` if pushing to the configured bones remote and `deploy_on_push = true`. Aborts on warnings or errors.
2. Git updates refs in the bare repository.
3. **post-receive** (remote): Resolves the configured deployment ref from stdin:
   - If `deploy_on_push = false`, exits early without deploying.
   - If the configured branch wasn't pushed, or the push deleted it, exits without deploying.
   - Otherwise runs a single unified command:
     ```
     bonesremote deploy --config "$BONES_TOML" --revision <newrev>
     ```
   - This command orchestrates the full pipeline:
     - **doctor** — Check server environment
     - **stage_release** — Create timestamped release dir, ensure build workspace
     - **post_receive** — `git checkout -f <branch>` into `build/workspace`
     - **wire_release** — Symlink shared paths from `runtime.toml` into workspace
     - **deploy** (inner) — Run deployment scripts, copy to release, activate symlink
     - **restart_services** — `sudo bonesremote service restart --config ...`
     - **post_deploy** — Prune old releases beyond `releases.keep`
     - On failure: **drop_failed_release** — Clean up staged release

`bonesdeploy deploy` performs the same remote pipeline by SSHing into the host and running `bonesremote deploy --config <remote_bones_toml>` directly (without `--revision`, so it uses the configured branch). Git-triggered deploy is optional plumbing, not the primary model.

```

`docs/bonesinfra-verification.md`:

```md
# Bonesinfra Verification Concern

`bonesdeploy` currently clones `bonesinfra` from its Git repository and uses that checkout as executable deployment infrastructure. Today, that fetch trusts whatever is currently at the repository tip.

## Concern

If `bonesinfra` is fetched by branch tip alone, then the code we run during `remote setup`, `remote runtime`, or `remote ssl` is whatever the remote repository serves at that moment. That creates a supply-chain trust boundary:

- a bad commit on `bonesinfra` could be pulled and executed
- a compromised maintainer machine could sign and push unwanted changes
- a compromised hosting account could expose unwanted branch-tip contents

This matters most because some of that infrastructure runs with elevated privileges.

## Deferred direction

We discussed verifying `bonesinfra` against a shipped public GPG key.

The rough idea:

1. Sign `bonesinfra` commits with a trusted GPG key.
2. Ship the corresponding public key with `bonesdeploy`.
3. After clone or update, verify the fetched commit against that key.
4. Refuse to run unverified infrastructure.

That approach is promising, but we are deliberately **not** implementing it in the current refactor.

## Why it is deferred

- The current cleanup pass is focused on dead code, duplication, wrapper collapse, and guardrail fixes.
- GPG verification introduces release-process and key-rotation decisions that deserve focused design.
- We want a separate decision on whether to verify only the fetched tip or a broader history.

## Questions for later

- Should we verify only the fetched commit, or the full reachable history we rely on?
- How do we rotate trusted keys without breaking old `bonesdeploy` installs?
- Should we support multiple trusted keys?
- Should verification happen only on fresh clone, or on every run that touches `bonesinfra`?
- Is GPG commit verification enough, or do we also want release tags or commit pinning?

## Current status

Deferred. Track this separately from the slop refactor.

```

`docs/references/bonesinfra.md`:

```md
Project Path: bonesinfra

Source Tree:

```txt
bonesinfra
├── AGENTS.md
├── README.md
├── build.sh
├── docs
├── pyproject.toml
├── ruff.toml
├── src
│   └── bonesinfra
│       ├── __main__.py
│       ├── app
│       │   ├── apply.py
│       │   ├── runtime_apply.py
│       │   ├── runtime_catalog.py
│       │   ├── setup_apply.py
│       │   └── ssl_apply.py
│       ├── assets
│       │   ├── apparmor
│       │   │   └── project-nginx-profile.j2
│       │   └── nginx
│       │       ├── index.html.j2
│       │       ├── router.conf.j2
│       │       ├── site-nginx.conf.j2
│       │       └── site-nginx.service.j2
│       ├── cli
│       │   └── app.py
│       ├── deploys
│       │   ├── runtime
│       │   │   ├── apparmor.py
│       │   │   ├── doctor.py
│       │   │   ├── nginx.py
│       │   │   ├── packages.py
│       │   │   ├── plan.py
│       │   │   └── template_runtime.py
│       │   ├── setup
│       │   │   ├── bonesremote.py
│       │   │   ├── directories.py
│       │   │   ├── firewall.py
│       │   │   ├── packages.py
│       │   │   ├── placeholder.py
│       │   │   ├── plan.py
│       │   │   └── users.py
│       │   └── ssl
│       │       └── plan.py
│       ├── domain
│       │   ├── context.py
│       │   └── paths.py
│       ├── infra
│       │   ├── deploy_helpers.py
│       │   ├── output.py
│       │   ├── pyinfra_runner.py
│       │   ├── toml_store.py
│       │   └── utils.py
│       └── runtimes
│           ├── __init__.py
│           ├── common
│           │   ├── __init__.py
│           │   ├── apparmor.py
│           │   ├── assets
│           │   │   ├── app-profile.j2
│           │   │   ├── app-site-nginx.conf.j2
│           │   │   ├── app.service.j2
│           │   │   └── static-site-nginx.conf.j2
│           │   ├── logs.py
│           │   ├── nginx.py
│           │   ├── node.py
│           │   ├── paths.py
│           │   ├── php_fpm_pool.py
│           │   ├── python.py
│           │   ├── ruby.py
│           │   ├── service.py
│           │   └── validation.py
│           ├── django
│           │   └── django.py
│           ├── laravel
│           │   ├── __init__.py
│           │   ├── assets
│           │   │   ├── nginx
│           │   │   │   └── laravel-site-nginx.conf.j2
│           │   │   └── php
│           │   │       └── php-fpm-pool.conf.j2
│           │   ├── deploy.py
│           │   ├── metadata.py
│           │   ├── nginx.py
│           │   ├── php_fpm.py
│           │   ├── php_packages.py
│           │   └── php_repo.py
│           ├── next
│           │   └── next.py
│           ├── nuxt
│           │   └── nuxt.py
│           ├── rails
│           │   └── rails.py
│           ├── sveltekit
│           │   └── svelte.py
│           └── vue
│               └── vue.py
└── tests
    ├── __init__.py
    ├── __main__.py
    ├── cleancode
    │   ├── test_no_provably_unnecessary_fallback.py
    │   └── test_no_suspicious_fallback.py
    ├── helpers.py
    ├── test_cli.py
    ├── test_context.py
    ├── test_deploy_structure.py
    ├── test_paths.py
    ├── test_pyinfra_runner.py
    ├── test_runtime_nginx.py
    ├── test_runtimes.py
    ├── test_syntax.py
    ├── test_templates_j2.py
    └── test_tripwires.py

```

`AGENTS.md`:

```md
You are a lazy senior developer. Lazy means efficient, not careless. The best code is the code never written.

Before writing any code, stop at the first rung that holds:

1. Does this need to be built at all? (YAGNI)
2. Does the standard library already do this? Use it.
3. Does a native platform feature cover it? Use it.
4. Does an already-installed dependency solve it? Use it.
5. Can this be one line? Make it one line.
6. Only then: write the minimum code that works.

When you are done, please run `ruff check .`. Do not ignore errors or warnings.

Rules:

- No abstractions that weren't explicitly requested.
- No new dependency if it can be avoided.
- No boilerplate nobody asked for.
- Deletion over addition. Boring over clever. Fewest files possible.
- Question complex requests: "Do you actually need X, or does Y cover it?"
- Pick the edge-case-correct option when two stdlib approaches are the same size, lazy means less code, not the flimsier algorithm.
- Mark intentional simplifications with a `ponytail:` comment. If the shortcut has a known ceiling (global lock, O(n²) scan, naive heuristic), the comment names the ceiling and the upgrade path.

Not lazy about: input validation at trust boundaries, error handling that prevents data loss, security, accessibility, the calibration real hardware needs (the platform is never the spec ideal, a clock drifts, a sensor reads off), anything explicitly requested. Lazy code without its check is unfinished: non-trivial logic leaves ONE runnable check behind, the smallest thing that fails if the logic breaks (an assert-based demo/self-check or one small test file; no frameworks, no fixtures). Trivial one-liners need no test.

(Yes, this file also applies to agents working on the ponytail repo itself. Especially to them.)
```

`README.md`:

```md
# bonesinfra

Hidden Python provisioning engine for BonesDeploy.

It handles pyinfra-based setup, runtime, and SSL provisioning. BonesDeploy owns TOML creation and uses this package as the private execution layer.

## Interface

- `bonesinfra runtime list`
- `bonesinfra runtime questions <runtime>`
- `bonesinfra setup apply --config <bones.toml>`
- `bonesinfra runtime apply --config <bones.toml> --runtime-config <runtime.toml>`
- `bonesinfra ssl apply --config <bones.toml>`

## Runtime metadata

Runtime modules expose `questions()` so BonesDeploy can prompt users and write `runtime.toml` on the Rust side.

## Notes

- `bonesinfra` reads `bones.toml` and `runtime.toml`.
- It does not create those files.
- It does not own deployment scripts.

```

`build.sh`:

```sh
#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-python3}"

if command -v uv >/dev/null 2>&1; then
  exec uv run --with pyinstaller --project "$ROOT" python -m PyInstaller \
    --clean \
    --noconfirm \
    --onefile \
    --name bonesinfra \
    --paths "$ROOT/src" \
    --collect-data bonesinfra \
    --collect-submodules pyinfra \
    "$ROOT/src/bonesinfra/__main__.py"
fi

"$PYTHON" -m pip install --upgrade pyinstaller

exec "$PYTHON" -m PyInstaller \
  --clean \
  --noconfirm \
  --onefile \
  --name bonesinfra \
  --paths "$ROOT/src" \
  --collect-data bonesinfra \
  --collect-submodules pyinfra \
  "$ROOT/src/bonesinfra/__main__.py"

```

`pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=75"]
build-backend = "setuptools.build_meta"

[project]
name = "bonesinfra"
version = "0.1.0"
description = "Deployment automation for BonesDeploy"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "pyinfra>=3.8.0",
    "rich>=15.0.0",
    "typer>=0.26.7",
]

[project.scripts]
bonesinfra = "bonesinfra.__main__:main"

[tool.setuptools.package-dir]
"" = "src"

[tool.setuptools.package-data]
bonesinfra = [
    "assets/**/*.j2",
    "runtimes/**/assets/**/*.j2",
]

[dependency-groups]
dev = [
    "pytest>=9.0.3",
]

```

`ruff.toml`:

```toml
target-version = "py312"
line-length = 120

[lint]
select = [
  "E",    # pycodestyle
  "F",    # pyflakes
  "B",    # bugbear
  "I",    # import sorting
  "SIM",  # simplify
  "UP",   # pyupgrade
  "N",    # naming
  "ARG",  # unused args
  "C90",  # complexity
  "BLE",  # blind except
  "FBT",  # boolean trap
  "TRY",  # exception handling quality
  "PTH",  # pathlib preference
  "RUF",  # Ruff-specific rules
  "PL",   # pylint-derived rules
  "S",    # security-ish checks
  "D",    # docstring presence/style
  "DOC",  # docstring consistency
  "A",    # shadowing builtins
  "RET",  # return statement cleanliness
  "T20",  # print statement detection (like dbg_macro in Rust)
  "ERA",  # commented-out code detection
  "ICN",  # import conventions (numpy as np, etc.)
  "PERF", # performance anti-patterns
  "FURB", # modernize / refurbish
  "Q",    # quote consistency
  "PIE",  # misc. lints (unnecessary pass, duplicate class field keys)
  "C4",   # comprehension style
  "RSE",  # unnecessary exception parentheses
  "FA",   # future annotations
]
ignore = [
  "D",      # docstring rules (disabled by project convention)
  "TRY003", # long exception messages (sometimes necessary in CLI tools)
  "FBT001", # boolean positional arg (sometimes necessary for flags)
  "RET504", # unnecessary assignment before return (can aid readability)
  "ERA001", # commented-out code (enable once codebase is clean)
]

fixable = ["ALL"]
dummy-variable-rgx = "^_$"

[lint.mccabe]
max-complexity = 8

[lint.pylint]
max-args = 5
max-branches = 10
max-returns = 6
max-statements = 40

[lint.isort]
force-single-line = false
known-first-party = []
combine-as-imports = true

[lint.per-file-ignores]
"tests/**/*.py" = [
  "S101",   # allow assert in tests
  "D100",   # no module docstring requirement in tests
  "D101",
  "D102",
  "D103",
  "D104",
  "ARG001", # unused function args (fixtures, parametrize)
  "ARG002", # unused method args
  "PLR2004", # magic values in comparisons (fine in tests)
  "T20",    # allow print in tests
  "S102",    # exec() used in test helpers
  "S603",    # subprocess with test harness
]
"__init__.py" = ["F401", "D104"]
"conftest.py" = ["D100", "D103"]
"scripts/**/*.py" = ["T20"]
"src/bonesinfra/cli/*.py" = [
  "T20",     # CLI tool uses print for output/errors
  "PLC0415", # intentional lazy imports for CLI commands
]
"src/bonesinfra/app/*.py" = [
  "T20",     # app services print errors to stderr
]
"src/bonesinfra/infra/pyinfra_runner.py" = [
  "T20",     # print to stderr on failure
  "PLR0913", # run() takes 6 keyword args naturally
]
"src/bonesinfra/infra/deploy_helpers.py" = [
  "PLR0913", # render() wraps pyinfra template with all its args
]
"src/bonesinfra/deploys/runtime/template_runtime.py" = [
  "PLC0415", # lazy import to avoid circular dependency
  "BLE001",  # blind except on ImportError/KeyError
]
"src/bonesinfra/runtimes/__init__.py" = ["T20"]
"src/bonesinfra/runtimes/**/*.py" = [
  "PLC0415", # pyinfra imports are deferred to deploy time
]
"src/bonesinfra/deploys/setup/bonesremote.py" = [
  "S604",    # pyinfra.server.user with shell=True is standard
]
"src/bonesinfra/deploys/setup/users.py" = [
  "S604",    # pyinfra.server.user with shell=True is standard
]
"src/bonesinfra/deploys/ssl/plan.py" = [
  "A005",    # intentional module name matching project domain
  "T20",     # print to stderr on error
]

[format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
docstring-code-format = true
docstring-code-line-length = 80

```

`src/bonesinfra/__main__.py`:

```py
from bonesinfra.cli.app import app


def main():
    app()


if __name__ == "__main__":
    main()

```

`src/bonesinfra/app/apply.py`:

```py
import sys

from bonesinfra.infra.pyinfra_runner import run as run_deploy


def run_plan(deploy, ctx):
    if not ctx.host:
        print("Error: missing host in bones.toml", file=sys.stderr)
        sys.exit(3)
    run_deploy(ctx=ctx, deploy=deploy)

```

`src/bonesinfra/app/runtime_apply.py`:

```py
from bonesinfra.app.apply import run_plan
from bonesinfra.deploys.runtime.plan import deploy_runtime
from bonesinfra.domain.context import DeployContext


def apply(config_path: str, runtime_config_path: str) -> None:
    ctx = DeployContext.from_files(config_path, runtime_config_path)
    run_plan(deploy_runtime, ctx)

```

`src/bonesinfra/app/runtime_catalog.py`:

```py
from bonesinfra.runtimes import get_runtime, list_runtimes


def list_all() -> list[str]:
    return list_runtimes()


def get_questions(runtime_name: str) -> list[dict]:
    module = get_runtime(runtime_name)
    return module.questions()

```

`src/bonesinfra/app/setup_apply.py`:

```py
from bonesinfra.app.apply import run_plan
from bonesinfra.deploys.setup.plan import deploy_setup
from bonesinfra.domain.context import DeployContext


def apply(config_path: str) -> None:
    ctx = DeployContext.from_files(config_path)
    run_plan(deploy_setup, ctx)

```

`src/bonesinfra/app/ssl_apply.py`:

```py
import sys

from bonesinfra.app.apply import run_plan
from bonesinfra.deploys.ssl.plan import deploy_ssl
from bonesinfra.domain.context import DeployContext


def apply(config_path: str) -> None:
    ctx = DeployContext.from_files(config_path)
    if not ctx.host:
        print("Error: missing host in bones.toml", file=sys.stderr)
        sys.exit(3)
    if not ctx.config.domain or not ctx.config.email:
        print("Error: ssl.domain and ssl.email are required in bones.toml", file=sys.stderr)
        sys.exit(3)
    run_plan(deploy_ssl, ctx)

```

`src/bonesinfra/assets/apparmor/project-nginx-profile.j2`:

```j2
#include <tunables/global>

profile {{ apparmor_profile_name | default("bonesdeploy-" ~ project_name ~ "-nginx") }} flags=(attach_disconnected,mediate_deleted) {
  # Base runtime abstractions and libc/loader paths.
  #include <abstractions/base>

  network unix stream,

  {{ paths.bonesremote_global_link }} mr,
  {{ paths.bonesremote_global_link }} ix,
  /usr/sbin/nginx mr,
  /usr/sbin/nginx ix,

  /usr/** r,
  /bin/** r,
  /sbin/** r,
  /lib/** r,
  /lib64/** r,
  /etc/nginx/** r,
  /etc/ssl/** r,
  /etc/hosts r,
  /etc/resolv.conf r,
  /etc/nsswitch.conf r,
  /etc/passwd r,
  /etc/group r,
  /proc/** r,
  /sys/devices/system/cpu/online r,

  {{ paths.current_web_root }}/** r,
  # current is a symlink, so allow the resolved release path too.
  {{ paths.releases }}/*/{{ web_root }}/** r,
  {{ paths.repo_bones_toml }} r,
  {{ paths.site_nginx_config }} r,

  {{ paths.runtime_nginx_dir }}/ rw,
  {{ paths.runtime_nginx_dir }}/** rwk,

  # ponytail: glob grant on app sockets — per-app profiles are leaf-scoped,
  # but the per-site nginx must reach every app socket under /run/<project>/.
  # Upgrade path: enumerate explicit socket paths per runtime when runtimes
  # become dynamic.
  {{ paths.runtime_socket_dir }}/ r,
  {{ paths.runtime_socket_dir }}/*/ r,
  {{ paths.runtime_socket_dir }}/*/*.sock rw,

  # repo_path defaults to /home/{{ deploy_user }}/<project>.git, so global /home denies
  # would block bonesremote reading config and nginx config from repo-local bones files.
  deny /root/** r,
  deny /etc/ssh/** r,
}

```

`src/bonesinfra/assets/nginx/index.html.j2`:

```j2
<!doctype html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Pirata+One&display=swap" rel="stylesheet">
	<title>{{ project_name }}</title>

	<style>
		:root {
			color-scheme: light;
		}

		* {
			box-sizing: border-box;
		}

		body {
			margin: 0;
			min-height: 100vh;
			display: grid;
			place-items: center;
			background: #010302;
			font-family: "Trebuchet MS", "Segoe UI", sans-serif;
		}

		.logo {
			font-size: clamp(96px, 22vw, 200px);
			line-height: 1;
			user-select: none;
		}

		h1 {
			font-family: "Pirata One", cursive;
			font-size: 5rem;
			letter-spacing: 2px;
			color: #E8E7E2;
			text-shadow: 0 2px 5px rgba(0, 0, 0, 0.25);
			margin: 0;
			margin-top: 3rem;
		}
	</style>
</head>

<body>
	<h1>It's Working!</h1>
	<div class="logo">
		<img class="logo" style="width: 35vw;"
			src="data:image/jpg;base64,/9j//gAQTGF2YzYyLjExLjEwMAD/2wBDAAgSEhUSFRgYGBgYGB0bHR4eHh0dHR0eHh4gICAmJiYgICAeHiAgJCQmJikqKScnJicqKi0tLTY2MzM/P0FNTV3/xACYAAEAAQUBAQAAAAAAAAAAAAAABwgBBgIFBAMBAQEBAQEAAAAAAAAAAAAAAAABAgMEEAEAAgECAwIICggEBAUFAQEAAQIDBBEFITESQVFhcQaBIpETMrFScqFCssFzNWLRFIIjMzSSU/DCQ6LSFeFUJJNjgxazRPGjJeIRAQEBAAMBAQEBAQAAAAAAAAABETECEiFBUSIy/8AAEQgE5gTmAwESAAISAAMSAP/aAAwDAQACEQMRAD8AgEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAf//Z"
			alt="BonesDeploy">
		
	</div>
</body>

</html>
```

`src/bonesinfra/assets/nginx/router.conf.j2`:

```j2
server {
    listen 80;
    listen [::]:80;
    server_name {{ nginx_server_name }};

    location / {
        proxy_pass http://unix:{{ paths.runtime_nginx_socket }};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location ^~ /.well-known/acme-challenge/ {
        root {{ paths.current_web_root }};
        try_files $uri =404;
    }
}

{% if nginx_ssl_enabled %}
server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name {{ nginx_server_name }};

    ssl_certificate {{ nginx_ssl_certificate_path }};
    ssl_certificate_key {{ nginx_ssl_certificate_key_path }};

    location / {
        proxy_pass http://unix:{{ paths.runtime_nginx_socket }};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
{% endif %}

```

`src/bonesinfra/assets/nginx/site-nginx.conf.j2`:

```j2
worker_processes 1;
pid {{ paths.runtime_nginx_pid }};
error_log {{ paths.runtime_nginx_dir }}/error.log notice;

events {
    worker_connections 1024;
}

http {
    access_log {{ paths.runtime_nginx_dir }}/access.log;
    client_body_temp_path {{ paths.runtime_nginx_dir }}/client_body;
    proxy_temp_path {{ paths.runtime_nginx_dir }}/proxy;
    fastcgi_temp_path {{ paths.runtime_nginx_dir }}/fastcgi;
    uwsgi_temp_path {{ paths.runtime_nginx_dir }}/uwsgi;
    scgi_temp_path {{ paths.runtime_nginx_dir }}/scgi;

    server {
        # ponytail: socket inherits umask, typically 0666 — any local user
        # can connect directly, bypassing the system nginx router. Acceptable
        # on single-tenant deploy servers. Upgrade path: set the per-site
        # nginx group to www-data and use a 0660 socket mode directive.
        listen unix:{{ paths.runtime_nginx_socket }};
        root {{ paths.current_web_root }};
        index index.html;

        location / {
            try_files $uri $uri/ /index.html;
        }

        location ^~ /.well-known/acme-challenge/ {
            try_files $uri =404;
        }
    }
}

```

`src/bonesinfra/assets/nginx/site-nginx.service.j2`:

```j2
[Unit]
Description=Per-site nginx for {{ project_name }}
After=network.target apparmor.service
Requires=apparmor.service

[Service]
Type=simple
User={{ runtime_user }}
Group={{ runtime_group }}
SupplementaryGroups={{ release_group }}
WorkingDirectory={{ paths.current }}
# 0711: system nginx (www-data) must traverse this dir to reach the socket.
# 0750 causes 502 — www-data is not in the runtime group.
RuntimeDirectory={{ project_name }}/nginx
RuntimeDirectoryMode=0711
StandardOutput=journal
StandardError=journal

ExecStart=/usr/sbin/nginx -c {{ paths.site_nginx_config }} -g 'daemon off;'

AppArmorProfile={{ apparmor_profile_name | default("bonesdeploy-" ~ project_name ~ "-nginx") }}

NoNewPrivileges=yes
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

PrivateTmp=yes
ProtectHome=yes
ProtectSystem=strict

ReadWritePaths={{ paths.runtime_nginx_dir }}
ReadOnlyPaths={{ paths.current }} {{ paths.site_nginx_config }}

Restart=always
RestartSec=2

[Install]
WantedBy=multi-user.target

```

`src/bonesinfra/cli/app.py`:

```py
import json

import typer

from bonesinfra.app import runtime_apply, runtime_catalog, setup_apply, ssl_apply

app = typer.Typer()
runtime_app = typer.Typer()
setup_app = typer.Typer()
ssl_app = typer.Typer()
app.add_typer(runtime_app, name="runtime", help="Runtime operations")
app.add_typer(setup_app, name="setup", help="Setup operations")
app.add_typer(ssl_app, name="ssl", help="SSL operations")


@runtime_app.command("list")
def runtime_list():
    print(json.dumps(runtime_catalog.list_all()))


@runtime_app.command("questions")
def runtime_questions(
    runtime: str = typer.Argument(help="Runtime name"),
):
    print(json.dumps(runtime_catalog.get_questions(runtime)))


@runtime_app.command("apply")
def runtime_apply_cmd(
    config: str = typer.Option(..., "--config", help="Path to bones.toml"),
    runtime_config: str = typer.Option(..., "--runtime-config", help="Path to runtime.toml"),
):
    runtime_apply.apply(config, runtime_config)


@setup_app.command("apply")
def setup_apply_cmd(
    config: str = typer.Option(..., "--config", help="Path to bones.toml"),
):
    setup_apply.apply(config)


@ssl_app.command("apply")
def ssl_apply_cmd(
    config: str = typer.Option(..., "--config", help="Path to bones.toml"),
):
    ssl_apply.apply(config)

```

`src/bonesinfra/deploys/runtime/apparmor.py`:

```py
from pyinfra.operations import server, systemd

from bonesinfra.domain.context import template_data
from bonesinfra.infra.deploy_helpers import render


def setup(ctx, paths, here):
    systemd.service(
        name="Ensure apparmor service is enabled and started",
        service="apparmor",
        enabled=True,
        running=True,
        _sudo=True,
    )

    server.shell(
        name="Verify apparmor kernel enabled",
        commands=[f"cat {paths['apparmor_enabled_param']}"],
        _sudo=True,
    )

    apparmor_profile_name = f"bonesdeploy-{ctx.config.project_name}-nginx"
    apparmor_profile_path = f"/etc/apparmor.d/{apparmor_profile_name}"

    render(
        "Deploy per-project apparmor profile",
        here / "assets/apparmor/project-nginx-profile.j2",
        apparmor_profile_path,
        mode="0644",
        apparmor_profile_name=apparmor_profile_name,
        **template_data(ctx, paths=paths),
    )

    server.shell(
        name="Load updated apparmor profile",
        commands=[f"apparmor_parser -r {apparmor_profile_path}"],
        _sudo=True,
    )

    server.shell(
        name="Ensure project profile is in enforce mode",
        commands=[f"aa-enforce {apparmor_profile_path}"],
        _sudo=True,
    )

```

`src/bonesinfra/deploys/runtime/doctor.py`:

```py
from shlex import quote

from pyinfra.operations import server


def _user_env_command(user, command):
    q_user = quote(user)
    home = f"$(getent passwd {q_user} | cut -d: -f6)"
    return f"HOME={home} XDG_CONFIG_HOME={home}/.config {command}"


def run(ctx):
    server.shell(
        name="Run bonesremote doctor as deploy user",
        commands=[_user_env_command(ctx.config.deploy_user, "/usr/local/bin/bonesremote doctor")],
        _sudo=True,
        _sudo_user=ctx.config.deploy_user,
    )

```

`src/bonesinfra/deploys/runtime/nginx.py`:

```py
from pathlib import Path

from pyinfra.operations import files, server, systemd

from bonesinfra.domain.context import template_data
from bonesinfra.infra.deploy_helpers import mkdir, render


def setup(ctx, paths, here):
    # 0711: system nginx (www-data) needs traversal to reach the per-site
    # nginx socket at /run/<project>/nginx/nginx.sock. 0750 would block it.
    mkdir(
        name="Ensure socket directory exists",
        path=paths["runtime_socket_dir"],
        user=ctx.runtime.runtime_user,
        group=ctx.runtime.runtime_group,
        mode="0711",
    )

    mkdir(
        name="Ensure nginx runtime directory exists",
        path=paths["runtime_nginx_dir"],
        user=ctx.runtime.runtime_user,
        group=ctx.runtime.runtime_group,
        mode="0711",
    )

    mkdir(
        name="Ensure conf directory exists",
        path=paths["conf_root"],
        group=ctx.runtime.runtime_group,
        mode="0750",
    )

    render(
        "Deploy per-site nginx config",
        here / "assets/nginx/site-nginx.conf.j2",
        paths["site_nginx_config"],
        group=ctx.runtime.runtime_group,
        mode="0640",
        **template_data(ctx, paths=paths),
    )

    render(
        "Deploy per-site nginx systemd service",
        here / "assets/nginx/site-nginx.service.j2",
        paths["systemd_site_nginx_service"],
        mode="0644",
        **template_data(ctx, paths=paths),
    )

    systemd.daemon_reload(
        name="Reload systemd after site-nginx service change",
        _sudo=True,
    )

    nginx_server_name = ctx.config.domain or ctx.config.preview_domain
    if not nginx_server_name:
        raise ValueError("domain or preview_domain is required for nginx config")
    nginx_ssl_enabled = bool(
        ctx.runtime.runtime_data.get("ssl_cert_path")
        and ctx.runtime.runtime_data.get("ssl_key_path")
    )

    render(
        "Deploy router nginx config",
        here / "assets/nginx/router.conf.j2",
        paths["nginx_site_available"],
        mode="0644",
        nginx_server_name=nginx_server_name,
        nginx_ssl_enabled=nginx_ssl_enabled,
        nginx_ssl_certificate_path=ctx.runtime.runtime_data.get("ssl_cert_path", ""),
        nginx_ssl_certificate_key_path=ctx.runtime.runtime_data.get("ssl_key_path", ""),
        **template_data(ctx, paths=paths),
    )

    files.link(
        name="Enable router nginx site",
        path=paths["nginx_site_enabled"],
        target=paths["nginx_site_available"],
        force=True,
        _sudo=True,
    )

    files.link(
        name="Disable default nginx site",
        path=paths["nginx_default_site_enabled"],
        present=False,
        _sudo=True,
    )

    server.shell(
        name="Validate nginx configuration",
        commands=["nginx -t"],
        _sudo=True,
    )


def start_services(paths):
    systemd.service(
        name="Ensure nginx service is enabled and started",
        service="nginx",
        enabled=True,
        running=True,
        _sudo=True,
    )

    site_name = Path(paths["systemd_site_nginx_service"]).stem
    systemd.service(
        name="Ensure per-site nginx service is enabled and started",
        service=site_name,
        enabled=True,
        running=True,
        daemon_reload=True,
        _sudo=True,
    )

    # ponytail: reload only after the per-site nginx socket exists, so the
    # router never flips over to a missing upstream and briefly serves 502s.
    server.shell(
        name="Reload nginx to apply site config changes",
        commands=["systemctl reload nginx"],
        _sudo=True,
    )

```

`src/bonesinfra/deploys/runtime/packages.py`:

```py
from pyinfra.operations import apt


def install_apt(ctx):
    pkgs = ctx.runtime.runtime_data.get("runtime_apt_packages", [])
    if not pkgs:
        return
    apt.packages(
        name="Install runtime apt packages",
        packages=pkgs,
        present=True,
        update=True,
        cache_time=3600,
        _sudo=True,
    )

```

`src/bonesinfra/deploys/runtime/plan.py`:

```py
from pathlib import Path

from bonesinfra.deploys.runtime import apparmor, doctor, nginx, packages, template_runtime
from bonesinfra.domain.paths import DeploymentPaths


def deploy_runtime(ctx):
    paths = DeploymentPaths.new(
        ctx.config.project_name,
        ctx.config.repo_path,
        ctx.config.project_root,
        ctx.runtime.web_root,
    ).__dict__
    here = Path(__file__).parent.parent.parent

    packages.install_apt(ctx)
    apparmor.setup(ctx, paths, here)
    nginx.setup(ctx, paths, here)
    template_runtime.load(ctx)
    nginx.start_services(paths)
    doctor.run(ctx)

```

`src/bonesinfra/deploys/runtime/template_runtime.py`:

```py
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

`src/bonesinfra/deploys/setup/bonesremote.py`:

```py
from pyinfra.operations import server

from bonesinfra.domain.paths import BONESDEPLOY_REPO


def install():
    cargo_bin = "/root/.cargo/bin/cargo"
    server.shell(
        name="Install bonesremote binary",
        commands=[f"{cargo_bin} install --root /usr/local --git {BONESDEPLOY_REPO} bonesremote"],
        _sudo=True,
    )

    server.shell(
        name="Run bonesremote init",
        commands=["/usr/local/bin/bonesremote init"],
        _sudo=True,
    )

```

`src/bonesinfra/deploys/setup/directories.py`:

```py
from pathlib import Path
from shlex import quote

from pyinfra.operations import server

from bonesinfra.infra.deploy_helpers import mkdir


def _user_env_command(user, command):
    q_user = quote(user)
    home = f"$(getent passwd {q_user} | cut -d: -f6)"
    return f"HOME={home} XDG_CONFIG_HOME={home}/.config {command}"


def setup_repo_and_project(ctx, paths):
    mkdir(
        name="Ensure bare repo parent directory exists",
        path=paths["repo_parent"],
        user=ctx.config.deploy_user,
        group=ctx.config.deploy_user,
    )

    server.shell(
        name="Initialize bare git repo",
        commands=[_user_env_command(ctx.config.deploy_user, f"git init --bare {quote(paths['repo'])}")],
        _sudo=True,
        _sudo_user=ctx.config.deploy_user,
    )

    mkdir(
        name="Ensure bare repo bones directory exists",
        path=paths["repo_bones"],
        user=ctx.config.deploy_user,
        group=ctx.config.deploy_user,
    )

    mkdir(
        name="Ensure project root parent directory is traversable",
        path=paths["project_root_parent"],
        mode="0711",
    )

    mkdir(
        name="Ensure project root with setgid for release group",
        path=ctx.config.project_root,
        user=ctx.config.deploy_user,
        group=ctx.runtime.release_group,
        mode="2751",
    )

    mkdir(
        name="Ensure releases directory with setgid",
        path=paths["releases"],
        user=ctx.config.deploy_user,
        group=ctx.runtime.release_group,
        mode="2750",
    )

    mkdir(
        name="Ensure build directory (private to deploy user)",
        path=str(Path(ctx.config.project_root) / "build"),
        user=ctx.config.deploy_user,
        group=ctx.config.deploy_user,
        mode="0700",
    )

    mkdir(
        name="Ensure shared directory (owned by runtime user)",
        path=paths["shared"],
        user=ctx.runtime.runtime_user,
        group=ctx.runtime.runtime_group,
        mode="0711",
    )

    mkdir(
        name="Ensure placeholder release directory exists",
        path=paths["placeholder_web_root"],
        user=ctx.config.deploy_user,
        group=ctx.runtime.release_group,
        mode="0750",
    )

```

`src/bonesinfra/deploys/setup/firewall.py`:

```py
from pyinfra.operations import server


def configure(ctx):
    if not ctx.runtime.runtime_data.get("firewall_enabled", True):
        return

    ssh_port = int(ctx.runtime.runtime_data.get("ssh_port", int(ctx.config.port)))
    allowed_ports = ctx.runtime.runtime_data.get("firewall_allowed_ports", ["http", "https"])
    port_aliases = ctx.runtime.runtime_data.get("firewall_port_aliases", {"http": 80, "https": 443})
    rate_limit = ctx.runtime.runtime_data.get("firewall_ssh_rate_limit", False)
    ssh_cidrs = ctx.runtime.runtime_data.get("firewall_ssh_allowed_cidrs", [])
    manage_ssh = ctx.runtime.runtime_data.get("firewall_manage_ssh", True)

    cmds = []

    if manage_ssh:
        rule = "limit" if rate_limit else "allow"
        if not ssh_cidrs:
            cmds.append(f"ufw {rule} {ssh_port}/tcp")
        else:
            cmds.extend(f"ufw {rule} from {cidr} to any port {ssh_port} proto tcp" for cidr in ssh_cidrs)

    for port in allowed_ports:
        if port == "ssh":
            continue
        port_num = port_aliases.get(port, port)
        cmds.append(f"ufw allow {port_num}/tcp")

    incoming = ctx.runtime.runtime_data.get("firewall_default_incoming_policy", "deny")
    outgoing = ctx.runtime.runtime_data.get("firewall_default_outgoing_policy", "allow")
    cmds.append(f"ufw --force default {incoming} incoming")
    cmds.append(f"ufw --force default {outgoing} outgoing")
    cmds.append("ufw --force enable")

    server.shell(
        name="Apply UFW configuration",
        commands=cmds,
        _sudo=True,
    )

    if ctx.runtime.runtime_data.get("firewall_show_status", True):
        server.shell(
            name="Display UFW status",
            commands=["ufw status verbose"],
            _sudo=True,
        )

```

`src/bonesinfra/deploys/setup/packages.py`:

```py
from pyinfra.operations import apt

BASE_SYSTEM_PACKAGES: list[str] = [
    "build-essential",
    "ca-certificates",
    "curl",
    "git",
    "rsync",
    "sudo",
    "nginx",
    "apparmor",
    "apparmor-utils",
    "certbot",
    "ufw",
]

SUPPLEMENTARY_PACKAGES: list[str] = [
    "acl",
    "age",
    "apt-listchanges",
    "apt-transport-https",
    "automysqlbackup",
    "autossh",
    "btop",
    "borgbackup",
    "fail2ban",
    "fastfetch",
    "gnupg",
    "htop",
    "iftop",
    "inotify-tools",
    "iotop",
    "jdupes",
    "jq",
    "lsb-release",
    "lsof",
    "moreutils",
    "mutt",
    "nano",
    "neovim",
    "ncdu",
    "powerstat",
    "powertop",
    "rename",
    "sqlite3",
    "smartmontools",
    "sysbench",
    "sysstat",
    "telnet",
    "tmux",
    "tree",
    "unattended-upgrades",
    "unzip",
    "zip",
    "zsh",
]


def install_system(packages):
    apt.packages(
        name="Install setup apt packages",
        packages=packages,
        present=True,
        update=True,
        cache_time=3600,
        _sudo=True,
    )

```

`src/bonesinfra/deploys/setup/placeholder.py`:

```py
from pyinfra.operations import files

from bonesinfra.domain.context import template_data
from bonesinfra.infra.deploy_helpers import render


def seed(ctx, paths, here):
    render(
        "Seed placeholder index page",
        here / "assets/nginx/index.html.j2",
        paths["placeholder_index"],
        user=ctx.config.deploy_user,
        group=ctx.runtime.release_group,
        mode="0640",
        **template_data(ctx, paths=paths),
    )

    files.link(
        name="Point current symlink at placeholder release",
        path=paths["current"],
        target=paths["placeholder_release"],
        force=True,
        _sudo=True,
    )

```

`src/bonesinfra/deploys/setup/plan.py`:

```py
from pathlib import Path

from bonesinfra.deploys.setup import bonesremote, directories, firewall, packages, placeholder, users
from bonesinfra.deploys.setup.packages import BASE_SYSTEM_PACKAGES, SUPPLEMENTARY_PACKAGES
from bonesinfra.domain.paths import DeploymentPaths


def deploy_setup(ctx):
    paths = DeploymentPaths.new(
        ctx.config.project_name,
        ctx.config.repo_path,
        ctx.config.project_root,
        ctx.runtime.web_root,
    ).__dict__
    here = Path(__file__).parent.parent.parent
    all_pkgs = BASE_SYSTEM_PACKAGES + SUPPLEMENTARY_PACKAGES

    packages.install_system(all_pkgs)
    users.install_rust()
    users.ensure_users_and_groups(ctx)
    directories.setup_repo_and_project(ctx, paths)
    placeholder.seed(ctx, paths, here)
    firewall.configure(ctx)
    users.install_authorized_key(ctx)
    bonesremote.install()

```

`src/bonesinfra/deploys/setup/users.py`:

```py
from shlex import quote

from pyinfra import host
from pyinfra.facts.server import Users
from pyinfra.operations import server


def install_rust():
    server.shell(
        name="Install rustup and cargo",
        commands=["curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal"],
        _sudo=True,
    )


def _ensure_group_membership(user, group):
    q_user = quote(user)
    q_group = quote(group)
    server.shell(
        name=f"Ensure {user} is a member of {group}",
        commands=[f"id -nG {q_user} | tr ' ' '\\n' | grep -Fxq {q_group} || gpasswd -a {q_user} {q_group}"],
        _sudo=True,
    )


def ensure_users_and_groups(ctx):
    server.user(
        name="Ensure deploy user exists",
        user=ctx.config.deploy_user,
        shell="/bin/bash",
        ensure_home=True,
        _sudo=True,
    )

    server.group(
        name="Ensure runtime group exists",
        group=ctx.runtime.runtime_group,
        _sudo=True,
    )

    server.group(
        name="Ensure release-read group exists",
        group=ctx.runtime.release_group,
        _sudo=True,
    )

    existing_user = host.get_fact(Users).get(ctx.runtime.runtime_user)

    if existing_user is None:
        server.user(
            name="Ensure runtime user exists with groups",
            user=ctx.runtime.runtime_user,
            system=True,
            home="/nonexistent",
            shell="/usr/sbin/nologin",
            create_home=False,
            groups=[ctx.runtime.runtime_group, ctx.runtime.release_group],
            _sudo=True,
        )
        return

    required_groups = []
    for group in (ctx.runtime.runtime_group, ctx.runtime.release_group):
        if group not in required_groups:
            required_groups.append(group)

    for group in required_groups:
        if group != existing_user["group"] and group not in existing_user["groups"]:
            _ensure_group_membership(ctx.runtime.runtime_user, group)


def install_authorized_key(ctx):
    deploy_user = ctx.config.deploy_user
    ssh_user = ctx.config.ssh_user
    server.shell(
        name=f"Copy {ssh_user} SSH key to deploy user {deploy_user}",
        commands=[
            f"install -d -o {deploy_user} -g {deploy_user} -m 0700 /home/{deploy_user}/.ssh",
            (
                f'src=$(eval echo ~{ssh_user}/.ssh/authorized_keys); '
                f'[ -f "$src" ] || {{ echo "ERROR: $src not found" >&2; exit 1; }}; '
                f'cp "$src" /home/{deploy_user}/.ssh/authorized_keys'
            ),
            f"chown {deploy_user}:{deploy_user} /home/{deploy_user}/.ssh/authorized_keys",
            f"chmod 0600 /home/{deploy_user}/.ssh/authorized_keys",
        ],
        _sudo=True,
    )

```

`src/bonesinfra/deploys/ssl/plan.py`:

```py
import sys
from pathlib import Path

from pyinfra.operations import server, systemd

from bonesinfra.domain.context import template_data
from bonesinfra.domain.paths import DeploymentPaths
from bonesinfra.infra.deploy_helpers import render


def deploy_ssl(ctx):
    paths = DeploymentPaths.new(
        ctx.config.project_name,
        ctx.config.repo_path,
        ctx.config.project_root,
        ctx.runtime.web_root,
    ).__dict__
    here = Path(__file__).parent.parent.parent

    if not ctx.config.domain or not ctx.config.email:
        print("Error: ssl_domain and ssl_email are required", file=sys.stderr)
        sys.exit(1)

    _render_router_config(ctx, paths, here, ssl_enabled=False, stage="certbot challenge")
    obtain_certificate(ctx, paths)
    _render_router_config(ctx, paths, here, ssl_enabled=True, stage="SSL enable")


def _render_router_config(ctx, paths, here, ssl_enabled, stage):
    nginx_server_name = ctx.config.domain
    if not nginx_server_name:
        raise ValueError("domain is required for ssl nginx config")

    render(
        f"Render nginx config ({stage})",
        here / "assets/nginx/router.conf.j2",
        paths["nginx_site_available"],
        mode="0644",
        nginx_server_name=nginx_server_name,
        nginx_ssl_enabled=ssl_enabled,
        **template_data(ctx, paths=paths),
    )

    server.shell(
        name=f"Validate nginx configuration ({stage})",
        commands=["nginx -t"],
        _sudo=True,
    )

    systemd.service(
        name=f"Reload nginx ({stage})",
        service="nginx",
        reloaded=True,
        _sudo=True,
    )


def obtain_certificate(ctx, paths):
    server.shell(
        name="Obtain or renew certificate",
        commands=[
            "certbot certonly --non-interactive --agree-tos "
            f"--email {ctx.config.email} "
            "--webroot "
            f"-w {paths['current_web_root']} "
            f"-d {ctx.config.domain} "
            "--keep-until-expiring"
        ],
        _sudo=True,
    )

```

`src/bonesinfra/domain/context.py`:

```py
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from bonesinfra.domain.paths import DeploymentPaths
from bonesinfra.infra.toml_store import load_toml

DEPLOY_USER = "git"

DEFAULT_SSH_USER = "root"
DEFAULT_SSH_PORT = "22"
DEFAULT_WEB_ROOT = "public"


@dataclass
class DeployContext:
    config: BonesConfig
    runtime: RuntimeConfig

    @classmethod
    def from_files(
        cls,
        config_path: str,
        runtime_config_path: str | None = None,
    ) -> DeployContext:
        bones_cfg = load_toml(config_path)
        project_name = bones_cfg.get("project_name", "")
        repo_path = bones_cfg.get("repo_path", "")
        project_root = bones_cfg.get("project_root", "")
        host = bones_cfg.get("host", "")
        port = int(bones_cfg.get("port", DEFAULT_SSH_PORT))

        runtime_cfg = {}
        if runtime_config_path:
            rpath = Path(runtime_config_path)
            if rpath.exists():
                runtime_cfg = load_toml(str(rpath))

        config = BonesConfig(
            remote_name=bones_cfg.get("remote_name", ""),
            project_name=project_name,
            ssh_user=bones_cfg.get("ssh_user", DEFAULT_SSH_USER),
            host=host,
            port=str(port),
            repo_path=repo_path,
            project_root=project_root,
            branch=bones_cfg.get("branch", ""),
            preview_domain=bones_cfg.get("preview_domain", ""),
            releases_keep=int(bones_cfg.get("releases_keep", 5)),
            ssl_enabled=bones_cfg.get("ssl_enabled", False),
            domain=bones_cfg.get("domain", ""),
            email=bones_cfg.get("email", ""),
            deploy_user=DEPLOY_USER,
        )

        runtime = RuntimeConfig(
            web_root=runtime_cfg.get("web_root", DEFAULT_WEB_ROOT),
            runtime_user=runtime_cfg.get("runtime_user", project_name),
            runtime_group=runtime_cfg.get("runtime_group", project_name),
            release_group=runtime_cfg.get("release_group", f"{project_name}-release"),
            runtime_data=runtime_cfg,
        )

        return cls(config=config, runtime=runtime)

    @property
    def host(self) -> str:
        return self.config.host

    @property
    def ssh_port(self) -> int:
        return int(self.config.port)


def template_data(ctx: DeployContext, *, paths: dict[str, Any] | None = None, **extra: Any) -> dict[str, Any]:
    """Build flat template context from DeployContext for Jinja2 template rendering."""
    if paths is None:
        p = DeploymentPaths.new(
            ctx.config.project_name, ctx.config.repo_path, ctx.config.project_root, ctx.runtime.web_root
        )
        paths = p.__dict__

    data: dict[str, Any] = {}
    data["project_name"] = ctx.config.project_name
    data["project_root"] = ctx.config.project_root
    data["web_root"] = ctx.runtime.web_root
    data["repo_path"] = ctx.config.repo_path
    data["deploy_user"] = ctx.config.deploy_user
    data["runtime_user"] = ctx.runtime.runtime_user
    data["runtime_group"] = ctx.runtime.runtime_group
    data["release_group"] = ctx.runtime.release_group
    data["project_root_parent"] = paths.get("project_root_parent", "")
    data["ssh_port"] = int(ctx.config.port)
    data["paths"] = paths
    data["ssl_domain"] = ctx.config.domain
    data["ssl_email"] = ctx.config.email
    data["preview_domain"] = ctx.config.preview_domain

    for key, value in ctx.runtime.runtime_data.items():
        if key not in data:
            data[key] = value

    data.update(extra)
    return data


@dataclass
class BonesConfig:
    remote_name: str
    project_name: str
    ssh_user: str
    host: str
    port: str
    repo_path: str
    project_root: str
    branch: str
    preview_domain: str
    releases_keep: int
    ssl_enabled: bool
    domain: str
    email: str
    deploy_user: str


@dataclass
class RuntimeConfig:
    web_root: str
    runtime_user: str
    runtime_group: str
    release_group: str
    runtime_data: dict[str, Any] = field(default_factory=dict)

```

`src/bonesinfra/domain/paths.py`:

```py
from dataclasses import dataclass
from pathlib import Path

DEFAULT_REPO_PARENT = "/home/git"
DEFAULT_PROJECT_ROOT_PARENT = "/srv/sites"
DEFAULT_CONF_ROOT_PARENT = "/srv/conf"
DEFAULT_WEB_ROOT = "public"

ETC_NGINX_SITES_AVAILABLE = "/etc/nginx/sites-available"
ETC_NGINX_SITES_ENABLED = "/etc/nginx/sites-enabled"
ETC_SYSTEMD_SYSTEM = "/etc/systemd/system"
ETC_APPARMOR_D = "/etc/apparmor.d"
ETC_SUDOERS_D = "/etc/sudoers.d"

RUNTIME_SOCKET_PARENT = "/run"
BONES_DIR = "bones"
BONES_TOML = "bones.toml"
NGINX_CONF = "nginx.conf"
INDEX_HTML = "index.html"
GIT_HEAD = "HEAD"
RELEASES_DIR = "releases"
SHARED_DIR = "shared"
BUILD_DIR = "build"
WORKSPACE_DIR = "workspace"
LOGS_DIR = "logs"
CURRENT_LINK = "current"
PLACEHOLDER_RELEASE_NAME = "19700101_000000"

NGINX_SOCKET = "nginx.sock"
NGINX_PID = "nginx.pid"
PHP_FPM_SOCKET = "php-fpm.sock"
DEFAULT_NGINX_SITE = "default"

BONESDEPLOY_BINARY = "bonesdeploy"
BONESREMOTE_BINARY = "bonesremote"

USR_LOCAL_BIN = "/usr/local/bin"
APPARMOR_ENABLED_PARAM = "/sys/module/apparmor/parameters/enabled"
APPARMOR_PROFILES = "/sys/kernel/security/apparmor/profiles"

BONESDEPLOY_REPO = "https://github.com/AlextheYounga/bonesdeploy.git"


def _parent_or_default(path: str, fallback: str) -> str:
    parent = Path(path).parent
    if parent and str(parent) != ".":
        return str(parent)
    return fallback


@dataclass
class DeploymentPaths:
    repo: str
    repo_parent: str
    repo_head: str
    repo_bones: str
    repo_bones_toml: str
    site_nginx_config: str
    conf_root: str
    project_root: str
    project_root_parent: str
    releases: str
    shared: str
    build_root: str
    build_logs: str
    current: str
    current_web_root: str
    placeholder_release: str
    placeholder_web_root: str
    placeholder_index: str
    nginx_site_available: str
    nginx_site_enabled: str
    nginx_default_site_enabled: str
    systemd_site_nginx_service: str
    apparmor_profile_path: str
    runtime_socket_dir: str
    runtime_nginx_dir: str
    runtime_nginx_socket: str
    runtime_nginx_pid: str
    runtime_php_fpm_socket: str
    sudoers_path: str
    usr_local_bin: str
    bonesremote_global_link: str
    apparmor_enabled_param: str
    apparmor_profiles: str

    @classmethod
    def new(
        cls,
        project_name: str,
        repo_path: str,
        project_root: str,
        web_root: str | None = None,
    ) -> "DeploymentPaths":
        if web_root is None:
            web_root = DEFAULT_WEB_ROOT

        placeholder_release = Path(project_root) / RELEASES_DIR / PLACEHOLDER_RELEASE_NAME
        current = Path(project_root) / CURRENT_LINK
        runtime_socket_dir = Path(RUNTIME_SOCKET_PARENT) / project_name
        runtime_nginx_dir = runtime_socket_dir / "nginx"
        repo_bones = Path(repo_path) / BONES_DIR
        conf_root = Path(DEFAULT_CONF_ROOT_PARENT) / project_name

        return cls(
            repo=repo_path,
            repo_parent=_parent_or_default(repo_path, DEFAULT_REPO_PARENT),
            repo_head=str(Path(repo_path) / GIT_HEAD),
            repo_bones=str(repo_bones),
            repo_bones_toml=str(repo_bones / BONES_TOML),
            site_nginx_config=str(conf_root / NGINX_CONF),
            conf_root=str(conf_root),
            project_root=project_root,
            project_root_parent=_parent_or_default(project_root, DEFAULT_PROJECT_ROOT_PARENT),
            releases=str(Path(project_root) / RELEASES_DIR),
            shared=str(Path(project_root) / SHARED_DIR),
            build_root=str(Path(project_root) / BUILD_DIR / WORKSPACE_DIR),
            build_logs=str(Path(project_root) / BUILD_DIR / LOGS_DIR),
            current=str(current),
            current_web_root=str(current / web_root),
            placeholder_release=str(placeholder_release),
            placeholder_web_root=str(placeholder_release / web_root),
            placeholder_index=str(placeholder_release / web_root / INDEX_HTML),
            nginx_site_available=str(Path(ETC_NGINX_SITES_AVAILABLE) / f"{project_name}.conf"),
            nginx_site_enabled=str(Path(ETC_NGINX_SITES_ENABLED) / f"{project_name}.conf"),
            nginx_default_site_enabled=str(Path(ETC_NGINX_SITES_ENABLED) / DEFAULT_NGINX_SITE),
            systemd_site_nginx_service=str(Path(ETC_SYSTEMD_SYSTEM) / f"{project_name}-nginx.service"),
            apparmor_profile_path=str(Path(ETC_APPARMOR_D) / f"bonesdeploy-{project_name}-nginx"),
            runtime_socket_dir=str(runtime_socket_dir),
            runtime_nginx_dir=str(runtime_nginx_dir),
            runtime_nginx_socket=str(runtime_nginx_dir / NGINX_SOCKET),
            runtime_nginx_pid=str(runtime_nginx_dir / NGINX_PID),
            runtime_php_fpm_socket=str(runtime_socket_dir / PHP_FPM_SOCKET),
            sudoers_path=str(Path(ETC_SUDOERS_D) / "bonesdeploy"),
            usr_local_bin=USR_LOCAL_BIN,
            bonesremote_global_link=str(Path(USR_LOCAL_BIN) / BONESREMOTE_BINARY),
            apparmor_enabled_param=APPARMOR_ENABLED_PARAM,
            apparmor_profiles=APPARMOR_PROFILES,
        )

```

`src/bonesinfra/infra/deploy_helpers.py`:

```py
from pyinfra.operations import files


def mkdir(name, path, user="root", group="root", mode="0755"):
    files.directory(
        name=name,
        path=path,
        user=user,
        group=group,
        mode=mode,
        _sudo=True,
    )


def render(name, src, dest, user="root", group="root", mode="0644", **data):
    files.template(
        name=name,
        src=str(src),
        dest=dest,
        user=user,
        group=group,
        mode=mode,
        **data,
        _sudo=True,
    )

```

`src/bonesinfra/infra/output.py`:

```py
from __future__ import annotations

import logging
import os
from collections.abc import Iterator
from contextlib import contextmanager

from pyinfra.api.output import set_echo, set_formatter
from pyinfra.api.state import BaseStateCallback, State
from rich.console import Console
from rich.markup import escape
from rich.panel import Panel
from rich.status import Status
from rich.table import Table
from rich.text import Text

console = Console(stderr=True)
_err = Console(stderr=True)

_STATUS_STYLES = {
    "Success": "bold green",
    "No changes": "cyan",
    "Failure": "bold red",
}


class _PyinfraLogHandler(logging.Handler):
    def emit(self, record):
        console.print(self.format(record), markup=True, highlight=False)


class BonesDeployCallback(BaseStateCallback):
    _status: Status | None = None

    @classmethod
    def _stop_status(cls) -> None:
        if cls._status is not None:
            cls._status.stop()
            cls._status = None

    @staticmethod
    def operation_start(state: State, op_hash: str) -> None:
        BonesDeployCallback._stop_status()
        op_meta = state.get_op_meta(op_hash)
        op_name = ", ".join(op_meta.names) or "Operation"
        BonesDeployCallback._status = console.status(
            f"[bold cyan]☠[/]  Running operation: [bold]{escape(op_name)}[/]",
            spinner="dots",
        )
        BonesDeployCallback._status.start()

    @staticmethod
    def operation_end(state: State, op_hash: str) -> None:
        BonesDeployCallback._stop_status()
        op_meta = state.get_op_meta(op_hash)
        op_name = ", ".join(op_meta.names) or "Operation"
        status = "No changes"

        for host in state.inventory:
            try:
                op_data = state.get_op_data_for_host(host, op_hash)
            except KeyError:
                continue

            operation_meta = op_data.operation_meta
            if not operation_meta.is_complete() or operation_meta.did_error():
                status = "Failure"
                break

            if operation_meta.did_change():
                status = "Success"

        status_style = _STATUS_STYLES.get(status, "dim")
        console.print(f"☠  {op_name}", end=" ")
        console.print(f"[{status_style}]{status}[/{status_style}]")


def setup_output() -> None:
    os.environ["PYINFRA_PROGRESS"] = "off"

    def bones_echo(message=None, **kwargs):
        del kwargs
        if message is not None:
            _err.print(message, markup=True, highlight=False)

    def bones_format(text, *args, **kwargs):
        fg = args[0] if args else kwargs.get("fg")
        styles = []
        if kwargs.get("bold"):
            styles.append("bold")
        if fg:
            styles.append(str(fg))

        text = escape(str(text))
        if not styles:
            return text
        return f"[{' '.join(styles)}]{text}[/]"

    set_echo(bones_echo)
    set_formatter(bones_format)

    pyinfra_logger = logging.getLogger("pyinfra")
    pyinfra_logger.handlers.clear()
    handler = _PyinfraLogHandler()
    handler.setFormatter(logging.Formatter("%(message)s"))
    handler.setLevel(logging.WARNING)
    pyinfra_logger.addHandler(handler)
    pyinfra_logger.setLevel(logging.WARNING)
    pyinfra_logger.propagate = False


def print_banner() -> None:
    console.print()
    title = Text("☠  bonesdeploy", style="bold cyan")
    console.print(Panel(title, border_style="cyan"))


def print_target(hostname: str, user: str) -> None:
    info = Table.grid(padding=(0, 1))
    info.add_column(style="dim")
    info.add_column(style="bold yellow")
    info.add_row("target:", f"{user}@{hostname}")
    console.print(info)
    console.print()


def print_connected() -> None:
    console.print("☠  [bold cyan]connected[/]")
    console.print()


def stop_live_output() -> None:
    BonesDeployCallback._stop_status()


def print_done(success: bool) -> None:
    console.print()
    if success:
        console.print("☠  [bold green]deploy complete[/]")
    else:
        console.print("☠  [bold red]deploy failed[/]")
    console.print()


@contextmanager
def activity(message: str) -> Iterator[None]:
    with console.status(f"[bold cyan]☠ bonesdeploy[/] {message}", spinner="dots"):
        yield

```

`src/bonesinfra/infra/pyinfra_runner.py`:

```py
from __future__ import annotations

import sys
from collections.abc import Callable

from pyinfra.api import Config, Inventory, State
from pyinfra.api.connect import connect_all
from pyinfra.api.exceptions import PyinfraError
from pyinfra.api.operations import run_ops
from pyinfra.context import ctx_config, ctx_host, ctx_inventory, ctx_state

from bonesinfra.domain.context import DeployContext
from bonesinfra.infra.output import (
    BonesDeployCallback,
    activity,
    print_banner,
    print_connected,
    print_done,
    print_target,
    setup_output,
    stop_live_output,
)


def run(
    *,
    ctx: DeployContext,
    ssh_key: str | None = None,
    deploy: Callable[[DeployContext], None],
) -> None:
    setup_output()

    hostname = ctx.config.host
    ssh_user = ctx.config.ssh_user
    ssh_port = int(ctx.config.port)

    host_data: dict[str, object] = {
        "ssh_user": ssh_user,
        "ssh_port": ssh_port,
    }
    if ssh_key:
        host_data["ssh_key"] = ssh_key

    config = Config()

    inventory = Inventory(([(hostname, host_data)], {}))
    state = State(inventory, config)
    target_host = next(iter(inventory))

    print_banner()
    print_target(hostname, ssh_user)

    try:
        with activity("connecting"):
            connect_all(state)
    except PyinfraError:
        print_done(success=False)
        sys.exit(1)

    print_connected()

    with (
        ctx_state.use(state),
        ctx_config.use(config),
        ctx_inventory.use(inventory),
        ctx_host.use(target_host),
        activity("planning deploy operations"),
    ):
        deploy(ctx)

    state.add_callback_handler(BonesDeployCallback())

    try:
        run_ops(state)
    except PyinfraError:
        stop_live_output()
        print_done(success=False)
        sys.exit(1)

    if state.failed_hosts:
        stop_live_output()
        print_done(success=False)
        sys.exit(1)

    stop_live_output()
    print_done(success=True)

```

`src/bonesinfra/infra/toml_store.py`:

```py
import tomllib
from pathlib import Path
from typing import Any


def load_toml(path: str) -> dict[str, Any]:
    with Path(path).open("rb") as file:
        return tomllib.load(file)


def load_runtime_config(deploy_file: str) -> dict[str, Any]:
    return load_toml(str(Path(deploy_file).parent / "runtime.toml"))

```

`src/bonesinfra/infra/utils.py`:

```py
from collections.abc import Mapping
from typing import Any


def unflatten(data_dict: Mapping[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in data_dict.items():
        parts = key.split(".")
        node = result
        for part in parts[:-1]:
            if part not in node:
                node[part] = {}
            node = node[part]
        node[parts[-1]] = value
    return result

```

`src/bonesinfra/runtimes/__init__.py`:

```py
import sys

from bonesinfra.runtimes import laravel
from bonesinfra.runtimes.django import django
from bonesinfra.runtimes.next import next as next_runtime
from bonesinfra.runtimes.nuxt import nuxt
from bonesinfra.runtimes.rails import rails
from bonesinfra.runtimes.sveltekit import svelte
from bonesinfra.runtimes.vue import vue

RUNTIMES = {
    "laravel": laravel,
    "django": django,
    "next": next_runtime,
    "nuxt": nuxt,
    "rails": rails,
    "sveltekit": svelte,
    "vue": vue,
}


def list_runtimes():
    return sorted(RUNTIMES.keys())


def get_runtime(name):
    module = RUNTIMES.get(name)
    if module is None:
        print(f"Unknown runtime: {name}. Available: {', '.join(list_runtimes())}", file=sys.stderr)
        sys.exit(1)
    return module

```

`src/bonesinfra/runtimes/common/__init__.py`:

```py
from bonesinfra.runtimes.common import apparmor, logs, nginx, node, paths, python, ruby, service, validation

__all__ = ["apparmor", "logs", "nginx", "node", "paths", "python", "ruby", "service", "validation"]

```

`src/bonesinfra/runtimes/common/apparmor.py`:

```py
from pathlib import Path

from pyinfra.operations import files, server

from bonesinfra.domain.context import template_data


def render_app_profile(  # noqa: PLR0913
    ctx,
    *,
    paths,
    runtime,
    apparmor_exec_paths,
    apparmor_writable_paths,
    apparmor_network="network unix stream,",
):
    here = Path(__file__).parent
    profile_name = f"bonesdeploy-{ctx.config.project_name}-{runtime}"
    profile_path = f"/etc/apparmor.d/{profile_name}"
    files.template(
        name=f"Deploy {runtime} AppArmor profile",
        src=str(here / "assets/app-profile.j2"),
        dest=profile_path,
        user="root",
        group="root",
        mode="0644",
        apparmor_profile_name=profile_name,
        apparmor_runtime=runtime,
        apparmor_exec_paths=apparmor_exec_paths,
        apparmor_writable_paths=apparmor_writable_paths,
        apparmor_network=apparmor_network,
        **template_data(ctx, paths=paths),
        _sudo=True,
    )
    server.shell(
        name=f"Load {runtime} AppArmor profile",
        commands=[f"apparmor_parser -r -T -W {profile_path}"],
        _sudo=True,
    )
    server.shell(
        name=f"Enforce {runtime} AppArmor profile",
        commands=[f"aa-enforce {profile_name}"],
        _sudo=True,
    )
    return profile_name

```

`src/bonesinfra/runtimes/common/assets/app-profile.j2`:

```j2
#include <tunables/global>

profile {{ apparmor_profile_name }} flags=(attach_disconnected,mediate_deleted) {
  #include <abstractions/base>

  {{ apparmor_network | default("network unix stream,") }}

{% for exec_path in apparmor_exec_paths %}
  {{ exec_path }} mrix,
{% endfor %}

  /usr/** r,
  /bin/** r,
  /sbin/** r,
  /lib/** r,
  /lib64/** r,
  /etc/** r,
  /proc/** r,
  /sys/devices/system/cpu/online r,

  {{ paths.current }}/** r,
{% for write_path in apparmor_writable_paths %}
  {{ write_path }}/ rw,
  {{ write_path }}/** rwk,
{% endfor %}

  {{ paths.runtime_socket_dir }}/{{ apparmor_runtime }}/ rw,
  {{ paths.runtime_socket_dir }}/{{ apparmor_runtime }}/** rwk,

  /var/log/bonesdeploy/{{ project_name }}/ rw,
  /var/log/bonesdeploy/{{ project_name }}/** rwk,

  deny /root/** r,
  deny /etc/ssh/** r,
}

```

`src/bonesinfra/runtimes/common/assets/app-site-nginx.conf.j2`:

```j2
worker_processes 1;
pid {{ paths.runtime_nginx_pid }};
error_log {{ paths.runtime_nginx_dir }}/error.log notice;

events {
    worker_connections 1024;
}

http {
    access_log {{ paths.runtime_nginx_dir }}/access.log;
    client_body_temp_path {{ paths.runtime_nginx_dir }}/client_body;
    proxy_temp_path {{ paths.runtime_nginx_dir }}/proxy;
    fastcgi_temp_path {{ paths.runtime_nginx_dir }}/fastcgi;
    uwsgi_temp_path {{ paths.runtime_nginx_dir }}/uwsgi;
    scgi_temp_path {{ paths.runtime_nginx_dir }}/scgi;

    server {
        listen unix:{{ paths.runtime_nginx_socket }};
        root {{ paths.current_web_root }};

        location / {
            proxy_pass {{ app_proxy_target }};
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-Forwarded-Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_http_version 1.1;
            proxy_set_header Connection "";
        }

        location ^~ /.well-known/acme-challenge/ {
            try_files $uri =404;
        }
    }
}

```

`src/bonesinfra/runtimes/common/assets/app.service.j2`:

```j2
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
RuntimeDirectory={{ project_name }}/{{ runtime_name }}
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
RestrictAddressFamilies={{ runtime_address_families | default("AF_UNIX") }}

ReadOnlyPaths={{ paths.current }}
ReadWritePaths={{ paths.runtime_socket_dir }}/{{ runtime_name }} {{ runtime_write_paths }} /var/log/bonesdeploy/{{ project_name }}

StandardOutput=journal
StandardError=journal
Restart=always
RestartSec=2

[Install]
WantedBy=multi-user.target

```

`src/bonesinfra/runtimes/common/assets/static-site-nginx.conf.j2`:

```j2
worker_processes 1;
pid {{ paths.runtime_nginx_pid }};
error_log {{ paths.runtime_nginx_dir }}/error.log notice;

events {
    worker_connections 1024;
}

http {
    access_log {{ paths.runtime_nginx_dir }}/access.log;
    client_body_temp_path {{ paths.runtime_nginx_dir }}/client_body;
    proxy_temp_path {{ paths.runtime_nginx_dir }}/proxy;
    fastcgi_temp_path {{ paths.runtime_nginx_dir }}/fastcgi;
    uwsgi_temp_path {{ paths.runtime_nginx_dir }}/uwsgi;
    scgi_temp_path {{ paths.runtime_nginx_dir }}/scgi;

    server {
        listen unix:{{ paths.runtime_nginx_socket }};
        root {{ paths.current }}/dist;
        index index.html;

        location / {
            try_files $uri $uri/ /index.html;
        }

        location ^~ /.well-known/acme-challenge/ {
            try_files $uri =404;
        }
    }
}

```

`src/bonesinfra/runtimes/common/logs.py`:

```py
from pyinfra.operations import files

BONESDEPLOY_LOG_ROOT = "/var/log/bonesdeploy"


def ensure(ctx):
    """Provision /var/log/bonesdeploy and /var/log/bonesdeploy/<project>.

    The root is root-owned; the per-project dir is owned by the runtime user
    so the service (and validation) can write logs without root.
    """
    files.directory(
        name="Ensure BonesDeploy log root exists",
        path=BONESDEPLOY_LOG_ROOT,
        user="root",
        group="root",
        mode="0755",
        _sudo=True,
    )

    files.directory(
        name="Ensure per-project log directory exists",
        path=f"{BONESDEPLOY_LOG_ROOT}/{ctx.config.project_name}",
        user=ctx.runtime.runtime_user,
        group=ctx.runtime.runtime_group,
        mode="0750",
        _sudo=True,
    )

```

`src/bonesinfra/runtimes/common/nginx.py`:

```py
from pathlib import Path

from pyinfra.operations import files, server

from bonesinfra.domain.context import template_data


def _ensure_runtime_socket_dir(ctx, paths):
    # 0711: system nginx (www-data) must traverse to reach per-site sockets.
    files.directory(
        name="Ensure runtime socket directory exists before nginx validation",
        path=paths["runtime_socket_dir"],
        user=ctx.runtime.runtime_user,
        group=ctx.runtime.runtime_group,
        mode="0711",
        _sudo=True,
    )
    files.directory(
        name="Ensure nginx runtime directory exists before nginx validation",
        path=paths["runtime_nginx_dir"],
        user=ctx.runtime.runtime_user,
        group=ctx.runtime.runtime_group,
        mode="0711",
        _sudo=True,
    )


def render_proxy(ctx, *, paths, socket_path=None, port=None):
    here = Path(__file__).parent
    app_proxy_target = f"http://unix:{socket_path}:" if socket_path else f"http://127.0.0.1:{port}"
    files.template(
        name="Deploy per-site app nginx config",
        src=str(here / "assets/app-site-nginx.conf.j2"),
        dest=paths["site_nginx_config"],
        user="root",
        group=ctx.runtime.runtime_group,
        mode="0640",
        app_proxy_target=app_proxy_target,
        **template_data(ctx, paths=paths),
        _sudo=True,
    )
    _ensure_runtime_socket_dir(ctx, paths)
    server.shell(
        name="Validate nginx configuration with app config",
        commands=[f"nginx -t -c {paths['site_nginx_config']}"],
        _sudo=True,
    )


def render_static(ctx, *, paths):
    here = Path(__file__).parent
    files.template(
        name="Deploy per-site static nginx config",
        src=str(here / "assets/static-site-nginx.conf.j2"),
        dest=paths["site_nginx_config"],
        user="root",
        group=ctx.runtime.runtime_group,
        mode="0640",
        **template_data(ctx, paths=paths),
        _sudo=True,
    )
    _ensure_runtime_socket_dir(ctx, paths)
    server.shell(
        name="Validate nginx configuration with static config",
        commands=[f"nginx -t -c {paths['site_nginx_config']}"],
        _sudo=True,
    )

```

`src/bonesinfra/runtimes/common/node.py`:

```py
from pyinfra.operations import apt

NODE_PACKAGES = ["nodejs", "npm"]


def install_packages():
    apt.packages(
        name="Install Node.js runtime packages",
        packages=NODE_PACKAGES,
        present=True,
        update=True,
        _sudo=True,
    )

```

`src/bonesinfra/runtimes/common/paths.py`:

```py
from pyinfra.operations import files

from bonesinfra.domain.paths import RUNTIME_SOCKET_PARENT


def ensure_runtime_dirs(ctx):
    """Create /run/<project> as the runtime user before validation or service start.

    RuntimeDirectory= in the systemd unit also does this at start time, but
    validation runs before start, so we provision it here too.
    """
    # 0711: system nginx (www-data) must traverse /run/<project>/ to reach
    # the per-site nginx socket. 0750 would cause 502 on every public request.
    project = ctx.config.project_name
    files.directory(
        name="Ensure runtime socket directory exists",
        path=f"{RUNTIME_SOCKET_PARENT}/{project}",
        user=ctx.runtime.runtime_user,
        group=ctx.runtime.runtime_group,
        mode="0711",
        _sudo=True,
    )

```

`src/bonesinfra/runtimes/common/php_fpm_pool.py`:

```py
from pyinfra.operations import files, server, systemd

from bonesinfra.domain.context import template_data
from bonesinfra.runtimes.common import logs

PHP_FPM_SOCKET_PARENT = "/run/php"


def socket_path(project, php_version):
    return f"{PHP_FPM_SOCKET_PARENT}/php{php_version}-fpm-{project}.sock"


def pool_config_path(project, php_version):
    return f"/etc/php/{php_version}/fpm/pool.d/{project}.conf"


def ensure_log_dir(ctx):
    logs.ensure(ctx)


def render_pool(ctx, *, here, paths, php_version):
    project = ctx.config.project_name
    files.template(
        name="Deploy Laravel PHP-FPM pool config",
        src=str(here / "assets/php/php-fpm-pool.conf.j2"),
        dest=pool_config_path(project, php_version),
        user="root",
        group="root",
        mode="0644",
        laravel_php_fpm_pool_name=project,
        laravel_php_fpm_socket_path=socket_path(project, php_version),
        **template_data(ctx, paths=paths),
        _sudo=True,
    )


def validate_php_fpm(php_version):
    server.shell(
        name="Validate PHP-FPM configuration",
        commands=[f"php-fpm{php_version} --test"],
        _sudo=True,
    )


def reload_php_fpm(php_version):
    # ponytail: reload may fail on a fresh install where the unit is inactive,
    # so we restart (always valid) rather than `systemctl reload`. Upgrade path
    # is a dedicated "ensure active then reload" sequence once first-boot is
    # handled out of band.
    systemd.service(
        name="Enable and restart PHP-FPM service",
        service=f"php{php_version}-fpm",
        enabled=True,
        running=True,
        restarted=True,
        _sudo=True,
    )

```

`src/bonesinfra/runtimes/common/python.py`:

```py
from pyinfra.operations import apt

PYTHON_PACKAGES = [
    "python3",
    "python3-dev",
    "python3-pip",
    "python3-venv",
    "libpq-dev",
]


def install_packages():
    apt.packages(
        name="Install Python runtime packages",
        packages=PYTHON_PACKAGES,
        present=True,
        update=True,
        _sudo=True,
    )

```

`src/bonesinfra/runtimes/common/ruby.py`:

```py
from pyinfra.operations import apt

RUBY_PACKAGES = [
    "ruby-full",
    "ruby-bundler",
    "libffi-dev",
    "libpq-dev",
    "libyaml-dev",
    "shared-mime-info",
    "zlib1g-dev",
]


def install_packages():
    apt.packages(
        name="Install Ruby runtime packages",
        packages=RUBY_PACKAGES,
        present=True,
        update=True,
        _sudo=True,
    )

```

`src/bonesinfra/runtimes/common/service.py`:

```py
from pathlib import Path

from pyinfra.operations import files, systemd

from bonesinfra.domain.context import template_data
from bonesinfra.domain.paths import DeploymentPaths
from bonesinfra.runtimes.common import validation


def runtime_paths(ctx):
    return DeploymentPaths.new(
        ctx.config.project_name,
        ctx.config.repo_path,
        ctx.config.project_root,
        ctx.runtime.web_root,
    ).__dict__


def render_app_service(  # noqa: PLR0913
    ctx,
    *,
    paths,
    name,
    runtime_label,
    runtime_exec,
    apparmor_profile_name,
    runtime_write_paths,
    runtime_address_families="AF_UNIX",
):
    here = Path(__file__).parent
    project = ctx.config.project_name
    files.template(
        name=f"Deploy {name} systemd service",
        src=str(here / "assets/app.service.j2"),
        dest=f"/etc/systemd/system/{project}-{name}.service",
        user="root",
        group="root",
        mode="0644",
        runtime_name=name,
        runtime_label=runtime_label,
        runtime_exec=runtime_exec,
        apparmor_profile_name=apparmor_profile_name,
        runtime_write_paths=" ".join(runtime_write_paths),
        runtime_address_families=runtime_address_families,
        **template_data(ctx, paths=paths),
        _sudo=True,
    )


def enable_and_start(ctx, name, *, apparmor_profile_name=None):
    service = f"{ctx.config.project_name}-{name}.service"
    systemd.service(
        name=f"Enable and start {name} service",
        service=service,
        enabled=True,
        running=True,
        daemon_reload=True,
        _sudo=True,
    )
    if apparmor_profile_name:
        validation.verify_profile_attached(service, apparmor_profile_name)

```

`src/bonesinfra/runtimes/common/validation.py`:

```py
from shlex import quote

from pyinfra.operations import server


def run_as_runtime_user(ctx, name, command):
    """Validate a runtime command as the runtime user, never as root.

    Root provisioning must not also be the thing that proves the service can
    start: a root-owned validation artifact (e.g. a log file) would later be
    unwritable by the service. Runs the command with HOME/XDG_CONFIG_HOME set
    so user-scoped config resolution matches the real service environment.
    """
    user = ctx.runtime.runtime_user
    q_user = quote(user)
    home = f"$(getent passwd {q_user} | cut -d: -f6)"
    wrapped = f"HOME={home} XDG_CONFIG_HOME={home}/.config {command}"
    server.shell(
        name=name,
        commands=[wrapped],
        _sudo=True,
        _sudo_user=user,
    )


def verify_profile_attached(service_name, profile_name, *, name=None):
    """Verify the service's main PID is confined to the expected AppArmor profile.

    A loaded-but-unattached profile is a silent isolation failure: the service
    runs unrestricted. Reads /proc/<MainPID>/attr/current and fails if the
    profile name is not present. Deliberately run as root (needs /proc access
    to other users' attr and systemctl show).
    """
    q_service = quote(service_name)
    q_profile = quote(profile_name)
    cmd = (
        f"pid=$(systemctl show -p MainPID --value {q_service}); "
        f'[ "$pid" != "0" ] && [ -n "$pid" ] && '
        f'grep -q "{q_profile}" /proc/$pid/attr/current'
    )
    server.shell(
        name=name or f"Verify {service_name} attached to {profile_name}",
        commands=[cmd],
        _sudo=True,
    )

```

`src/bonesinfra/runtimes/django/django.py`:

```py
from bonesinfra.runtimes.common import apparmor, logs, nginx, paths as common_paths, python, service, validation


def questions():
    return [
        {
            "key": "wsgi_module",
            "type": "text",
            "label": "WSGI module",
            "default": "config.wsgi:application",
        },
        {
            "key": "python_version",
            "type": "choice",
            "label": "Python version",
            "choices": ["3.11", "3.12", "3.13"],
            "default": "3.12",
        },
        {
            "key": "install_postgres",
            "type": "bool",
            "label": "Install PostgreSQL client libraries?",
            "default": False,
        },
        {
            "key": "static_root",
            "type": "text",
            "label": "Static root",
            "default": "staticfiles",
        },
        {
            "key": "media_root",
            "type": "text",
            "label": "Media root",
            "default": "media",
        },
    ]


def deploy(ctx):
    paths = service.runtime_paths(ctx)
    socket_path = f"{paths['runtime_socket_dir']}/gunicorn/gunicorn.sock"
    wsgi_module = ctx.runtime.runtime_data.get("wsgi_module", "config.wsgi:application")
    static_root = f"{paths['current']}/{ctx.runtime.runtime_data.get('static_root', 'staticfiles')}"
    media_root = f"{paths['current']}/{ctx.runtime.runtime_data.get('media_root', 'media')}"
    writable = [static_root, media_root]
    gunicorn_bin = f"{paths['current']}/.venv/bin/gunicorn"
    python.install_packages()
    common_paths.ensure_runtime_dirs(ctx)
    logs.ensure(ctx)
    apparmor_profile_name = apparmor.render_app_profile(
        ctx,
        paths=paths,
        runtime="gunicorn",
        apparmor_exec_paths=[gunicorn_bin],
        apparmor_writable_paths=writable,
    )
    validation.run_as_runtime_user(
        ctx,
        "Validate Gunicorn configuration as runtime user",
        f"{gunicorn_bin} --check-config {wsgi_module}",
    )
    service.render_app_service(
        ctx,
        paths=paths,
        name="gunicorn",
        runtime_label="Gunicorn",
        runtime_exec=f"{gunicorn_bin} {wsgi_module} --bind unix:{socket_path}",
        apparmor_profile_name=apparmor_profile_name,
        runtime_write_paths=writable,
    )
    nginx.render_proxy(ctx, paths=paths, socket_path=socket_path)
    service.enable_and_start(ctx, "gunicorn", apparmor_profile_name=apparmor_profile_name)

```

`src/bonesinfra/runtimes/laravel/__init__.py`:

```py
from bonesinfra.runtimes.laravel.deploy import deploy
from bonesinfra.runtimes.laravel.metadata import questions

```

`src/bonesinfra/runtimes/laravel/assets/nginx/laravel-site-nginx.conf.j2`:

```j2
worker_processes 1;
pid {{ paths.runtime_nginx_pid }};
error_log {{ paths.runtime_nginx_dir }}/error.log notice;

events {
    worker_connections 1024;
}

http {
    access_log {{ paths.runtime_nginx_dir }}/access.log;
    client_body_temp_path {{ paths.runtime_nginx_dir }}/client_body;
    proxy_temp_path {{ paths.runtime_nginx_dir }}/proxy;
    fastcgi_temp_path {{ paths.runtime_nginx_dir }}/fastcgi;
    uwsgi_temp_path {{ paths.runtime_nginx_dir }}/uwsgi;
    scgi_temp_path {{ paths.runtime_nginx_dir }}/scgi;

    server {
        listen unix:{{ paths.runtime_nginx_socket }};
        root {{ paths.current_web_root }};
        index index.php index.html;

        location / {
            try_files $uri $uri/ /index.php?$query_string;
        }

        location ~ ^/index\.php(/|$) {
            fastcgi_pass unix:{{ laravel_php_fpm_socket_path }};
            fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
            include /etc/nginx/fastcgi_params;
            fastcgi_param DOCUMENT_ROOT $realpath_root;
            internal;
        }

        location ~ \.php$ {
            return 404;
        }

        location ^~ /.well-known/acme-challenge/ {
            try_files $uri =404;
        }
    }
}

```

`src/bonesinfra/runtimes/laravel/assets/php/php-fpm-pool.conf.j2`:

```j2
[{{ laravel_php_fpm_pool_name }}]
user = {{ runtime_user }}
group = {{ runtime_group }}

listen = {{ laravel_php_fpm_socket_path }}
listen.owner = www-data
listen.group = www-data
listen.mode = 0660

pm = dynamic
pm.max_children = 10
pm.start_servers = 2
pm.min_spare_servers = 1
pm.max_spare_servers = 3

chdir = {{ paths.current }}
clear_env = no

catch_workers_output = yes
decorate_workers_output = no

php_admin_flag[log_errors] = on
php_admin_value[error_log] = /var/log/bonesdeploy/{{ project_name }}/php-worker-error.log

access.log = /var/log/bonesdeploy/{{ project_name }}/php-fpm-access.log
slowlog = /var/log/bonesdeploy/{{ project_name }}/php-fpm-slow.log

```

`src/bonesinfra/runtimes/laravel/deploy.py`:

```py
from pathlib import Path

from bonesinfra.domain.paths import DeploymentPaths
from bonesinfra.runtimes.laravel import nginx, php_fpm, php_packages, php_repo


def deploy(ctx):
    here = Path(__file__).parent
    php_version = ctx.runtime.runtime_data.get("php_version", "8.3")
    paths = DeploymentPaths.new(
        ctx.config.project_name,
        ctx.config.repo_path,
        ctx.config.project_root,
        ctx.runtime.web_root,
    ).__dict__

    php_repo.add_php_apt_source()
    php_packages.install_php(php_version)

    php_fpm.setup_storage_directories(paths, ctx)
    php_fpm.setup_pool(here, ctx, paths, php_version)
    nginx.setup(here, ctx, paths, php_version)

```

`src/bonesinfra/runtimes/laravel/metadata.py`:

```py
def questions():
    return [
        {
            "key": "php_version",
            "type": "choice",
            "label": "PHP version",
            "choices": ["8.2", "8.3", "8.4", "8.5"],
            "default": "8.5",
        },
        {
            "key": "install_queue_worker",
            "type": "bool",
            "label": "Install Laravel queue worker?",
            "default": False,
        },
    ]

```

`src/bonesinfra/runtimes/laravel/nginx.py`:

```py
from pyinfra.operations import files, server

from bonesinfra.domain.context import template_data
from bonesinfra.runtimes.common import php_fpm_pool


def setup(here, ctx, paths, php_version):
    runtime_group = ctx.runtime.runtime_group
    php_fpm_socket_path = php_fpm_pool.socket_path(ctx.config.project_name, php_version)

    files.template(
        name="Deploy Laravel-specific per-site nginx config",
        src=str(here / "assets/nginx/laravel-site-nginx.conf.j2"),
        dest=paths["site_nginx_config"],
        user="root",
        group=runtime_group,
        mode="0640",
        laravel_php_fpm_socket_path=php_fpm_socket_path,
        **template_data(ctx, paths=paths),
        _sudo=True,
    )

    server.shell(
        name="Validate nginx configuration with Laravel config",
        commands=[f"nginx -t -c {paths['site_nginx_config']}"],
        _sudo=True,
    )

```

`src/bonesinfra/runtimes/laravel/php_fpm.py`:

```py
from pyinfra.operations import files

from bonesinfra.runtimes.common import php_fpm_pool


def setup_storage_directories(paths, ctx):
    runtime_user = ctx.runtime.runtime_user
    runtime_group = ctx.runtime.runtime_group
    subdirs = ["logs", "framework/cache", "framework/sessions", "framework/views"]
    for subdir in subdirs:
        files.directory(
            name=f"Ensure storage/{subdir} exists",
            path=f"{paths['current']}/storage/{subdir}",
            user=runtime_user,
            group=runtime_group,
            mode="0775",
            _sudo=True,
        )


def setup_pool(here, ctx, paths, php_version):
    php_fpm_pool.ensure_log_dir(ctx)
    php_fpm_pool.render_pool(ctx, here=here, paths=paths, php_version=php_version)
    php_fpm_pool.validate_php_fpm(php_version)
    php_fpm_pool.reload_php_fpm(php_version)

```

`src/bonesinfra/runtimes/laravel/php_packages.py`:

```py
from pyinfra.operations import apt


def install_php(php_version):
    packages = [
        f"php{php_version}",
        f"php{php_version}-cli",
        f"php{php_version}-fpm",
        f"php{php_version}-bcmath",
        f"php{php_version}-curl",
        f"php{php_version}-gd",
        f"php{php_version}-intl",
        f"php{php_version}-mbstring",
        f"php{php_version}-mysql",
        f"php{php_version}-sqlite3",
        f"php{php_version}-xml",
        f"php{php_version}-zip",
        "composer",
    ]

    apt.packages(
        name="Install Laravel PHP packages",
        packages=packages,
        present=True,
        update=True,
        _sudo=True,
    )

```

`src/bonesinfra/runtimes/laravel/php_repo.py`:

```py
from tempfile import NamedTemporaryFile

PHP_SURY_KEYRING_URL = "https://packages.sury.org/debsuryorg-archive-keyring.deb"
PHP_SURY_KEYRING_DEST = "/usr/share/keyrings/deb.sury.org-php.gpg"
PHP_SURY_PREREQUISITES = [
    "apt-transport-https",
    "ca-certificates",
    "curl",
    "lsb-release",
]


def _resolve_codename():
    from pyinfra import host
    from pyinfra.facts.server import LinuxDistribution

    deb = host.get_fact(LinuxDistribution)
    release_meta = deb.get("release_meta", {}) if deb else {}
    return (
        release_meta.get("VERSION_CODENAME")
        or release_meta.get("CODENAME")
        or release_meta.get("DISTRIB_CODENAME")
        or "noble"
    )


def add_php_apt_source():
    from pyinfra.operations import apt, server

    apt.packages(
        name="Install PHP repo prerequisites",
        packages=PHP_SURY_PREREQUISITES,
        present=True,
        update=True,
        _sudo=True,
    )

    with NamedTemporaryFile(delete=False, suffix=".deb") as f:
        keyring_path = f.name

    server.shell(
        name="Download PHP repo keyring package",
        commands=[f"curl -sSLo {keyring_path} {PHP_SURY_KEYRING_URL}"],
        _sudo=True,
    )

    apt.deb(
        name="Install PHP repo keyring package",
        src=keyring_path,
        _sudo=True,
    )

    server.shell(
        name="Remove stale PHP apt source file",
        commands=["rm -f /etc/apt/sources.list.d/php.list"],
        _sudo=True,
    )

    codename = _resolve_codename()
    apt.repo(
        name="Add Laravel PHP apt repository",
        src=f"deb [signed-by={PHP_SURY_KEYRING_DEST}] https://packages.sury.org/php {codename} main",
        filename="php",
        _sudo=True,
    )

```

`src/bonesinfra/runtimes/next/next.py`:

```py
from bonesinfra.runtimes.common import apparmor, logs, nginx, node, paths as common_paths, service, validation


def questions():
    return []


def deploy(ctx):
    paths = service.runtime_paths(ctx)
    port = ctx.runtime.runtime_data.get("internal_port", 3100)
    node.install_packages()
    common_paths.ensure_runtime_dirs(ctx)
    logs.ensure(ctx)
    apparmor_profile_name = apparmor.render_app_profile(
        ctx,
        paths=paths,
        runtime="next",
        apparmor_exec_paths=["/usr/bin/node"],
        apparmor_writable_paths=[],
        apparmor_network="network inet stream,",
    )
    validation.run_as_runtime_user(
        ctx,
        "Validate Next.js standalone server exists as runtime user",
        "test -f .next/standalone/server.js",
    )
    service.render_app_service(
        ctx,
        paths=paths,
        name="next",
        runtime_label="Next.js app server",
        runtime_exec=(
            f"/usr/bin/env NODE_ENV=production PORT={port} HOSTNAME=127.0.0.1 "
            "node .next/standalone/server.js"
        ),
        apparmor_profile_name=apparmor_profile_name,
        runtime_write_paths=[],
        runtime_address_families="AF_UNIX AF_INET",
    )
    nginx.render_proxy(ctx, paths=paths, port=port)
    service.enable_and_start(ctx, "next", apparmor_profile_name=apparmor_profile_name)

```

`src/bonesinfra/runtimes/nuxt/nuxt.py`:

```py
from bonesinfra.runtimes.common import apparmor, logs, nginx, node, paths as common_paths, service, validation


def questions():
    return []


def deploy(ctx):
    paths = service.runtime_paths(ctx)
    socket_path = f"{paths['runtime_socket_dir']}/nuxt/nuxt.sock"
    node.install_packages()
    common_paths.ensure_runtime_dirs(ctx)
    logs.ensure(ctx)
    apparmor_profile_name = apparmor.render_app_profile(
        ctx,
        paths=paths,
        runtime="nuxt",
        apparmor_exec_paths=["/usr/bin/node"],
        apparmor_writable_paths=[],
    )
    validation.run_as_runtime_user(
        ctx,
        "Validate Nuxt server entrypoint exists as runtime user",
        "test -f .output/server/index.mjs",
    )
    service.render_app_service(
        ctx,
        paths=paths,
        name="nuxt",
        runtime_label="Nuxt app server",
        runtime_exec=(
            f"/usr/bin/env NODE_ENV=production NITRO_UNIX_SOCKET={socket_path} "
            "node .output/server/index.mjs"
        ),
        apparmor_profile_name=apparmor_profile_name,
        runtime_write_paths=[],
    )
    nginx.render_proxy(ctx, paths=paths, socket_path=socket_path)
    service.enable_and_start(ctx, "nuxt", apparmor_profile_name=apparmor_profile_name)

```

`src/bonesinfra/runtimes/rails/rails.py`:

```py
from bonesinfra.runtimes.common import apparmor, logs, nginx, paths as common_paths, ruby, service, validation


def questions():
    return [
        {
            "key": "ruby_version",
            "type": "choice",
            "label": "Ruby version",
            "choices": ["3.2", "3.3", "3.4"],
            "default": "3.3",
        },
        {
            "key": "install_postgres",
            "type": "bool",
            "label": "Install PostgreSQL client libraries?",
            "default": False,
        },
        {
            "key": "install_redis",
            "type": "bool",
            "label": "Install Redis?",
            "default": False,
        },
        {
            "key": "rails_env",
            "type": "text",
            "label": "Rails environment",
            "default": "production",
        },
    ]


def deploy(ctx):
    paths = service.runtime_paths(ctx)
    socket_path = f"{paths['runtime_socket_dir']}/puma/puma.sock"
    runtime_write_paths = [
        f"{paths['current']}/tmp",  # noqa: S108
        f"{paths['current']}/log",
        f"{paths['current']}/storage",
    ]
    rails_env = ctx.runtime.runtime_data.get("rails_env", "production")
    ruby.install_packages()
    common_paths.ensure_runtime_dirs(ctx)
    logs.ensure(ctx)
    apparmor_profile_name = apparmor.render_app_profile(
        ctx,
        paths=paths,
        runtime="puma",
        apparmor_exec_paths=["/usr/bin/ruby*", "/usr/bin/bundle*"],
        apparmor_writable_paths=runtime_write_paths,
    )
    validation.run_as_runtime_user(
        ctx,
        "Validate Puma availability as runtime user",
        "bundle exec puma --help >/dev/null",
    )
    service.render_app_service(
        ctx,
        paths=paths,
        name="puma",
        runtime_label="Puma",
        runtime_exec=f"/usr/bin/env RAILS_ENV={rails_env} bundle exec puma -e {rails_env} -b unix://{socket_path}",
        apparmor_profile_name=apparmor_profile_name,
        runtime_write_paths=runtime_write_paths,
    )
    nginx.render_proxy(ctx, paths=paths, socket_path=socket_path)
    service.enable_and_start(ctx, "puma", apparmor_profile_name=apparmor_profile_name)

```

`src/bonesinfra/runtimes/sveltekit/svelte.py`:

```py
from bonesinfra.runtimes.common import apparmor, logs, nginx, node, paths as common_paths, service, validation


def questions():
    return []


def deploy(ctx):
    paths = service.runtime_paths(ctx)
    socket_path = f"{paths['runtime_socket_dir']}/sveltekit/sveltekit.sock"
    origin = f"https://{ctx.config.domain}" if ctx.config.domain else "https://localhost"
    node.install_packages()
    common_paths.ensure_runtime_dirs(ctx)
    logs.ensure(ctx)
    apparmor_profile_name = apparmor.render_app_profile(
        ctx,
        paths=paths,
        runtime="sveltekit",
        apparmor_exec_paths=["/usr/bin/node"],
        apparmor_writable_paths=[],
    )
    validation.run_as_runtime_user(
        ctx,
        "Validate SvelteKit build entrypoint exists as runtime user",
        "test -e build",
    )
    service.render_app_service(
        ctx,
        paths=paths,
        name="sveltekit",
        runtime_label="SvelteKit app server",
        runtime_exec=(
            f"/usr/bin/env --chdir={paths['current']} NODE_ENV=production SOCKET_PATH={socket_path} "
            f"ORIGIN={origin} node --env-file=.env build"
        ),
        apparmor_profile_name=apparmor_profile_name,
        runtime_write_paths=[],
    )
    nginx.render_proxy(ctx, paths=paths, socket_path=socket_path)
    service.enable_and_start(ctx, "sveltekit", apparmor_profile_name=apparmor_profile_name)

```

`src/bonesinfra/runtimes/vue/vue.py`:

```py
from bonesinfra.runtimes.common import nginx, service


def questions():
    return []


def deploy(ctx):
    paths = service.runtime_paths(ctx)
    nginx.render_static(ctx, paths=paths)

```

`tests/__main__.py`:

```py
"""Test discovery runner — no external deps required."""

import importlib
import traceback
from pathlib import Path


def discover_tests():
    root = Path(__file__).parent
    for file in sorted(root.glob("test_*.py")):
        mod = file.stem
        print(f"\n=== {mod} ===")
        m = importlib.import_module(f"tests.{mod}")
        for name in sorted(dir(m)):
            if not name.startswith("test_"):
                continue
            fn = getattr(m, name)
            if not callable(fn):
                continue
            yield mod, name, fn


def main():
    passed = 0
    failed = 0

    for _, test_name, fn in discover_tests():
        try:
            fn()
            print(f"  OK: {test_name}")
            passed += 1
        except AssertionError:
            print(f"  FAIL: {test_name}")
            for line in traceback.format_exc().splitlines()[-3:]:
                print(f"        {line}")
            failed += 1

    print(f"\n{passed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

```

`tests/cleancode/test_no_provably_unnecessary_fallback.py`:

```py
"""Test: no provably unnecessary fallback patterns.

Detects ``or`` expressions where the left side is a literal that is
always truthy, making the right-hand side (fallback) dead code.
"""

import ast
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIRS = ["src", "app", "lib"]
IGNORE_DIRS = {"venv", ".venv", ".env", "node_modules", "dist", "build", "coverage", "__pycache__"}


def _find_source_files() -> list[Path]:
    files = []
    for d in SRC_DIRS:
        src = PROJECT_ROOT / d
        if not src.is_dir():
            continue
        files.extend(
            path
            for path in src.rglob("*.py")
            if not any(part in IGNORE_DIRS for part in path.relative_to(PROJECT_ROOT).parts)
        )
    return files


def _has_items(node: ast.expr) -> bool:
    match node:
        case ast.List(elts=elts) | ast.Tuple(elts=elts) | ast.Set(elts=elts):
            return len(elts) > 0
        case ast.Dict(keys=keys):
            return len(keys) > 0
        case _:
            return False


def _is_definitely_truthy(node: ast.expr) -> bool:
    result = False
    match node:
        case ast.Constant(value=bool() as value):
            result = value
        case ast.Constant(value=str() as value):
            result = len(value) > 0
        case ast.Constant(value=int() as value):
            result = value != 0
        case ast.Constant(value=float() as value):
            result = value != 0.0
        case _:
            result = _has_items(node)
    return result


_SOURCE_FILES = _find_source_files()


@pytest.mark.parametrize("filepath", _SOURCE_FILES, ids=lambda p: str(p.relative_to(PROJECT_ROOT)))
def test_no_provably_unnecessary_fallback(filepath: Path) -> None:
    code = filepath.read_text(encoding="utf-8")
    try:
        tree = ast.parse(code)
    except SyntaxError:
        pytest.skip(f"Cannot parse {filepath}")

    violations: list[str] = []

    for node in ast.walk(tree):
        if not isinstance(node, ast.BoolOp) or node.op.__class__ is not ast.Or:
            continue
        if len(node.values) < 2:
            continue
        left = node.values[0]
        if _is_definitely_truthy(left):
            violations.append(f"  L{left.lineno}: left side of `or` is always truthy")

    assert not violations, f"Unnecessary fallback(s) in {filepath.relative_to(PROJECT_ROOT)}:\n" + "\n".join(violations)

```

`tests/cleancode/test_no_suspicious_fallback.py`:

```py
"""Test: no suspicious fallback patterns.

Detects ``try/except`` blocks where the except handler returns a
success value without re-raising — silently manufacturing success
from an error path.
"""

import ast
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIRS = ["src", "app", "lib"]
IGNORE_DIRS = {"venv", ".venv", ".env", "node_modules", "dist", "build", "coverage", "__pycache__"}


def _find_source_files() -> list[Path]:
    files = []
    for d in SRC_DIRS:
        src = PROJECT_ROOT / d
        if not src.is_dir():
            continue
        files.extend(
            path
            for path in src.rglob("*.py")
            if not any(part in IGNORE_DIRS for part in path.relative_to(PROJECT_ROOT).parts)
        )
    return files


def _has_return(stmts: list[ast.stmt]) -> bool:
    stack: list[ast.AST] = list(stmts)
    while stack:
        node = stack.pop()
        if isinstance(node, ast.Return):
            return True
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                continue
            stack.append(child)
    return False


def _has_raise(stmts: list[ast.stmt]) -> bool:
    stack: list[ast.AST] = list(stmts)
    while stack:
        node = stack.pop()
        if isinstance(node, ast.Raise):
            return True
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                continue
            stack.append(child)
    return False


def _find_returns(stmts: list[ast.stmt]) -> list[ast.Return]:
    results: list[ast.Return] = []
    stack: list[ast.AST] = list(stmts)
    while stack:
        node = stack.pop()
        if isinstance(node, ast.Return):
            results.append(node)
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                continue
            stack.append(child)
    return results


_SOURCE_FILES = _find_source_files()


@pytest.mark.parametrize("filepath", _SOURCE_FILES, ids=lambda p: str(p.relative_to(PROJECT_ROOT)))
def test_no_suspicious_fallback(filepath: Path) -> None:
    code = filepath.read_text(encoding="utf-8")
    try:
        tree = ast.parse(code)
    except SyntaxError:
        pytest.skip(f"Cannot parse {filepath}")

    violations: list[str] = []

    for node in ast.walk(tree):
        if not isinstance(node, ast.Try):
            continue
        if not _has_return(list(node.body)):
            continue
        for handler in node.handlers:
            if _has_raise(list(handler.body)):
                continue
            violations.extend(
                f"  L{return_node.lineno}: except handler returns success without re-raise"
                for return_node in _find_returns(list(handler.body))
            )

    assert not violations, f"Suspicious fallback(s) in {filepath.relative_to(PROJECT_ROOT)}:\n" + "\n".join(violations)

```

`tests/helpers.py`:

```py
import os
import subprocess
import sys
from functools import cache
from pathlib import Path

INFRA_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = INFRA_DIR / "src"
REPO_ROOT = INFRA_DIR.parent
sys.path.insert(0, str(SRC_DIR))

PYTHON_BIN = sys.executable
PYTHON_ENV = {**os.environ, "PYTHONPATH": str(SRC_DIR)}


@cache
def read(path):
    return Path(path).read_text()


def assert_contains(text, pattern, msg=""):
    assert pattern in text, f"{msg}\n  missing: {pattern!r}"


def assert_not_contains(text, pattern, msg=""):
    assert pattern not in text, f"{msg}\n  unexpected: {pattern!r}"


def assert_ordering(text, *anchors):
    idx = -1
    for anchor in anchors:
        new_idx = text.find(anchor, idx + 1)
        assert new_idx > idx, f"Must appear in order, missing earlier: {anchor!r}"


def assert_file_exists(path, msg=""):
    assert Path(path).exists(), msg or f"Missing file: {path}"


def assert_file_not_exists(path, msg=""):
    assert not Path(path).exists(), msg or f"Unexpected file: {path}"


def compile_module(path):
    source = Path(path).read_text()
    return compile(source, str(path), "exec")


def exec_module(path):
    source = Path(path).read_text()
    ns = {}
    exec(source, ns)
    return ns


def run(*args):
    result = subprocess.run(
        [sys.executable, "-m", "bonesinfra", *args],
        capture_output=True,
        text=True,
        timeout=10,
        env=PYTHON_ENV,
        check=False,
    )
    assert result.returncode == 0, f"Failed: {' '.join(args)}\n{result.stderr}"
    return result.stdout

```

`tests/test_cli.py`:

```py
"""CLI commands must run without crashing."""

import subprocess

from . import helpers

PYTHON = helpers.PYTHON_BIN
PYTHON_ENV = helpers.PYTHON_ENV


def _run_no_input(*args):
    return subprocess.run(
        [PYTHON, "-m", "bonesinfra", *args],
        capture_output=True,
        text=True,
        timeout=10,
        env=PYTHON_ENV,
        check=False,
    )


def test_runtime_list():
    result = _run_no_input("runtime", "list")
    assert result.returncode == 0, result.stderr


def test_runtime_questions_all():
    for name in ["django", "laravel", "next", "rails", "sveltekit", "vue"]:
        result = _run_no_input("runtime", "questions", name)
        assert result.returncode == 0, f"{name}: {result.stderr}"


def test_setup_apply_rejects_missing_host():
    result = _run_no_input("setup", "apply", "--config", "/dev/null")
    assert result.returncode == 3, f"Expected exit 3 for missing host, got {result.returncode}"
    assert "missing host" in result.stderr.lower()


def test_runtime_apply_rejects_missing_host():
    result = _run_no_input("runtime", "apply", "--config", "/dev/null", "--runtime-config", "/dev/null")
    assert result.returncode == 3, f"Expected exit 3 for missing host, got {result.returncode}"
    assert "missing host" in result.stderr.lower()


def test_ssl_apply_rejects_missing_host():
    result = _run_no_input("ssl", "apply", "--config", "/dev/null")
    assert result.returncode == 3, f"Expected exit 3 for missing host, got {result.returncode}"
    assert "missing host" in result.stderr.lower()

```

`tests/test_context.py`:

```py
"""Deploy context defaults should preserve per-project identity."""

from pathlib import Path
from tempfile import TemporaryDirectory

from bonesinfra.domain.context import DeployContext, template_data


def test_runtime_identity_defaults_to_project_name():
    with TemporaryDirectory() as tmp:
        config_path = Path(tmp) / "bones.toml"
        config_path.write_text(
            """
project_name = "lawsnipe"
repo_path = "/home/git/lawsnipe.git"
project_root = "/srv/sites/lawsnipe"
host = "example.com"
""".lstrip()
        )

        ctx = DeployContext.from_files(str(config_path))

    assert ctx.config.project_name == "lawsnipe"
    assert ctx.config.host == "example.com"
    assert ctx.config.ssh_user == "root"
    assert ctx.runtime.web_root == "public"
    assert ctx.runtime.runtime_user == "lawsnipe"
    assert ctx.runtime.runtime_group == "lawsnipe"
    assert ctx.runtime.release_group == "lawsnipe-release"
    assert ctx.ssh_port == 22

    td = template_data(ctx)
    assert td["runtime_user"] == "lawsnipe"
    assert td["runtime_group"] == "lawsnipe"


def test_runtime_identity_respects_explicit_override():
    with TemporaryDirectory() as tmp:
        config_path = Path(tmp) / "bones.toml"
        config_path.write_text(
            """
project_name = "lawsnipe"
repo_path = "/home/git/lawsnipe.git"
project_root = "/srv/sites/lawsnipe"
host = "example.com"
""".lstrip()
        )
        runtime_config_path = Path(tmp) / "runtime.toml"
        runtime_config_path.write_text(
            """
runtime_user = "lawsnipe-web"
runtime_group = "lawsnipe-web"
""".lstrip()
        )

        ctx = DeployContext.from_files(str(config_path), str(runtime_config_path))

    assert ctx.config.project_name == "lawsnipe"
    assert ctx.runtime.web_root == "public"
    assert ctx.runtime.runtime_user == "lawsnipe-web"
    assert ctx.runtime.runtime_group == "lawsnipe-web"

```

`tests/test_deploy_structure.py`:

```py
"""Operation ordering and separation of concerns in deploy plans."""

from . import helpers

SETUP_PLAN = helpers.SRC_DIR / "bonesinfra/deploys/setup/plan.py"
SETUP_PACKAGES = helpers.SRC_DIR / "bonesinfra/deploys/setup/packages.py"
SETUP_USERS = helpers.SRC_DIR / "bonesinfra/deploys/setup/users.py"
SETUP_DIRECTORIES = helpers.SRC_DIR / "bonesinfra/deploys/setup/directories.py"
SETUP_PLACEHOLDER = helpers.SRC_DIR / "bonesinfra/deploys/setup/placeholder.py"
SETUP_FIREWALL = helpers.SRC_DIR / "bonesinfra/deploys/setup/firewall.py"
SETUP_BONESREMOTE = helpers.SRC_DIR / "bonesinfra/deploys/setup/bonesremote.py"
RUNTIME_PLAN = helpers.SRC_DIR / "bonesinfra/deploys/runtime/plan.py"
RUNTIME_PACKAGES = helpers.SRC_DIR / "bonesinfra/deploys/runtime/packages.py"
RUNTIME_APPARMOR = helpers.SRC_DIR / "bonesinfra/deploys/runtime/apparmor.py"
RUNTIME_NGINX = helpers.SRC_DIR / "bonesinfra/deploys/runtime/nginx.py"
RUNTIME_DOCTOR = helpers.SRC_DIR / "bonesinfra/deploys/runtime/doctor.py"
RUNTIME_TEMPLATE = helpers.SRC_DIR / "bonesinfra/deploys/runtime/template_runtime.py"
SSL_PLAN = helpers.SRC_DIR / "bonesinfra/deploys/ssl/plan.py"
LARAVEL_DEPLOY = helpers.SRC_DIR / "bonesinfra/runtimes/laravel/deploy.py"


# ---- setup plan ----


def test_setup_plan_calls_all_steps():
    c = helpers.read(SETUP_PLAN)
    helpers.assert_contains(c, "packages.install_system")
    helpers.assert_contains(c, "users.install_rust")
    helpers.assert_contains(c, "users.ensure_users_and_groups")
    helpers.assert_contains(c, "directories.setup_repo_and_project")
    helpers.assert_contains(c, "placeholder.seed")
    helpers.assert_contains(c, "firewall.configure")
    helpers.assert_contains(c, "users.install_authorized_key")
    helpers.assert_contains(c, "bonesremote.install")


def test_setup_plan_uses_base_packages():
    c = helpers.read(SETUP_PLAN)
    helpers.assert_contains(c, "BASE_SYSTEM_PACKAGES")


def test_setup_plan_ordering():
    c = helpers.read(SETUP_PLAN)
    helpers.assert_ordering(
        c,
        "packages.install_system",
        "users.install_rust",
        "users.ensure_users_and_groups",
    )


def test_setup_excludes_apparmor():
    for f in [
        SETUP_PLAN,
        SETUP_PACKAGES,
        SETUP_USERS,
        SETUP_DIRECTORIES,
        SETUP_PLACEHOLDER,
        SETUP_FIREWALL,
        SETUP_BONESREMOTE,
    ]:
        c = helpers.read(f)
        helpers.assert_not_contains(c, "apparmor_parser")
        helpers.assert_not_contains(c, "apparmor_profile_name")


def test_setup_excludes_runtime_doctor():
    c = helpers.read(SETUP_PLAN)
    helpers.assert_not_contains(c, "bonesremote doctor")


def test_setup_excludes_per_site_roles():
    c = helpers.read(SETUP_PLAN)
    helpers.assert_not_contains(c, "bonesdeploy-nginx")
    helpers.assert_not_contains(c, "per-site nginx")


def test_setup_uses_resolved_placeholder_paths():
    c1 = helpers.read(SETUP_DIRECTORIES)
    helpers.assert_contains(c1, "placeholder_web_root")
    c2 = helpers.read(SETUP_PLACEHOLDER)
    helpers.assert_contains(c2, "placeholder_index")


def test_setup_avoids_usermod_for_existing_runtime_user():
    c = helpers.read(SETUP_USERS)
    helpers.assert_contains(c, "host.get_fact(Users)")
    helpers.assert_contains(c, "gpasswd -a")


def test_setup_deploy_user_commands_set_user_home():
    c = helpers.read(SETUP_DIRECTORIES)
    helpers.assert_contains(c, "XDG_CONFIG_HOME={home}/.config")
    helpers.assert_contains(c, "getent passwd")


# ---- Firewall ----


def test_setup_firewall_handles_ssh_cidrs():
    c = helpers.read(SETUP_FIREWALL)
    helpers.assert_contains(c, "ssh_cidrs")


def test_setup_firewall_filters_ssh_from_allowed_ports():
    c = helpers.read(SETUP_FIREWALL)
    helpers.assert_contains(c, 'port == "ssh"')
    helpers.assert_contains(c, "continue")


def test_setup_firewall_resolves_port_aliases():
    c = helpers.read(SETUP_FIREWALL)
    helpers.assert_contains(c, "port_aliases.get(port, port)")


def test_setup_firewall_sets_default_policies():
    c = helpers.read(SETUP_FIREWALL)
    helpers.assert_contains(c, "ufw --force default")
    helpers.assert_contains(c, "firewall_default_incoming_policy")
    helpers.assert_contains(c, "firewall_default_outgoing_policy")


def test_setup_firewall_gated_by_enabled_flag():
    c = helpers.read(SETUP_FIREWALL)
    helpers.assert_contains(c, "firewall_enabled")


def test_setup_firewall_status_gated_by_show_status():
    c = helpers.read(SETUP_FIREWALL)
    helpers.assert_contains(c, "ufw status verbose")
    helpers.assert_contains(c, "firewall_show_status")


# ---- runtime plan ----


def test_runtime_plan_calls_all_steps():
    c = helpers.read(RUNTIME_PLAN)
    helpers.assert_contains(c, "packages.install_apt")
    helpers.assert_contains(c, "apparmor.setup")
    helpers.assert_contains(c, "nginx.setup")
    helpers.assert_contains(c, "template_runtime.load")
    helpers.assert_contains(c, "nginx.start_services")
    helpers.assert_contains(c, "doctor.run")


def test_runtime_applies_apparmor_and_nginx():
    c = helpers.read(RUNTIME_APPARMOR)
    helpers.assert_contains(c, "apparmor_parser -r")
    helpers.assert_contains(c, "aa-enforce")
    helpers.assert_contains(c, "apparmor_enabled_param")
    c2 = helpers.read(RUNTIME_NGINX)
    helpers.assert_contains(c2, "per-site nginx")


def test_common_apparmor_enforces_after_load():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/common/apparmor.py")
    helpers.assert_ordering(
        c,
        "apparmor_parser -r",
        "aa-enforce",
    )


def test_common_service_verifies_profile_attached():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/common/service.py")
    helpers.assert_contains(c, "validation.verify_profile_attached")
    helpers.assert_contains(c, "apparmor_profile_name=None")


def test_common_validation_verifies_proc_attr_current():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/common/validation.py")
    helpers.assert_contains(c, "def verify_profile_attached")
    helpers.assert_contains(c, "attr/current")
    helpers.assert_contains(c, "MainPID")


def test_app_service_uses_per_service_runtime_directory_leaf():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/common/assets/app.service.j2")
    helpers.assert_contains(c, "RuntimeDirectory={{ project_name }}/{{ runtime_name }}")


def test_site_nginx_service_uses_nginx_runtime_directory_leaf():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/assets/nginx/site-nginx.service.j2")
    helpers.assert_contains(c, "RuntimeDirectory={{ project_name }}/nginx")
    helpers.assert_contains(c, "ReadWritePaths={{ paths.runtime_nginx_dir }}")


def test_project_nginx_profile_grants_nginx_dir_and_app_sockets():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/assets/apparmor/project-nginx-profile.j2")
    helpers.assert_contains(c, "{{ paths.runtime_nginx_dir }}/ rw,")
    helpers.assert_contains(c, "{{ paths.runtime_nginx_dir }}/** rwk,")
    helpers.assert_contains(c, "{{ paths.runtime_socket_dir }}/*/*.sock rw,")
    helpers.assert_not_contains(c, "{{ paths.runtime_socket_dir }}/** rwk,")


def test_runtime_plan_ordering():
    c = helpers.read(RUNTIME_PLAN)
    helpers.assert_ordering(
        c,
        "packages.install_apt",
        "nginx.setup",
        "template_runtime.load",
        "nginx.start_services",
    )


def test_runtime_excludes_ssl_logic():
    c = helpers.read(RUNTIME_PLAN)
    helpers.assert_not_contains(c, "certbot")


def test_runtime_socket_dir_runtime_user_owned():
    c = helpers.read(RUNTIME_NGINX)
    helpers.assert_contains(c, 'path=paths["runtime_socket_dir"]')
    helpers.assert_contains(c, 'path=paths["runtime_nginx_dir"]')
    helpers.assert_contains(c, "user=ctx.runtime.runtime_user")
    helpers.assert_contains(c, "group=ctx.runtime.runtime_group")
    # 0711: system nginx (www-data) must traverse /run/<project>/ and
    # /run/<project>/nginx/ to reach the per-site nginx socket. 0750 causes 502.
    helpers.assert_contains(c, 'mode="0711"')


def test_runtime_uses_template_runtime():
    c = helpers.read(RUNTIME_TEMPLATE)
    helpers.assert_contains(c, "get_runtime(template)")


def test_runtime_doctor_deploy_user_commands_set_user_home():
    c = helpers.read(RUNTIME_DOCTOR)
    helpers.assert_contains(c, "XDG_CONFIG_HOME={home}/.config")
    helpers.assert_contains(c, "getent passwd")


# ---- ssl plan ----


def test_ssl_uses_certbot():
    c = helpers.read(SSL_PLAN)
    helpers.assert_contains(c, "certbot certonly")
    helpers.assert_contains(c, "ssl_domain")


def test_ssl_excludes_apparmor():
    c = helpers.read(SSL_PLAN)
    helpers.assert_not_contains(c, "apparmor_parser")


def test_ssl_excludes_per_site_nginx():
    c = helpers.read(SSL_PLAN)
    helpers.assert_not_contains(c, '"per-site nginx"')


def test_ssl_excludes_runtimes():
    c = helpers.read(SSL_PLAN)
    helpers.assert_not_contains(c, "runtimes")


def test_ssl_defines_nginx_inline():
    c = helpers.read(SSL_PLAN)
    helpers.assert_contains(c, "nginx_server_name")
    helpers.assert_contains(c, "router.conf.j2")
    helpers.assert_contains(c, "nginx -t")


def test_runtime_nginx_falls_back_when_domain_empty():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/deploys/runtime/nginx.py")
    helpers.assert_contains(c, "ctx.config.domain or ctx.config.preview_domain")
    helpers.assert_contains(
        c,
        'raise ValueError("domain or preview_domain is required for nginx config")',
    )


def test_ssl_requires_real_domain_for_router_render():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/deploys/ssl/plan.py")
    helpers.assert_contains(c, 'raise ValueError("domain is required for ssl nginx config")')


def test_ssl_uses_current_web_root():
    c = helpers.read(SSL_PLAN)
    helpers.assert_contains(c, "current_web_root")


# ---- Laravel-specific ordering ----


def test_laravel_validates_php_fpm_before_start():
    c = helpers.read(LARAVEL_DEPLOY)
    helpers.assert_ordering(
        c,
        "php_repo.add_php_apt_source",
        "php_packages.install_php",
    )


def test_laravel_validates_php_fpm_before_reload():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/php_fpm.py")
    helpers.assert_ordering(
        c,
        "php_fpm_pool.render_pool",
        "php_fpm_pool.validate_php_fpm",
        "php_fpm_pool.reload_php_fpm",
    )


def test_laravel_deploy_does_not_setup_php_fpm_apparmor():
    c = helpers.read(LARAVEL_DEPLOY)
    helpers.assert_not_contains(c, "apparmor")
    helpers.assert_ordering(
        c,
        "php_fpm.setup_storage_directories",
        "php_fpm.setup_pool",
        "nginx.setup",
    )


def test_laravel_nginx_validates_without_creating_runtime_dir():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/nginx.py")
    helpers.assert_ordering(
        c,
        "laravel-site-nginx.conf.j2",
        "nginx -t",
    )
    helpers.assert_not_contains(c, "runtime_socket_dir")


def test_laravel_nginx_does_not_restart_site_service_early():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/nginx.py")
    helpers.assert_not_contains(c, "Restart per-site nginx with Laravel config")


# ---- Runtime directory traversal for system nginx (www-data) ----


def test_runtime_socket_dir_is_traversable_by_system_nginx():
    """Regression: /run/<project>/ must be 0711, not 0750, so system nginx
    (www-data) can traverse it to reach /run/<project>/nginx/nginx.sock.

    0750 caused 502 on every public request after the per-site nginx layout
    change moved the socket under /run/<project>/nginx/.
    """
    runtime_nginx = helpers.read(helpers.SRC_DIR / "bonesinfra/deploys/runtime/nginx.py")
    # Both runtime dir mkdirs must use 0711; the conf dir (0750) is unrelated.
    socket_dir_block = runtime_nginx.split('path=paths["runtime_socket_dir"]')[1].split(")")[0]
    helpers.assert_contains(socket_dir_block, 'mode="0711"')
    nginx_dir_block = runtime_nginx.split('path=paths["runtime_nginx_dir"]')[1].split(")")[0]
    helpers.assert_contains(nginx_dir_block, 'mode="0711"')

    common_paths = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/common/paths.py")
    helpers.assert_contains(common_paths, 'mode="0711"')
    helpers.assert_not_contains(common_paths, 'mode="0750"')

    common_nginx = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/common/nginx.py")
    helpers.assert_contains(common_nginx, 'mode="0711"')
    helpers.assert_not_contains(common_nginx, 'mode="0750"')


def test_site_nginx_service_runtime_dir_is_traversable():
    """The per-site nginx RuntimeDirectory must be 0711 so www-data can
    traverse into /run/<project>/nginx/ to reach the socket."""
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/assets/nginx/site-nginx.service.j2")
    helpers.assert_contains(c, "RuntimeDirectoryMode=0711")
    helpers.assert_not_contains(c, "RuntimeDirectoryMode=0750")


def test_app_service_runtime_dir_stays_private():
    """App runtime dirs stay 0750 — only the per-site nginx (same runtime
    user) needs to reach app sockets, so no world traversal is required."""
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/common/assets/app.service.j2")
    helpers.assert_contains(c, "RuntimeDirectoryMode=0750")


def test_runtime_nginx_reloads_after_config_change():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/deploys/runtime/nginx.py")
    helpers.assert_ordering(
        c,
        "Enable router nginx site",
        "nginx -t",
        "Ensure nginx service is enabled and started",
        "Ensure per-site nginx service is enabled and started",
        "systemctl reload nginx",
    )

```

`tests/test_paths.py`:

```py
"""Paths manifest must define `build_logs` and `LOGS_DIR` for centralized log handling."""

from . import helpers

CRATES_PATHS = helpers.REPO_ROOT / "crates/shared/src/paths.rs"


def test_paths_has_build_logs_constant():
    if not CRATES_PATHS.exists():
        return
    c = helpers.read(CRATES_PATHS)
    helpers.assert_contains(c, 'pub const LOGS_DIR: &str = "logs";')
    helpers.assert_contains(c, "pub build_logs: String,")
    helpers.assert_contains(
        c,
        "build_logs: Path::new(&project_root).join(BUILD_DIR).join(LOGS_DIR).display().to_string()",
    )

```

`tests/test_pyinfra_runner.py`:

```py
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory

import pyinfra.connectors.ssh as pyinfra_ssh

from bonesinfra.domain.context import DeployContext
from bonesinfra.infra import pyinfra_runner

sentinel_key = object()


@contextmanager
def _noop_activity(_message):
    yield


def _noop_print_target(*args, **kwargs):
    del args, kwargs


def _noop_run_ops(state):
    del state


def _noop_get_private_key(*args, **kwargs):
    del args, kwargs
    return sentinel_key


def _noop_deploy(*args, **kwargs):
    del args, kwargs


def test_run_passes_ssh_auth_through_inventory(monkeypatch):
    with TemporaryDirectory() as tmp:
        config_path = Path(tmp) / "bones.toml"
        config_path.write_text(
            """
project_name = "lawsnipe"
repo_path = "/home/git/lawsnipe.git"
project_root = "/srv/sites/lawsnipe"
host = "example.com"
ssh_user = "root"
port = 2222
""".lstrip()
        )

        ctx = DeployContext.from_files(str(config_path))

    seen = {}

    monkeypatch.setattr(pyinfra_runner, "setup_output", lambda: None)
    monkeypatch.setattr(pyinfra_runner, "print_banner", lambda: None)
    monkeypatch.setattr(pyinfra_runner, "print_target", _noop_print_target)
    monkeypatch.setattr(pyinfra_runner, "print_connected", lambda: None)
    monkeypatch.setattr(pyinfra_runner, "print_done", lambda success: seen.setdefault("done", success))
    monkeypatch.setattr(pyinfra_runner, "stop_live_output", lambda: None)
    monkeypatch.setattr(pyinfra_runner, "activity", _noop_activity)
    monkeypatch.setattr(pyinfra_runner, "run_ops", _noop_run_ops)
    monkeypatch.setattr(pyinfra_ssh, "get_private_key", _noop_get_private_key)

    def fake_connect_all(state):
        host = next(iter(state.inventory))
        seen["kwargs"] = host.connector.make_paramiko_kwargs()

    monkeypatch.setattr(pyinfra_runner, "connect_all", fake_connect_all)

    pyinfra_runner.run(ctx=ctx, ssh_key="~/.ssh/id_ed25519", deploy=_noop_deploy)

    assert seen["kwargs"]["username"] == "root"
    assert seen["kwargs"]["port"] == 2222
    assert seen["kwargs"]["pkey"] is sentinel_key
    assert seen["kwargs"]["allow_agent"] is False
    assert seen["kwargs"]["look_for_keys"] is False
    assert seen["done"] is True

```

`tests/test_runtime_nginx.py`:

```py

import pytest

from bonesinfra.deploys.runtime import nginx as runtime_nginx
from bonesinfra.deploys.ssl import plan as ssl_plan
from bonesinfra.domain.context import DeployContext
from bonesinfra.domain.paths import DeploymentPaths


def _make_ctx(tmp_path, *, domain: str = "", preview_domain: str = "preview.example.com"):
    config_path = tmp_path / "bones.toml"
    config_path.write_text(
        f"""
project_name = "lawsnipe"
repo_path = "/home/git/lawsnipe.git"
project_root = "/srv/sites/lawsnipe"
host = "example.com"
domain = "{domain}"
preview_domain = "{preview_domain}"
email = "ops@example.com"
""".lstrip()
    )
    return DeployContext.from_files(str(config_path))


def _noop(*args, **kwargs):
    del args, kwargs


def test_runtime_nginx_uses_preview_domain_when_domain_is_empty(tmp_path, monkeypatch):
    ctx = _make_ctx(tmp_path, domain="", preview_domain="preview.example.com")
    paths = DeploymentPaths.new(
        ctx.config.project_name,
        ctx.config.repo_path,
        ctx.config.project_root,
        ctx.runtime.web_root,
    ).__dict__
    calls = []

    monkeypatch.setattr(runtime_nginx, "mkdir", _noop)
    monkeypatch.setattr(runtime_nginx.files, "link", _noop)
    monkeypatch.setattr(runtime_nginx.server, "shell", _noop)
    monkeypatch.setattr(runtime_nginx.systemd, "daemon_reload", _noop)

    def fake_render(*args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr(runtime_nginx, "render", fake_render)

    runtime_nginx.setup(ctx, paths, tmp_path)

    router_call = next(call for _, call in calls if "nginx_server_name" in call)
    assert router_call["nginx_server_name"] == "preview.example.com"
    assert router_call["preview_domain"] == "preview.example.com"


def test_runtime_nginx_requires_a_real_name(tmp_path, monkeypatch):
    ctx = _make_ctx(tmp_path, domain="", preview_domain="")
    paths = DeploymentPaths.new(
        ctx.config.project_name,
        ctx.config.repo_path,
        ctx.config.project_root,
        ctx.runtime.web_root,
    ).__dict__

    monkeypatch.setattr(runtime_nginx, "mkdir", _noop)
    monkeypatch.setattr(runtime_nginx.files, "link", _noop)
    monkeypatch.setattr(runtime_nginx.server, "shell", _noop)
    monkeypatch.setattr(runtime_nginx.systemd, "daemon_reload", _noop)
    monkeypatch.setattr(runtime_nginx, "render", _noop)

    with pytest.raises(ValueError, match="domain or preview_domain"):
        runtime_nginx.setup(ctx, paths, tmp_path)


def test_ssl_setup_requires_a_real_domain(tmp_path):
    ctx = _make_ctx(tmp_path, domain="", preview_domain="preview.example.com")

    with pytest.raises(SystemExit, match="1"):
        ssl_plan.deploy_ssl(ctx)

```

`tests/test_runtimes.py`:

```py
import importlib

from bonesinfra.app import runtime_catalog
from bonesinfra.runtimes import list_runtimes

from . import helpers

RUNTIMES_MODULES = {
    "laravel": "bonesinfra.runtimes.laravel",
    "django": "bonesinfra.runtimes.django.django",
    "next": "bonesinfra.runtimes.next.next",
    "nuxt": "bonesinfra.runtimes.nuxt.nuxt",
    "rails": "bonesinfra.runtimes.rails.rails",
    "sveltekit": "bonesinfra.runtimes.sveltekit.svelte",
    "vue": "bonesinfra.runtimes.vue.vue",
}


def test_runtimes_have_questions_and_deploy():
    for name, module_path in RUNTIMES_MODULES.items():
        mod = importlib.import_module(module_path)
        assert callable(getattr(mod, "questions", None)), f"{name}: missing questions()"
        assert callable(getattr(mod, "deploy", None)), f"{name}: missing deploy()"


def test_runtime_registry_is_explicit():
    assert list_runtimes() == sorted(RUNTIMES_MODULES)


def test_laravel_questions_are_exposed():
    assert runtime_catalog.get_questions("laravel")


def test_laravel_deploy_accepts_ctx():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/deploy.py")
    helpers.assert_contains(content, "def deploy(ctx):", "laravel deploy must accept ctx")


def test_laravel_php_fpm_uses_distro_pool_model():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/php_fpm.py")
    helpers.assert_contains(content, "php_fpm_pool.render_pool")
    helpers.assert_contains(content, "php_fpm_pool.validate_php_fpm")
    helpers.assert_contains(content, "php_fpm_pool.reload_php_fpm")


def test_laravel_php_fpm_does_not_use_custom_service():
    """Regression guard: Laravel must not render or start a per-project
    php-fpm systemd service, nor validate via a custom --fpm-config."""
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/php_fpm.py")
    helpers.assert_not_contains(content, "site-php-fpm.service.j2")
    helpers.assert_not_contains(content, "-php-fpm.service")
    helpers.assert_not_contains(content, "--fpm-config")
    helpers.assert_not_contains(content, "apparmor")


def test_laravel_deploy_does_not_setup_php_fpm_apparmor():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/deploy.py")
    helpers.assert_not_contains(content, "apparmor.setup_php_fpm")
    helpers.assert_not_contains(content, "apparmor")


def test_common_php_fpm_pool_socket_path_is_distro_standard():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/common/php_fpm_pool.py")
    helpers.assert_contains(content, '"/run/php"')
    helpers.assert_contains(content, "fpm/pool.d/{project}.conf")
    helpers.assert_contains(content, "php-fpm{php_version} --test")
    helpers.assert_contains(content, "php{php_version}-fpm")


def test_common_php_fpm_pool_ensures_bonesdeploy_log_dir():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/common/php_fpm_pool.py")
    helpers.assert_contains(content, "logs.ensure(ctx)")


def test_laravel_nginx_uses_distro_php_socket_and_no_runtime_chown():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/nginx.py")
    helpers.assert_contains(content, "php_fpm_pool.socket_path")
    helpers.assert_not_contains(content, "runtime_socket_dir")
    helpers.assert_not_contains(content, "files.directory")


def test_common_validation_runs_as_runtime_user_not_root():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/common/validation.py")
    helpers.assert_contains(content, "_sudo_user=user")
    helpers.assert_contains(content, "def run_as_runtime_user(ctx, name, command):")


def test_common_logs_provisions_runtime_owned_dir():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/common/logs.py")
    helpers.assert_contains(content, "/var/log/bonesdeploy")
    helpers.assert_contains(content, "user=ctx.runtime.runtime_user")
    helpers.assert_contains(content, 'name="Ensure BonesDeploy log root exists"')


def test_template_runtime_load_fails_loudly_without_silent_swallow():
    content = helpers.read(
        helpers.SRC_DIR / "bonesinfra/deploys/runtime/template_runtime.py"
    )
    helpers.assert_not_contains(content, "except (ImportError, KeyError)")
    helpers.assert_not_contains(content, "    pass")
    helpers.assert_contains(content, 'raise RuntimeError(f"Runtime {template} does not expose deploy(ctx)")')


def test_template_runtime_load_requires_deploy_attribute():
    content = helpers.read(
        helpers.SRC_DIR / "bonesinfra/deploys/runtime/template_runtime.py"
    )
    helpers.assert_contains(content, 'if not hasattr(runtime, "deploy")')


def test_all_runtimes_use_common_service_layer():
    """Non-Laravel dynamic runtimes must wire through common.service, not pass."""
    runtime_to_module_file = {
        "django": "bonesinfra/runtimes/django/django.py",
        "next": "bonesinfra/runtimes/next/next.py",
        "nuxt": "bonesinfra/runtimes/nuxt/nuxt.py",
        "rails": "bonesinfra/runtimes/rails/rails.py",
        "sveltekit": "bonesinfra/runtimes/sveltekit/svelte.py",
        "vue": "bonesinfra/runtimes/vue/vue.py",
    }
    for name, rel in runtime_to_module_file.items():
        content = helpers.read(helpers.SRC_DIR / rel)
        helpers.assert_not_contains(content, "    pass", msg=name)
        helpers.assert_contains(content, "service.runtime_paths(ctx)", msg=name)


def test_vue_is_static_only():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/vue/vue.py")
    helpers.assert_contains(content, "nginx.render_static")
    helpers.assert_not_contains(content, "render_app_service")


def test_next_uses_tcp_localhost():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/next/next.py")
    helpers.assert_contains(content, "HOSTNAME=127.0.0.1")
    helpers.assert_contains(content, "port=port")
    helpers.assert_contains(content, 'runtime_address_families="AF_UNIX AF_INET"')


def test_nuxt_uses_nitro_unix_socket():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/nuxt/nuxt.py")
    helpers.assert_contains(content, "NITRO_UNIX_SOCKET=")
    helpers.assert_contains(content, "socket_path=socket_path")


def test_sveltekit_uses_socket_path_env():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/sveltekit/svelte.py")
    helpers.assert_contains(content, "SOCKET_PATH=")
    helpers.assert_contains(content, "ORIGIN=")


def test_django_uses_gunicorn_unix_socket():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/django/django.py")
    helpers.assert_contains(content, "gunicorn")
    helpers.assert_contains(content, "--bind unix:")
    helpers.assert_contains(content, "wsgi_module")
    helpers.assert_not_contains(content, "python3-gunicorn")


def test_app_runtimes_use_per_service_socket_leaf():
    """Each app runtime must place its socket in its own leaf dir under
    /run/<project>/<runtime>/, not in the shared /run/<project>/."""
    for slug, rel in [
        ("gunicorn", "bonesinfra/runtimes/django/django.py"),
        ("puma", "bonesinfra/runtimes/rails/rails.py"),
        ("nuxt", "bonesinfra/runtimes/nuxt/nuxt.py"),
        ("sveltekit", "bonesinfra/runtimes/sveltekit/svelte.py"),
    ]:
        content = helpers.read(helpers.SRC_DIR / rel)
        helpers.assert_contains(
            content,
            f"runtime_socket_dir']}}/{slug}/{slug}.sock",
            msg=slug,
        )


def test_rails_uses_puma_unix_socket():
    content = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/rails/rails.py")
    helpers.assert_contains(content, "bundle exec puma")
    helpers.assert_contains(content, "-b unix://")

```

`tests/test_syntax.py`:

```py
"""All .py files under infra/ must parse without syntax errors."""

from . import helpers


def test_all_source_files_parse():
    for root in (helpers.INFRA_DIR, helpers.SRC_DIR):
        for file in sorted(root.rglob("*.py")):
            helpers.compile_module(file)

```

`tests/test_templates_j2.py`:

```py
"""J2 template file existence and content assertions."""

from . import helpers

N = helpers.SRC_DIR / "bonesinfra"


def _read(name):
    return helpers.read(N / name)


# ---- Base AppArmor profile ----


def test_apparmor_profile_allows_resolved_web_root():
    c = _read("assets/apparmor/project-nginx-profile.j2")
    helpers.assert_contains(c, "{{ paths.current_web_root }}/** r,")
    helpers.assert_contains(c, "{{ paths.releases }}/*/{{ web_root }}/** r,")


def test_apparmor_profile_allows_site_nginx_conf():
    c = _read("assets/apparmor/project-nginx-profile.j2")
    helpers.assert_contains(c, "{{ paths.site_nginx_config }} r,")


def test_apparmor_profile_allows_repo_bones_toml():
    c = _read("assets/apparmor/project-nginx-profile.j2")
    helpers.assert_contains(c, "{{ paths.repo_bones_toml }} r,")


def test_apparmor_profile_does_not_deny_home_globally():
    c = _read("assets/apparmor/project-nginx-profile.j2")
    helpers.assert_not_contains(c, "deny /home/** r,")
    helpers.assert_not_contains(c, "deny /home/{{ deploy_user }}/** r,")


def test_apparmor_profile_limits_network_to_unix_stream():
    c = _read("assets/apparmor/project-nginx-profile.j2")
    helpers.assert_contains(c, "network unix stream,")
    helpers.assert_not_contains(c, "network inet stream,")
    helpers.assert_not_contains(c, "network inet6 stream,")


# ---- Base nginx service template ----


def test_nginx_service_sets_apparmor_profile():
    c = _read("assets/nginx/site-nginx.service.j2")
    helpers.assert_contains(c, "AppArmorProfile=")


def test_nginx_service_waits_for_apparmor():
    c = _read("assets/nginx/site-nginx.service.j2")
    helpers.assert_contains(c, "After=network.target apparmor.service")
    helpers.assert_contains(c, "Requires=apparmor.service")


# ---- Base nginx config ----


def test_site_nginx_config_logs_under_runtime_nginx_dir():
    c = _read("assets/nginx/site-nginx.conf.j2")
    helpers.assert_contains(c, "error_log {{ paths.runtime_nginx_dir }}/error.log")
    helpers.assert_contains(c, "access_log {{ paths.runtime_nginx_dir }}/access.log")
    helpers.assert_not_contains(c, "access_log stderr")


# ---- Router nginx config ----


def test_router_config_uses_resolved_socket_path():
    c = _read("assets/nginx/router.conf.j2")
    helpers.assert_contains(c, "{{ paths.runtime_nginx_socket }}")
    helpers.assert_not_contains(c, "default_server")


# ---- Laravel PHP-FPM pool config ----


def test_laravel_php_fpm_pool_has_no_global_section():
    c = _read("runtimes/laravel/assets/php/php-fpm-pool.conf.j2")
    helpers.assert_not_contains(c, "[global]")
    helpers.assert_not_contains(c, "daemonize")
    helpers.assert_not_contains(c, "/var/log/php-fpm.log")


def test_laravel_php_fpm_pool_uses_distro_run_php_socket():
    c = _read("runtimes/laravel/assets/php/php-fpm-pool.conf.j2")
    helpers.assert_contains(c, "listen = {{ laravel_php_fpm_socket_path }}")
    helpers.assert_not_contains(c, "{{ paths.runtime_socket_dir }}")
    helpers.assert_not_contains(c, "/run/{{ project_name }}")


def test_laravel_php_fpm_pool_listens_as_www_data():
    c = _read("runtimes/laravel/assets/php/php-fpm-pool.conf.j2")
    helpers.assert_contains(c, "listen.owner = www-data")
    helpers.assert_contains(c, "listen.group = www-data")
    helpers.assert_contains(c, "listen.mode = 0660")


def test_laravel_php_fpm_pool_runs_as_runtime_user():
    c = _read("runtimes/laravel/assets/php/php-fpm-pool.conf.j2")
    helpers.assert_contains(c, "user = {{ runtime_user }}")
    helpers.assert_contains(c, "group = {{ runtime_group }}")


def test_laravel_php_fpm_pool_logs_under_bonesdeploy():
    c = _read("runtimes/laravel/assets/php/php-fpm-pool.conf.j2")
    helpers.assert_contains(c, "/var/log/bonesdeploy/{{ project_name }}/php-worker-error.log")
    helpers.assert_contains(c, "access.log = /var/log/bonesdeploy/{{ project_name }}/php-fpm-access.log")
    helpers.assert_contains(c, "slowlog = /var/log/bonesdeploy/{{ project_name }}/php-fpm-slow.log")
    helpers.assert_not_contains(c, "{{ paths.runtime_socket_dir }}")


def test_laravel_php_fpm_pool_uses_resolved_current_path():
    c = _read("runtimes/laravel/assets/php/php-fpm-pool.conf.j2")
    helpers.assert_contains(c, "chdir = {{ paths.current }}")
    helpers.assert_contains(c, "catch_workers_output = yes")
    helpers.assert_contains(c, "php_admin_flag[log_errors] = on")


# ---- Laravel nginx config ----


def test_laravel_nginx_prefers_php_over_html():
    c = _read("runtimes/laravel/assets/nginx/laravel-site-nginx.conf.j2")
    helpers.assert_contains(c, "index index.php index.html;")


def test_laravel_nginx_uses_absolute_fastcgi_params():
    c = _read("runtimes/laravel/assets/nginx/laravel-site-nginx.conf.j2")
    helpers.assert_contains(c, "include /etc/nginx/fastcgi_params;")
    helpers.assert_not_contains(c, "include fastcgi_params;")


def test_laravel_nginx_uses_resolved_path_manifest():
    c = _read("runtimes/laravel/assets/nginx/laravel-site-nginx.conf.j2")
    helpers.assert_contains(c, "pid {{ paths.runtime_nginx_pid }}")
    helpers.assert_contains(c, "listen unix:{{ paths.runtime_nginx_socket }}")
    helpers.assert_contains(c, "root {{ paths.current_web_root }}")
    helpers.assert_contains(c, "{{ paths.runtime_nginx_dir }}/")
    helpers.assert_not_contains(c, "/run/{{ project_name }}")
    helpers.assert_not_contains(c, "{{ project_root }}/current/{{ web_root }}")


def test_laravel_nginx_logs_under_runtime_nginx_dir():
    c = _read("runtimes/laravel/assets/nginx/laravel-site-nginx.conf.j2")
    helpers.assert_contains(c, "error_log {{ paths.runtime_nginx_dir }}/error.log")
    helpers.assert_contains(c, "access_log {{ paths.runtime_nginx_dir }}/access.log")
    helpers.assert_not_contains(c, "access_log stderr")


# ---- Common app service template ----


def test_common_app_service_runs_as_runtime_user():
    c = _read("runtimes/common/assets/app.service.j2")
    helpers.assert_contains(c, "User={{ runtime_user }}")
    helpers.assert_contains(c, "Group={{ runtime_group }}")
    helpers.assert_contains(c, "SupplementaryGroups={{ release_group }}")
    helpers.assert_contains(c, "WorkingDirectory={{ paths.current }}")
    helpers.assert_contains(c, "RuntimeDirectory={{ project_name }}/{{ runtime_name }}")
    helpers.assert_contains(c, "RuntimeDirectoryMode=0750")
    helpers.assert_contains(c, "EnvironmentFile=-{{ paths.conf_root }}/runtime.env")
    helpers.assert_contains(c, "ExecStart={{ runtime_exec }}")
    helpers.assert_contains(c, "AppArmorProfile={{ apparmor_profile_name }}")


def test_common_app_service_is_tight_sandbox():
    c = _read("runtimes/common/assets/app.service.j2")
    helpers.assert_contains(c, "NoNewPrivileges=yes")
    helpers.assert_contains(c, "PrivateTmp=yes")
    helpers.assert_contains(c, "ProtectHome=yes")
    helpers.assert_contains(c, "ProtectSystem=strict")
    helpers.assert_contains(c, "RestrictNamespaces=yes")
    helpers.assert_contains(c, "LockPersonality=yes")
    helpers.assert_contains(c, "RestrictRealtime=yes")
    helpers.assert_contains(c, "SystemCallArchitectures=native")
    helpers.assert_contains(c, "CapabilityBoundingSet=")
    helpers.assert_contains(c, "AmbientCapabilities=")
    helpers.assert_contains(c, "PrivateDevices=yes")
    helpers.assert_contains(c, "ProtectKernelTunables=yes")
    helpers.assert_contains(c, "ProtectKernelModules=yes")
    helpers.assert_contains(c, "ProtectControlGroups=yes")
    helpers.assert_contains(c, 'RestrictAddressFamilies={{ runtime_address_families | default("AF_UNIX") }}')


def test_common_app_service_writes_to_runtime_and_logs_dirs():
    c = _read("runtimes/common/assets/app.service.j2")
    helpers.assert_contains(c, "ReadOnlyPaths={{ paths.current }}")
    helpers.assert_contains(
        c,
        "ReadWritePaths={{ paths.runtime_socket_dir }}/{{ runtime_name }} "
        "{{ runtime_write_paths }} /var/log/bonesdeploy/{{ project_name }}",
    )
    helpers.assert_contains(c, "StandardOutput=journal")
    helpers.assert_contains(c, "StandardError=journal")
    helpers.assert_contains(c, "Restart=always")
    helpers.assert_contains(c, "RestartSec=2")
    helpers.assert_contains(c, "WantedBy=multi-user.target")


# ---- Common app nginx proxy template ----


def test_common_app_nginx_proxies_to_socket():
    c = _read("runtimes/common/assets/app-site-nginx.conf.j2")
    helpers.assert_contains(c, "proxy_pass {{ app_proxy_target }}")
    helpers.assert_contains(c, "proxy_set_header Host $host")
    helpers.assert_contains(c, "proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for")
    helpers.assert_contains(c, "proxy_set_header X-Forwarded-Proto $scheme")
    helpers.assert_contains(c, "proxy_set_header X-Real-IP $remote_addr")
    helpers.assert_contains(c, "proxy_http_version 1.1")
    helpers.assert_contains(c, 'proxy_set_header Connection ""')


def test_common_app_nginx_logs_under_runtime_nginx_dir():
    c = _read("runtimes/common/assets/app-site-nginx.conf.j2")
    helpers.assert_contains(c, "error_log {{ paths.runtime_nginx_dir }}/error.log")
    helpers.assert_contains(c, "access_log {{ paths.runtime_nginx_dir }}/access.log")
    helpers.assert_not_contains(c, "access_log stderr")


# ---- Common static nginx template ----


def test_common_static_nginx_serves_dist():
    c = _read("runtimes/common/assets/static-site-nginx.conf.j2")
    helpers.assert_contains(c, "root {{ paths.current }}/dist")
    helpers.assert_contains(c, "index index.html")
    helpers.assert_contains(c, "try_files $uri $uri/ /index.html")


def test_common_static_nginx_has_no_proxy_pass():
    c = _read("runtimes/common/assets/static-site-nginx.conf.j2")
    helpers.assert_not_contains(c, "proxy_pass")


# ---- Common app AppArmor profile ----


def test_common_apparmor_profile_includes_exec_paths():
    c = _read("runtimes/common/assets/app-profile.j2")
    helpers.assert_contains(c, "{{ apparmor_profile_name }}")
    helpers.assert_contains(c, "{% for exec_path in apparmor_exec_paths %}")
    helpers.assert_contains(c, "mrix")


def test_common_apparmor_profile_allows_runtime_and_log_dirs():
    c = _read("runtimes/common/assets/app-profile.j2")
    helpers.assert_contains(c, "{{ paths.runtime_socket_dir }}/{{ apparmor_runtime }}/ rw,")
    helpers.assert_contains(c, "{{ paths.runtime_socket_dir }}/{{ apparmor_runtime }}/** rwk,")
    helpers.assert_contains(c, "/var/log/bonesdeploy/{{ project_name }}/ rw,")
    helpers.assert_contains(c, "/var/log/bonesdeploy/{{ project_name }}/** rwk,")


def test_common_apparmor_profile_uses_configurable_network():
    c = _read("runtimes/common/assets/app-profile.j2")
    helpers.assert_contains(c, '{{ apparmor_network | default("network unix stream,") }}')


def test_common_apparmor_profile_denies_root_and_ssh():
    c = _read("runtimes/common/assets/app-profile.j2")
    helpers.assert_contains(c, "deny /root/** r,")
    helpers.assert_contains(c, "deny /etc/ssh/** r,")

```

`tests/test_tripwires.py`:

```py
"""Files and directories that must NOT exist (removed in migrations)."""

from . import helpers

R = helpers.REPO_ROOT
SRC = R / "crates/bonesdeploy/src"
CRATES_EXIST = R.joinpath("crates").is_dir()


def test_old_embeds_runtimes_dir_is_removed():
    helpers.assert_file_not_exists(R / "crates/bonesdeploy/embeds/runtimes")


def test_old_embeds_kit_dir_is_removed():
    helpers.assert_file_not_exists(R / "crates/bonesdeploy/embeds/kit")


def test_old_operations_py_does_not_exist():
    for p in ("infra/src/operations.py", "infra/runtime/operations.py"):
        helpers.assert_file_not_exists(R / p)


def test_pyinfra_rs_is_deleted():
    helpers.assert_file_not_exists(SRC / "pyinfra.rs")


def test_main_rs_has_no_pyinfra_mod():
    if not CRATES_EXIST:
        return
    c = helpers.read(SRC / "main.rs")
    helpers.assert_not_contains(c, "mod pyinfra;")


def test_no_managed_pyinfra_in_shared_paths():
    if not CRATES_EXIST:
        return
    c = helpers.read(R / "crates/shared/src/paths.rs")
    helpers.assert_not_contains(c, "managed_pyinfra_venv_dir")
    helpers.assert_not_contains(c, "managed_pyinfra_binary")


def test_config_rs_no_deploy_constants():
    if not CRATES_EXIST:
        return
    c = helpers.read(R / "crates/bonesdeploy/src/config.rs")
    helpers.assert_not_contains(c, "BONES_REMOTE_SSL_DEPLOY")
    helpers.assert_not_contains(c, "BONES_REMOTE_SETUP_DEPLOY")


def test_embedded_rs_no_removed_functions():
    if not CRATES_EXIST:
        return
    c = helpers.read(R / "crates/bonesdeploy/src/embedded.rs")
    helpers.assert_not_contains(c, "struct Runtimes")
    helpers.assert_not_contains(c, "fn scaffold_runtime_template")
    helpers.assert_not_contains(c, "fn read_template_runtime_config")
    helpers.assert_not_contains(c, "fn available_templates")


def test_cli_has_apply_handlers():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/cli/app.py")
    helpers.assert_contains(c, "setup_apply_cmd")
    helpers.assert_contains(c, "runtime_apply_cmd")
    helpers.assert_contains(c, "ssl_apply_cmd")


def test_cli_has_no_unimplemented():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/cli/app.py")
    helpers.assert_not_contains(c, "UnimplementedError")


def test_infra_has_pyinfra_runner():
    helpers.assert_file_exists(helpers.SRC_DIR / "bonesinfra/infra/pyinfra_runner.py")


def test_infra_has_paths():
    helpers.assert_file_exists(helpers.SRC_DIR / "bonesinfra/domain/paths.py")

```
```

`docs/slop-refactor.md`:

```md
I've audited the workspace. Below is a refactor plan that follows AGENTS.md (lazy: deletion-first, no unrequested abstraction, no new deps, fewest files, `ponytail:` for shortcuts, strict at trust boundaries). This plan also reflects the clarifications we made while discussing SSH, `bonesinfra`, and repo housekeeping. I'm explicitly **rejecting** the 5-layer `cli/app/domain/infra/ui` restructure proposed in `docs/refactor-code.md` — it adds folders and indirection for no behavior gain, which violates AGENTS.md.

## Clarified decisions

- **Keep `__trash__/`.** It is intentional personal workspace storage, not project slop.
- **Keep `openssh`.** We only need simple remote commands, but `openssh` still buys us cross-platform behavior and is acceptable.
- **Do not revisit `KnownHosts::Accept` right now.** Earlier concern noted, but current behavior is acceptable for this project.
- **Do not add `bonesinfra` GPG verification in this refactor.** The supply-chain concern is real, but it is deferred into `docs/bonesinfra-verification.md`.
- **Do not force a `port` schema change.** The practical issue is duplicated parsing, not whether the config stores a string or integer.
- **Proceed with the rest of the cleanup plan.** Dead code, duplication, wrapper collapse, path cleanup, and test guardrail fixes are still in scope.

## Audit summary

59 `.rs` files, ~6,440 lines. Concrete slop found:
- **~400 lines of dead code**: `bonesremote/commands/manage.rs` (344, not in `mod.rs`, references nonexistent `cfg.data`), `shared::config::{Permissions, PathOverride}` (never referenced).
- **Two cleancode guardrails are no-ops**: `no_literal_wrapped_fallback` + `no_manufactured_success` scan `tests/cleancode/src/` instead of `crates/` (they only pass against themselves).
- **Committed build artifacts**: `bin/bonesdeploy` + `bin/bonesremote` (5.5 MB) reproducible by `compile.sh`.
- **Two deferred trust discussions and one immediate trust gap**: SSH host behavior is accepted for now, `bonesinfra` verification is deferred into a separate document, and `which`-resolved paths written into sudoers still need canonicalization.
- **Pervasive duplication**: `port: String` re-parsed in 2 sites + passed raw in 6; rsync invocation triplicated; `remote_bones_toml` built 2 ways; `runtime.toml` parsed by 2 types in 2 crates; hand-rolled TOML parser in `update.rs` reinvents the `toml` dep; `prompts::confirm_with_lines` reinvents `inquire::Confirm` used in the same file; defaulting expression ×7 in prompts.
- **Over-abstraction**: `release/scripts.rs` builds a generic `DeploymentRun<Out,Err>` + `ConsoleTargets` + `SharedWriter` + `TeeWriter` layer purely so tests can inject a `Cursor`. `config::Constants` Java-ism. ~10 single-field/one-line wrapper fns/structs.
- **No `ponytail:` markers anywhere** despite AGENTS.md requirement, on: rsync stdout parsing, `prune_old_releases` O(n²) re-sort, exec-by-path-prefix heuristic, `home_dir` `/root` fallback, URL hand-parsers, hardcoded `DEFAULT_WEB_ROOT` in `release_state`.
- **`test_init_project.rs`** is a full fixture harness (TempDir + git subprocess + `Mutex`+`OnceLock` + `unsafe env::set_var`) where AGENTS.md asks for the smallest runnable check; `test_doctor.rs` is the on-spec counterexample sitting right next to it.

## Proposed plan — deletion-first, 6 passes, small boring commits

### Pass 1 — Pure deletions (zero behavior change, ~450 lines gone)
1. Delete `crates/bonesremote/src/commands/manage.rs` (dead).
2. Delete `Permissions` + `PathOverride` from `shared/src/config.rs`.
3. Delete `bin/bonesdeploy` + `bin/bonesremote`; add `bin/` to `.gitignore`.
4. Delete WHAT comments and doc-comments that restate test/function names (pervasive, ~40 sites).
5. Delete `docs/refactor-code.md` (its proposed restructure violates AGENTS.md and we're not doing it).

### Pass 2 — Collapse wrappers and the `Constants` Java-ism
6. Delete `config::Constants` in both crates; use `shared::paths::*` consts directly.
7. Delete one-line forwarders: `init_project::collect`, `init_project::collect_non_interactive` (cfg-test), `bonesinfra::checkout_path`, `remote_data::setup`, `config::default_project_root_for`, `release_state::{deployment_paths, build_root, shared_dir, current_link}`, `wire_release::{shared_path_exists, release_path_is_resolved}` (identical dup).
8. Delete single-use wrapper structs: `InitOutcome` (return `bool`), `NonInteractiveValues`, `PullTarget` (use existing `git::RemoteConnectionDetails`).
9. Delete `release/scripts.rs` generic abstraction; `run_deployment_script` writes directly to `io::stdout()`/`io::stderr()`; rewrite the 4 tests as plain asserts against captured output (no `Cursor`/`Arc<Mutex>`/`TeeWriter`).
10. Delete `prompts::confirm_with_lines`; use `inquire::Confirm` (already a dep, already used in the file).
11. Delete `main.rs` `pub(crate) use infra::{...}` / `use ui::prompts` re-exports; callers use real paths.

### Pass 3 — De-duplicate
12. Keep `Bones.port` compatible as-is and add one shared parse helper; delete the duplicated `ssh.rs:10` + `update_release.rs:56` parse logic.
13. Add one `infra::rsync` helper; rewrite `push_state`, `pull_state`, `doctor::check_rsync_sync` to use it.
14. Standardize `remote_bones_toml` via `cfg.deployment_paths(...).repo_bones_toml` everywhere (rollback, manage-via-deploy, deploy).
15. Delete `wire_release::load_runtime_shared_paths` + local `RuntimeShared`; use `shared::config::load_runtime`.
16. Replace `update::parse_package_version` hand-parser with the `toml` crate (already installed).
17. Collapse `cli_or_prompt` / `cli_existing_or_prompt` into one fn.
18. Collapse the 7-copy `existing.map(...).filter(!empty).unwrap_or(default)` defaulting into one helper.
19. `git::list_remotes_with_urls` → parse `git remote -v` once (kills N+1 spawns).
20. Delete the 3 near-duplicated test config builders and 7 temp_dir helpers; one tiny helper per crate.

### Pass 4 — Trust boundaries (AGENTS.md: not lazy here)
21. Leave SSH trust behavior alone for now. Keep `openssh` and current `KnownHosts::Accept` behavior.
22. `bonesremote::init::which_bonesdeploy_remote`: canonicalize the resolved path before writing it into `/etc/sudoers.d/bonesdeploy`; reject if not under a sane root (`/usr/local/bin`, `/usr/bin`). `ponytail:` if we keep an allowlist.
23. Document the `bonesinfra` verification concern separately and defer implementation. See `docs/bonesinfra-verification.md`.
24. Validate `host` (hostname charset) at config load / remote-inference time, before it flows into any shell string.

### Pass 5 — `ponytail:` markers for kept shortcuts
25. Add `ponytail:` comments naming the ceiling + upgrade path for: `doctor::check_rsync_sync` stdout parsing, `post_deploy::prune_old_releases` O(n²) re-sort, `embedded::write_asset` exec-by-path-prefix, `python::runtime_defaults` hard-coded internal path, `paths::home_dir` `/root` fallback, `git::parse_ssh_style_url`/`parse_scp_style_url` (no IPv6 / percent-encoding), `release_state::deployment_paths` hardcoded `DEFAULT_WEB_ROOT`.

### Pass 6 — Fix the cleancode guardrails (so they actually enforce)
26. Fix `no_literal_wrapped_fallback` + `no_manufactured_success` to scan `crates/` (currently scanning themselves).
27. Extract one shared `collect_source_files` walker; unify skip lists (add `__trash__`, `.worktrees`).
28. Reconsider `no_legacy_terms` substring blacklist — either drop it or scope to identifiers only (it currently flags honest doc comments).
29. Add a guardrail: `shared::paths` must not grow past N lines / `Deployment` field count (prevents regression).
30. Strip `test_init_project.rs` harness for the pure-function tests; keep one minimal integration check.

## What I'm explicitly NOT doing (and why)
- **No 5-layer `cli/app/domain/infra/ui` restructure.** AGENTS.md: "No abstractions that weren't explicitly requested... Deletion over addition... Fewest files possible." The current `cli/`+`commands/`+`infra/`+`ui/` shape is fine once the slop is gone. `docs/refactor-code.md` proposes the opposite philosophy and should be deleted.
- **No adapter traits** for git/ssh/rsync/process. Folder boundary is enough.
- **No splitting `shared::paths`** into a `paths/` module tree. 270 lines, under the 400-line guardrail.
- **No new dependencies.** Everything above uses stdlib or already-installed crates (`toml`, `inquire`, `openssh`, `rust-embed`, `syn`).

## Order of risk
Pass 1 is pure deletion (safe). Pass 2 is mostly mechanical. Pass 3 stays lower risk now that `port` compatibility is preserved instead of forcing a schema change. Pass 4 is still security-sensitive, but SSH policy changes are explicitly out of scope for this pass. Pass 6 changes test behavior.

```

`rustfmt.toml`:

```toml
# Stable options
max_width = 120
hard_tabs = false
tab_spaces = 4
newline_style = "Unix"
edition = "2021"
use_small_heuristics = "Max"

# Unstable options (require nightly or config flag)
# Uncomment when using nightly toolchain:
# imports_granularity = "Module"       # merge imports from the same module
# group_imports = "StdExternalCrate"   # group: std → external → crate
# use_field_init_shorthand = true      # prefer Point { x, y } over Point { x: x, y: y }
# format_code_in_doc_comments = true   # format Rust code inside doc comments
# wrap_comments = true                 # wrap long comments to max_width
# normalize_comments = true            # normalize /* */ to //
# format_strings = true                # break long string literals
# condense_wildcard_suffixes = true    # simplify nested wildcard patterns
# overflow_delimited_expr = true       # allow long macro/function args to overflow

```

`tests/ASSERTIONS.md`:

```md
# Test Assertions Inventory

> Note: this file is auto-generated by `cargo assertions`.

## `crates/bonesdeploy/src/commands/manage.rs`
- Escapes embedded single quotes safely for remote shell execution. (shell_quote_single_escapes_embedded_single_quotes)
- Returns an explicit empty string for empty input, not a zero-length argument. (shell_quote_single_handles_empty_string)
- Wraps a plain value in single quotes to prevent whitespace and token splitting. (shell_quote_single_wraps_plain_value_in_single_quotes)

## `crates/bonesdeploy/src/commands/remote_data.rs`
- base data includes preview domain. (base_data_includes_preview_domain)
- Passes the SSL domain and email into the deploy data sent to the infra CLI. (ssl_data_includes_domain_and_email)

## `crates/bonesdeploy/src/commands/tests/test_init_project.rs`
- Requires a host when neither seed config nor CLI provide one. (collect_non_interactive_requires_host_when_seed_and_cli_are_missing_it)
- Uses seed config and CLI values without prompting when non-interactive mode is active. (collect_non_interactive_uses_seed_and_cli_values_without_prompting)
- Materializes the base bonesdeploy kit and runtime config during init. (init_materializes_base_bones_assets)
- Keeps an already materialized local bones scaffold intact when init is run again. (init_rerun_preserves_existing_bones_assets)

## `crates/bonesdeploy/src/commands/update.rs`
- Extracts the package version from the `[package]` section of a Cargo manifest. (parses_package_version_from_manifest_package_section)
- Refreshes .bones scaffold assets from the cloned source tree without overwriting local config files. (refresh_local_bones_updates_scaffold_without_touching_configs)
- Returns an error when the manifest has no `[package]` section with a version field. (rejects_manifest_without_package_version)
- Verifies the update source repository and branch constants are set to the canonical values. (update_uses_master_branch_source_repository)

## `crates/bonesdeploy/src/config.rs`
- load applies default project root from project name. (load_applies_default_project_root_from_project_name)
- load applies default repo path from project name. (load_applies_default_repo_path_from_project_name)
- load preserves explicit repo and project root overrides. (load_preserves_explicit_repo_and_project_root_overrides)
- save includes derived repo and project root. (save_includes_derived_repo_and_project_root)
- save persists ssl settings. (save_persists_ssl_settings)

## `crates/bonesdeploy/src/infra/bonesinfra.rs`
- checkout dir lives under bones state root. (checkout_dir_lives_under_bones_state_root)
- reset checkout removes stale directory. (reset_checkout_removes_stale_directory)
- reset checkout removes stale file. (reset_checkout_removes_stale_file)

## `crates/bonesdeploy/src/infra/bootstrap_ssh.rs`
- defaults to root. (defaults_to_root)
- trims and rejects blank values. (trims_and_rejects_blank_values)
- uses config value. (uses_config_value)

## `crates/bonesdeploy/src/infra/git.rs`
- parse remote url rejects non git paths. (parse_remote_url_rejects_non_git_paths)
- parse remote url rejects non ssh urls. (parse_remote_url_rejects_non_ssh_urls)
- parse remote url rejects relative scp paths. (parse_remote_url_rejects_relative_scp_paths)
- parse scp style url parses absolute repo path. (parse_scp_style_url_parses_absolute_repo_path)
- parse scp style url trims surrounding whitespace. (parse_scp_style_url_trims_surrounding_whitespace)
- parse ssh style url defaults port to 22. (parse_ssh_style_url_defaults_port_to_22)
- parse ssh style url parses host port and repo path. (parse_ssh_style_url_parses_host_port_and_repo_path)

## `crates/bonesdeploy/src/infra/python.rs`
- base command launches bonesinfra via uv. (base_command_launches_bonesinfra_via_uv)
- parse json output reads cli stdout. (parse_json_output_reads_cli_stdout)

## `crates/bonesdeploy/src/ui/prompts.rs`
- Accepts common yes values like y, yes, and YES. (confirmation_parser_accepts_common_yes_values)
- Rejects non-affirmative values like empty string, n, and no. (confirmation_parser_rejects_non_affirmative_values)
- Describes `AppArmor` and nginx in the remote runtime prompt. (remote_runtime_prompt_lines_include_site_runtime_concerns)
- Describes firewall configuration in the remote setup prompt. (remote_setup_prompt_lines_include_firewall_configuration)

## `crates/bonesremote/src/commands/deploy.rs`
- Removes all direct children of a directory without removing the directory itself. (clear_directory_removes_all_direct_children)
- Returns deployment script files sorted and excludes subdirectories. (list_deployment_scripts_returns_sorted_files_only)
- Replaces the release tree contents with a fresh copy from the build workspace. (publish_release_tree_replaces_release_contents_with_build_workspace)

## `crates/bonesremote/src/commands/post_deploy.rs`
- Keeps all releases when the active release count is within the keep limit. (prune_old_releases_keeps_active_release_when_within_keep_limit)
- Prunes the oldest inactive releases when the active release count exceeds the keep limit. (prune_old_releases_removes_oldest_inactive_releases_up_to_keep_limit)

## `crates/bonesremote/src/commands/post_receive.rs`
- `post-receive` checks out the requested revision into the staged build workspace. (post_receive_checks_out_requested_revision_into_build_workspace)
- `post-receive` fails with a permission error when the build workspace is inaccessible. (post_receive_reports_permission_denied_for_inaccessible_workspace)
- `post-receive` fails when the build workspace does not exist. (post_receive_requires_existing_build_workspace)

## `crates/bonesremote/src/commands/tests/test_doctor.rs`
- Accepts a yes value as indicating `AppArmor` is enabled in the kernel. (apparmor_kernel_enabled_accepts_yes)
- Rejects a no value as indicating `AppArmor` is not enabled in the kernel. (apparmor_kernel_enabled_rejects_no)
- Reads the first `AppArmor` profile assignment from a systemd unit file. (apparmor_profile_binding_reads_first_profile_assignment)
- Accepts a valid bonesdeploy `AppArmor` profile filename. (apparmor_profile_filename_accepts_bonesdeploy_profile)
- Rejects a filename that does not match the bonesdeploy profile naming convention. (apparmor_profile_filename_rejects_unrelated_file)
- Maps a bonesdeploy `AppArmor` profile name to its corresponding systemd unit name. (apparmor_unit_name_for_profile_maps_project_unit)
- Accepts a systemd unit with correctly wired `AppArmor` dependency and profile. (apparmor_unit_wiring_accepts_expected_unit_with_reordered_after_tokens)
- Rejects a systemd unit that is missing the `AppArmor` profile binding. (apparmor_unit_wiring_rejects_missing_profile_binding)
- Rejects a systemd unit that binds an unknown `AppArmor` profile. (apparmor_unit_wiring_rejects_unknown_profile_binding)

## `crates/bonesremote/src/commands/wire_release.rs`
- Removes both files and directories, including nested contents, from the build workspace. (replace_workspace_path_removes_files_and_directories)
- Rejects empty, absolute, and parent-directory paths. Allows benign double-dots in filenames (e.g. "my..dir"). (validate_shared_path_rejects_unsafe_paths)

## `crates/bonesremote/src/config.rs`
- load derives project root and repo path from project name. (load_derives_project_root_and_repo_path_from_project_name)
- load fails for invalid toml. (load_fails_for_invalid_toml)
- load fails for missing file. (load_fails_for_missing_file)
- load preserves explicit repo and project root. (load_preserves_explicit_repo_and_project_root)
- load uses defaults for missing fields. (load_uses_defaults_for_missing_fields)

## `crates/bonesremote/src/release/scripts.rs`
- deployment log path lives under build logs. (deployment_log_path_lives_under_build_logs)
- run deployment script creates missing log directory. (run_deployment_script_creates_missing_log_directory)
- run deployment script preserves failing exit status. (run_deployment_script_preserves_failing_exit_status)
- run deployment script streams output to console and log. (run_deployment_script_streams_output_to_console_and_log)
- tee writer writes to both targets. (tee_writer_writes_to_both_targets)

## `crates/bonesremote/src/release_state.rs`
- clear staged release removes state file. (clear_staged_release_removes_state_file)
- current release name resolves from current symlink. (current_release_name_resolves_from_current_symlink)
- list releases sorted returns only directories in order. (list_releases_sorted_returns_only_directories_in_order)
- point symlink atomically creates parent dirs and points to target. (point_symlink_atomically_creates_parent_dirs_and_points_to_target)
- point symlink atomically repoints existing link. (point_symlink_atomically_repoints_existing_link)
- read staged release rejects empty file. (read_staged_release_rejects_empty_file)
- write then read staged release round trips. (write_then_read_staged_release_round_trips)

## `crates/shared/src/paths.rs`
- bones config root uses xdg config home. (bones_config_root_uses_xdg_config_home)
- bones state root uses xdg state home. (bones_state_root_uses_xdg_state_home)

## `tests/cleancode/src/cleancode_file_too_long.rs`
- source files stay under 400 lines. (source_files_stay_under_400_lines)

## `tests/cleancode/src/cleancode_no_legacy_terms.rs`
- no legacy terms. (no_legacy_terms)

## `tests/cleancode/src/cleancode_no_literal_wrapped_fallback.rs`
- no literal wrapped fallback. (no_literal_wrapped_fallback)

## `tests/cleancode/src/cleancode_no_manufactured_success.rs`
- no suspicious fallback. (no_suspicious_fallback)

```

`tests/cleancode/Cargo.toml`:

```toml
[package]
name = "cleancode"
version = "0.1.0"
edition = "2024"

[dependencies]
syn = { version = "2", features = ["full", "extra-traits", "visit"] }

[lints]
workspace = true

```

`tests/cleancode/src/cleancode_file_too_long.rs`:

```rs
//! Integration test: all `.rs` source files must stay at or below 400 lines.
//!
//! This is a structural scan — no type inference needed.
//! Skips generated/dependency directories and local Git worktrees by convention.

use std::fs;
use std::path::Path;

const MAX_LINES: usize = 400;

/// Verifies all Rust source files stay at or below 400 lines.
#[test]
fn source_files_stay_under_400_lines() {
    let project_root = workspace_root();
    let mut violations: Vec<String> = Vec::new();
    let mut file_count = 0;

    visit_dirs(project_root, &mut file_count, &mut violations);

    assert!(file_count > 0, "No source files found. This test should be run from the project root.");

    assert!(violations.is_empty(), "File(s) exceed {} line(s):\n{}", MAX_LINES, violations.join("\n"),);
}

fn workspace_root() -> &'static Path {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .and_then(Path::parent)
        .expect("tests/cleancode should live under the workspace root")
}

fn visit_dirs(dir: &Path, file_count: &mut usize, violations: &mut Vec<String>) {
    let Ok(entries) = fs::read_dir(dir) else {
        return;
    };

    for entry in entries.flatten() {
        let path = entry.path();

        if path.is_dir() {
            let name = entry.file_name();
            let name_str = name.to_string_lossy();
            if matches!(name_str.as_ref(), "target" | "vendor" | "node_modules" | ".git" | ".worktrees") {
                continue;
            }
            visit_dirs(&path, file_count, violations);
            continue;
        }

        if path.extension().is_some_and(|ext| ext == "rs") {
            *file_count += 1;
            if let Ok(content) = fs::read_to_string(&path) {
                let line_count = content.lines().count();
                if line_count > MAX_LINES {
                    let relative = path.strip_prefix(workspace_root()).unwrap_or(&path);
                    violations.push(format!("  {}: {} lines (max {MAX_LINES})", relative.display(), line_count));
                }
            }
        }
    }
}

```

`tests/cleancode/src/cleancode_no_legacy_terms.rs`:

```rs
//! Integration test: detect legacy-language smell terms in Rust source.
//!
//! Flags comments, docstrings, identifiers, attributes, and string literals
//! that describe code as `legacy`, `hack`, `workaround`,
//! `backcompat`, or `deprecated`.
//!
//! This is intentionally a high-signal smell check, not a semantic analysis.

use std::fs;
use std::path::{Path, PathBuf};

const IGNORE_DIRS: &[&str] = &["target", "vendor", "node_modules", ".git"];
const LEGACY_TERMS: &[&str] = &["legacy", "hack", "workaround", "backcompat", "deprecated"];

fn collect_source_files(project_root: &Path) -> Vec<PathBuf> {
    let mut files = Vec::new();
    let mut stack: Vec<PathBuf> = vec![project_root.join("crates")];

    while let Some(dir) = stack.pop() {
        let Ok(entries) = fs::read_dir(&dir) else {
            continue;
        };

        for entry in entries.flatten() {
            let path = entry.path();
            if path.is_dir() {
                let name = entry.file_name().to_string_lossy().to_string();
                if !IGNORE_DIRS.contains(&name.as_str()) {
                    stack.push(path);
                }
            } else if path.extension().is_some_and(|ext| ext == "rs") {
                files.push(path);
            }
        }
    }

    files
}

fn terms_in_line(line: &str) -> Vec<&'static str> {
    let mut matches = Vec::new();
    let lower = line.to_ascii_lowercase();

    for term in LEGACY_TERMS {
        if lower.contains(term) {
            matches.push(*term);
        }
    }
    matches
}

/// Detects legacy-language smell terms like legacy, hack, or workaround in source code.
#[test]
fn no_legacy_terms() {
    let project_root = Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .and_then(|p| p.parent())
        .expect("cleancode crate should be two levels deep under workspace root");
    let files = collect_source_files(project_root);

    assert!(!files.is_empty(), "No source files found in crates/.");

    let mut all_violations = Vec::new();
    let mut files_scanned = 0;

    for file in &files {
        let Ok(code) = fs::read_to_string(file) else {
            continue;
        };
        files_scanned += 1;

        for (line_number, line) in code.lines().enumerate() {
            let terms = terms_in_line(line);
            if terms.is_empty() {
                continue;
            }

            let relative = file.strip_prefix(project_root).unwrap_or(file);
            all_violations.push(format!(
                "  {}:{}: {} [{}]",
                relative.display(),
                line_number + 1,
                line.trim(),
                terms.join(", ")
            ));
        }
    }

    assert!(files_scanned > 0, "No readable Rust files were found to check.");

    assert!(all_violations.is_empty(), "Legacy-language terms found:\n{}", all_violations.join("\n"));
}

```

`tests/cleancode/src/cleancode_no_literal_wrapped_fallback.rs`:

```rs
//! Integration test: detect provably unnecessary fallback patterns.
//!
//! Flags method calls like `Some(expr).unwrap_or(fallback)` or
//! `Ok(expr).unwrap_or_else(|_| fallback)` where the receiver is
//! syntactically `Some(...)` or `Ok(...)`, making the fallback dead code.
//!
//! Works via syntax analysis only — no type inference required.

use std::fs;
use std::path::{Path, PathBuf};

use syn::{
    Expr, ExprCall, ExprMethodCall,
    visit::{self, Visit},
};

const SOURCE_DIRS: &[&str] = &["src", "app", "lib"];
const IGNORE_DIRS: &[&str] = &["target", "vendor", "node_modules", ".git"];

struct FallbackVisitor {
    violations: Vec<String>,
}

impl<'ast> Visit<'ast> for FallbackVisitor {
    fn visit_expr_method_call(&mut self, node: &'ast ExprMethodCall) {
        // Check for: Some(expr).unwrap_or(fallback), Ok(expr).or_else(fallback), etc.
        let method_name = node.method.to_string();
        let receiver_is_literal_wrapper = match node.receiver.as_ref() {
            Expr::Call(ExprCall { func, .. }) => {
                if let Expr::Path(p) = func.as_ref() {
                    let ident = p.path.get_ident().map(|i| i.to_string());
                    matches!(ident.as_deref(), Some("Some" | "Ok"))
                } else {
                    false
                }
            }
            _ => false,
        };

        if receiver_is_literal_wrapper
            && matches!(
                method_name.as_str(),
                "unwrap_or" | "unwrap_or_else" | "or" | "or_else" | "map_or" | "map_or_else"
            )
        {
            let message = if matches!(method_name.as_str(), "unwrap_or_else" | "or_else" | "map_or_else") {
                format!("call to `.{method_name}()` on `Some(…)`/`Ok(…)` — fallback closure is unreachable")
            } else {
                format!(
                    "call to `.{method_name}()` on `Some(…)`/`Ok(…)` — fallback is unnecessary and eagerly evaluated"
                )
            };
            self.violations.push(message);
        }

        visit::visit_expr_method_call(self, node);
    }
}

fn collect_source_files(project_root: &Path) -> Vec<PathBuf> {
    let mut files = Vec::new();
    let mut stack: Vec<PathBuf> =
        SOURCE_DIRS.iter().map(|dir| project_root.join(dir)).filter(|path| path.is_dir()).collect();

    while let Some(dir) = stack.pop() {
        let Ok(entries) = fs::read_dir(&dir) else {
            continue;
        };
        for entry in entries.flatten() {
            let p = entry.path();
            if p.is_dir() {
                let name = entry.file_name().to_string_lossy().to_string();
                if !IGNORE_DIRS.contains(&name.as_str()) {
                    stack.push(p);
                }
            } else if p.extension().is_some_and(|e| e == "rs") {
                files.push(p);
            }
        }
    }

    files
}

/// Detects provably unnecessary fallback calls on `Some` or `Ok` wrappers.
#[test]
fn no_literal_wrapped_fallback() {
    let project_root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let files = collect_source_files(project_root);

    assert!(!files.is_empty(), "No source files found in src/, app/, or lib/.");

    let mut all_violations = Vec::new();
    let mut files_scanned = 0;

    for file in &files {
        let Ok(code) = fs::read_to_string(file) else {
            continue;
        };
        let Ok(syntax) = syn::parse_file(&code) else {
            continue;
        };
        files_scanned += 1;

        let mut visitor = FallbackVisitor { violations: Vec::new() };
        visitor.visit_file(&syntax);

        for msg in &visitor.violations {
            let relative = file.strip_prefix(project_root).unwrap_or(file);
            all_violations.push(format!("  {} — {msg}", relative.display()));
        }
    }

    assert!(files_scanned > 0, "No parsable Rust files were found to check.");

    assert!(all_violations.is_empty(), "Provably unnecessary fallback(s) found:\n{}", all_violations.join("\n"),);
}

```

`tests/cleancode/src/cleancode_no_manufactured_success.rs`:

```rs
//! Integration test: detect suspicious fallback patterns.
//!
//! Flags `match` arms on `Option` or `Result` where the failure variant
//! (`None` / `Err`) produces a success value (`Some(…)` / `Ok(…)`),
//! indicating silent error recovery (the AI anti-pattern).
//!
//! Syntax-only: works on the AST without type inference.

use std::fs;
use std::path::{Path, PathBuf};

use syn::{
    Expr, ExprCall, ExprMatch,
    visit::{self, Visit},
};

const IGNORE_DIRS: &[&str] = &["target", "vendor", "node_modules", ".git"];
const SOURCE_DIRS: &[&str] = &["src", "app", "lib"];

struct SuspiciousMatchVisitor {
    violations: Vec<String>,
}

impl<'ast> Visit<'ast> for SuspiciousMatchVisitor {
    fn visit_expr_match(&mut self, node: &'ast ExprMatch) {
        let has_success_arm = node.arms.iter().any(|arm| is_success_pattern(&arm.pat));
        let produces_success =
            node.arms.iter().any(|arm| is_failure_pattern(&arm.pat) && arm_constructs_success(arm.body.as_ref()));

        if has_success_arm && produces_success {
            self.violations.push("suspicious match arm constructs `Ok(…)`/`Some(…)` from error path".to_string());
        }

        visit::visit_expr_match(self, node);
    }
}

fn is_success_pattern(pat: &syn::Pat) -> bool {
    matches!(pat, syn::Pat::TupleStruct(pts) if pts.path.get_ident().is_some_and(|i| matches!(i.to_string().as_str(), "Ok" | "Some")))
}

fn is_failure_pattern(pat: &syn::Pat) -> bool {
    matches!(pat, syn::Pat::TupleStruct(pts) if pts.path.get_ident().is_some_and(|i| i == "Err"))
        || matches!(pat, syn::Pat::Path(pp) if pp.path.get_ident().is_some_and(|i| i == "None"))
}

fn arm_constructs_success(expr: &Expr) -> bool {
    match expr {
        Expr::Call(ExprCall { func, .. }) => {
            matches!(func.as_ref(), Expr::Path(p) if p.path.get_ident().is_some_and(|i| matches!(i.to_string().as_str(), "Ok" | "Some")))
        }
        _ => false,
    }
}

fn collect_source_files(project_root: &Path) -> Vec<PathBuf> {
    let mut files = Vec::new();
    let mut stack: Vec<PathBuf> =
        SOURCE_DIRS.iter().map(|dir| project_root.join(dir)).filter(|path| path.is_dir()).collect();

    while let Some(dir) = stack.pop() {
        let Ok(entries) = fs::read_dir(&dir) else {
            continue;
        };
        for entry in entries.flatten() {
            let p = entry.path();
            if p.is_dir() {
                let name = entry.file_name().to_string_lossy().to_string();
                if !IGNORE_DIRS.contains(&name.as_str()) {
                    stack.push(p);
                }
            } else if p.extension().is_some_and(|e| e == "rs") {
                files.push(p);
            }
        }
    }

    files
}

/// Detects match arms that construct success values from error paths.
#[test]
fn no_suspicious_fallback() {
    let project_root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let files = collect_source_files(project_root);

    assert!(!files.is_empty(), "No source files found in src/, app/, or lib/.");

    let mut all_violations = Vec::new();
    let mut files_scanned = 0;

    for file in &files {
        let Ok(code) = fs::read_to_string(file) else {
            continue;
        };
        let Ok(syntax) = syn::parse_file(&code) else {
            continue;
        };
        files_scanned += 1;

        let mut visitor = SuspiciousMatchVisitor { violations: Vec::new() };
        visitor.visit_file(&syntax);

        for msg in &visitor.violations {
            let relative = file.strip_prefix(project_root).unwrap_or(file);
            all_violations.push(format!("  {} — {msg}", relative.display()));
        }
    }

    assert!(files_scanned > 0, "No parsable Rust files were found to check.");

    assert!(all_violations.is_empty(), "Suspicious fallback(s) found:\n{}", all_violations.join("\n"),);
}

```

`tests/cleancode/src/lib.rs`:

```rs
#![forbid(unsafe_code)]

#[cfg(test)]
mod cleancode_file_too_long;
#[cfg(test)]
mod cleancode_no_legacy_terms;
#[cfg(test)]
mod cleancode_no_literal_wrapped_fallback;
#[cfg(test)]
mod cleancode_no_manufactured_success;

```