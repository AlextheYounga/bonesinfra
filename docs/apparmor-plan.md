You are helping refactor BonesInfra runtime isolation.

Repository:
- https://github.com/AlextheYounga/bonesinfra

Goal:
Implement AppArmor support for all BonesInfra-managed services that can cleanly use it, without Docker, and without forcing PHP-FPM into the broken custom per-site systemd model.

This pass should produce a sane service isolation model that can be tested together on one server, rather than debugging one fragile runtime at a time.

Core decision:
Do NOT create per-project AppArmor for PHP-FPM pools in this pass.

Runtime backend model:

1. php_fpm_pool backend
   Used by Laravel/PHP.
   Security model:
   - distro php<version>-fpm.service
   - one FPM pool per app
   - one Unix user/group per app
   - one private socket per app
   - one per-project log directory
   - no custom <project>-php-fpm.service
   - no per-project PHP-FPM AppArmor profile in this pass

2. systemd_app backend
   Used by:
   - Django / Gunicorn
   - Rails / Puma
   - Next / Node standalone server
   - Nuxt / Nitro Node server
   - SvelteKit / adapter-node
   This backend should support:
   - one app-specific systemd service
   - one app-specific AppArmor profile
   - one app-specific runtime directory
   - one app-specific log directory
   - nginx reverse proxy to socket or localhost port

3. static_site backend
   Used by Vue/Vite.
   Security model:
   - no app service
   - no app AppArmor profile
   - nginx serves static files
   - per-site nginx AppArmor profile still applies

Current context:
The legacy Laravel model attempted to run a custom per-project PHP-FPM master process with:
- <project>-php-fpm.service
- custom --fpm-config
- RuntimeDirectory=<project>
- custom PHP-FPM AppArmor profile
- custom socket/log paths

That model caused:
- PHP-FPM log permission errors
- root-owned validation artifacts
- disappearing /run/<project> directories
- RuntimeDirectory conflicts between services
- too many ownership/lifecycle fights

Do not preserve that legacy PHP-FPM model.

Implementation target:
Create a clean shared AppArmor/systemd foundation for systemd_app services while Laravel uses PHP-FPM pool isolation.

Do not implement Docker.
Do not redesign the Rust/Python contract.
Do not try to make PHP-FPM AppArmor perfect in this pass.
Do not mix the old custom PHP-FPM service with the new PHP-FPM pool model.

Files to inspect first:
- src/bonesinfra/deploys/runtime/plan.py
- src/bonesinfra/deploys/runtime/apparmor.py
- src/bonesinfra/deploys/runtime/nginx.py
- src/bonesinfra/assets/nginx/site-nginx.service.j2
- src/bonesinfra/assets/apparmor/project-nginx-profile.j2
- src/bonesinfra/runtimes/__init__.py
- src/bonesinfra/runtimes/laravel/*
- src/bonesinfra/runtimes/django/*
- src/bonesinfra/runtimes/rails/*
- src/bonesinfra/runtimes/next/*
- src/bonesinfra/runtimes/nuxt/*
- src/bonesinfra/runtimes/sveltekit/*
- src/bonesinfra/runtimes/vue/*
- src/bonesinfra/domain/paths.py

Desired new common modules:

    src/bonesinfra/runtimes/common/
    ├── __init__.py
    ├── apparmor.py
    ├── systemd_app.py
    ├── php_fpm_pool.py
    ├── static_site.py
    ├── logs.py
    ├── runtime_dirs.py
    └── validation.py

Keep this small and practical. Do not build a giant framework.

------------------------------------------------------------
SYSTEMD_APP BACKEND
------------------------------------------------------------

Create a common systemd app service renderer.

It should support a descriptor like:

    SystemdApp(
        runtime_name="django",
        service_name="<project>-gunicorn",
        apparmor_profile_name="bonesdeploy-<project>-gunicorn",
        description="Gunicorn for <project>",
        exec_start="...",
        working_directory="<paths.current>",
        environment={...},
        environment_file="<paths.conf_root>/runtime.env",
        runtime_directory="<project>/gunicorn",
        logs_directory="bonesdeploy/<project>",
        read_only_paths=[...],
        read_write_paths=[...],
        network_policy="standard_app",
        validation_commands=[...],
        health_check=...
    )

The common service template should include:

    [Unit]
    Description={{ description }}
    After=network.target apparmor.service
    Requires=apparmor.service

    [Service]
    Type=simple
    User={{ runtime_user }}
    Group={{ runtime_group }}
    SupplementaryGroups={{ release_group }}
    WorkingDirectory={{ working_directory }}
    EnvironmentFile=-{{ environment_file }}
    ExecStart={{ exec_start }}

    AppArmorProfile={{ apparmor_profile_name }}

    RuntimeDirectory={{ runtime_directory }}
    RuntimeDirectoryMode=0750

    LogsDirectory={{ logs_directory }}
    LogsDirectoryMode=0750

    StandardOutput=journal
    StandardError=journal

    Restart=always
    RestartSec=2

    NoNewPrivileges=yes
    PrivateTmp=yes
    ProtectHome=yes
    ProtectSystem=full

    ReadOnlyPaths={{ read_only_paths }}
    ReadWritePaths={{ read_write_paths }}

    [Install]
    WantedBy=multi-user.target

Important:
- Start with ProtectSystem=full, not strict.
- Do not start with aggressive syscall filtering.
- Do not start with PrivateDevices unless the runtime works with it.
- Do not restrict network too hard yet; many apps need outbound DB/API connections.
- Harden later after smoke tests pass.

Each systemd_app service must have its own RuntimeDirectory leaf.

Good:

    RuntimeDirectory=<project>/gunicorn
    RuntimeDirectory=<project>/puma
    RuntimeDirectory=<project>/nuxt
    RuntimeDirectory=<project>/sveltekit
    RuntimeDirectory=<project>/next

Bad:

    RuntimeDirectory=<project>

No two services may share the same RuntimeDirectory value.

------------------------------------------------------------
APPARMOR COMMON BACKEND
------------------------------------------------------------

Create a common AppArmor renderer/loader.

Suggested API:

    render_profile(ctx, profile)
    load_profile(profile_path)
    set_profile_mode(profile_path, mode)
    verify_profile_loaded(profile_name)
    verify_service_attached(service_name, profile_name)
    collect_recent_denials(service_name=None)

The common AppArmor profile should be generated from a descriptor:

    AppArmorProfile(
        name="bonesdeploy-<project>-gunicorn",
        runtime_name="gunicorn",
        executable="/usr/bin/python3",
        app_root=paths.current,
        runtime_dir="/run/<project>/gunicorn",
        log_dir="/var/log/bonesdeploy/<project>",
        conf_root=paths.conf_root,
        read_paths=[...],
        write_paths=[...],
        exec_paths=[...],
        network_rules=[...],
        extra_rules=[...],
    )

Template shape:

    #include <tunables/global>

    profile {{ apparmor_profile_name }} flags=(attach_disconnected,mediate_deleted) {
      #include <abstractions/base>
      #include <abstractions/nameservice>

      signal,
      unix,
      network unix stream,
      network inet stream,
      network inet6 stream,

      {{ executable }} rix,

      /usr/bin/** rix,
      /bin/** rix,
      /usr/lib/** r,
      /lib/** r,
      /lib64/** r,

      {{ paths.conf_root }}/ r,
      {{ paths.conf_root }}/** r,

      {{ paths.current }}/ r,
      {{ paths.current }}/** r,

      {{ runtime_dir }}/ rw,
      {{ runtime_dir }}/** rwk,

      {{ log_dir }}/ rw,
      {{ log_dir }}/** rwk,

      # Runtime-specific writable paths go here.
      {{ runtime_write_rules }}

      # Runtime-specific executable/read paths go here.
      {{ runtime_extra_rules }}

      deny /root/** rwklmx,
      deny /etc/ssh/** rwklmx,
    }

Do not make the first version too tight.
The purpose of this pass is working AppArmor, not perfect AppArmor.

Use broad but bounded rules:
- allow the app release tree read-only by default
- allow only declared writable paths
- allow runtime dir
- allow log dir
- allow language/runtime libraries
- deny obvious sensitive system paths
- avoid per-file micromanagement until profiles are stable

Support profile modes:

    apparmor_mode = "complain" | "enforce"

Default for development/smoke testing:

    complain

Default for production later:

    enforce

For now, make mode configurable in runtime config or internal deployment setting.

Loading flow:
1. Ensure apparmor service enabled/running.
2. Render profile to /etc/apparmor.d/<profile_name>.
3. Load/reload with apparmor_parser -r.
4. Set complain/enforce mode as configured.
5. Verify profile appears in /sys/kernel/security/apparmor/profiles.
6. Start/restart service.
7. Verify service process is attached to the expected profile.

Service attachment check:
- Get MainPID:

      systemctl show -p MainPID --value <service>

- Read:

      /proc/<pid>/attr/current

- It should include the AppArmor profile name.

Do this as an explicit validation step for systemd_app services.

------------------------------------------------------------
NGINX APPARMOR
------------------------------------------------------------

Per-site nginx already has an AppArmor model.

Keep it.

But clean it up to use the same common AppArmor helper if practical.

Do not break existing per-site nginx AppArmor.

Nginx service should:
- keep AppArmorProfile=bonesdeploy-<project>-nginx
- have its own RuntimeDirectory=<project>/nginx
- not share RuntimeDirectory=<project> with other services
- write logs to /var/log/bonesdeploy/<project> or journal
- proxy to the app socket or localhost port

Per-site nginx profile should allow:
- read nginx config
- read current web root
- write nginx runtime dir
- write log dir
- connect to app socket if using Unix sockets
- deny /root and /etc/ssh

------------------------------------------------------------
PHP-FPM / LARAVEL POLICY
------------------------------------------------------------

Do not implement per-project AppArmor for PHP-FPM in this pass.

Laravel should use php_fpm_pool backend.

Expected Laravel shape:

    php<version>-fpm.service
      -> /etc/php/<version>/fpm/pool.d/<project>.conf
      -> /run/php/php<version>-fpm-<project>.sock

Laravel should not use:
- <project>-php-fpm.service
- AppArmorProfile= for PHP-FPM
- RuntimeDirectory for PHP-FPM
- custom full --fpm-config
- site-php-fpm-profile.j2

Laravel pool security:
- user=<runtime_user>
- group=<runtime_group>
- listen=/run/php/php<version>-fpm-<project>.sock
- listen.owner=www-data
- listen.group=www-data
- listen.mode=0660
- logs under /var/log/bonesdeploy/<project>
- security.limit_extensions=.php
- clear_env=yes
- optional open_basedir later, not required in this pass

PHP-FPM AppArmor can be revisited later as optional global PHP-FPM hardening, not per-project pool hardening.

------------------------------------------------------------
RUNTIME ADAPTER TARGETS
------------------------------------------------------------

Implement or prepare these adapters to use the new backend.

1. Django / Gunicorn
Backend:

    systemd_app

Service:
    <project>-gunicorn.service

Runtime directory:
    <project>/gunicorn

Socket:
    /run/<project>/gunicorn/gunicorn.sock

ExecStart example:
    {{ paths.current }}/.venv/bin/gunicorn {{ django_wsgi_module }} --bind unix:/run/<project>/gunicorn/gunicorn.sock

Writable paths:
- runtime dir
- log dir
- optional media dir
- optional static collection dir if configured

AppArmor:
    bonesdeploy-<project>-gunicorn

2. Rails / Puma
Backend:

    systemd_app

Service:
    <project>-puma.service

Runtime directory:
    <project>/puma

Socket:
    /run/<project>/puma/puma.sock

ExecStart example:
    bundle exec puma -e production -b unix:///run/<project>/puma/puma.sock

Writable paths:
- runtime dir
- log dir
- tmp
- storage
- maybe public/assets if needed during runtime, but prefer build-time assets

AppArmor:
    bonesdeploy-<project>-puma

3. Nuxt / Nitro
Backend:

    systemd_app

Service:
    <project>-nuxt.service

Runtime directory:
    <project>/nuxt

Socket:
    /run/<project>/nuxt/nuxt.sock

ExecStart example:
    node .output/server/index.mjs

Environment:
    NODE_ENV=production
    NITRO_UNIX_SOCKET=/run/<project>/nuxt/nuxt.sock

Writable paths:
- runtime dir
- log dir
- optional cache dirs if configured

AppArmor:
    bonesdeploy-<project>-nuxt

4. SvelteKit / adapter-node
Backend:

    systemd_app

Service:
    <project>-sveltekit.service

Runtime directory:
    <project>/sveltekit

Socket:
    /run/<project>/sveltekit/sveltekit.sock

ExecStart example:
    node build

Environment:
    NODE_ENV=production
    SOCKET_PATH=/run/<project>/sveltekit/sveltekit.sock
    ORIGIN=https://<domain>

Writable paths:
- runtime dir
- log dir
- optional app cache dirs if configured

AppArmor:
    bonesdeploy-<project>-sveltekit

5. Next
Backend:

    systemd_app

Service:
    <project>-next.service

Runtime directory:
    <project>/next

Prefer localhost TCP first.

ExecStart example:
    node .next/standalone/server.js

Environment:
    NODE_ENV=production
    HOSTNAME=127.0.0.1
    PORT=<allocated_port>

Nginx:
    proxy_pass http://127.0.0.1:<allocated_port>;

Writable paths:
- runtime dir
- log dir
- optional .next/cache if needed

AppArmor:
    bonesdeploy-<project>-next

Do not force Unix sockets for Next in this pass.

6. Vue / Vite
Backend:

    static_site

No app service.
No app AppArmor profile.
Nginx serves:

    {{ paths.current }}/dist

Per-site nginx AppArmor still applies.

7. Laravel
Backend:

    php_fpm_pool

No app AppArmor profile in this pass.
Per-site nginx AppArmor still applies.

------------------------------------------------------------
ORDER OF OPERATIONS
------------------------------------------------------------

Runtime apply should follow this order for systemd_app runtimes:

1. Install packages/runtime prerequisites.
2. Ensure runtime user/group assumptions are satisfied.
3. Ensure /srv/conf/<project>.
4. Ensure /var/log/bonesdeploy/<project>.
5. Render env file if needed.
6. Render app-specific AppArmor profile.
7. Load AppArmor profile.
8. Set profile mode: complain or enforce.
9. Verify profile loaded.
10. Render app-specific systemd service with AppArmorProfile=.
11. systemd daemon-reload.
12. Start/restart app service.
13. Verify service active.
14. Verify service process attached to expected AppArmor profile.
15. Render/update per-site nginx config.
16. Validate nginx.
17. Restart/reload per-site nginx.
18. Verify nginx service active.
19. Verify nginx AppArmor profile attached.
20. Run health check.
21. Collect recent AppArmor denials and print them clearly.

Runtime apply for Laravel should follow:

1. Install PHP packages.
2. Ensure /var/log/bonesdeploy/<project>.
3. Render PHP-FPM pool config.
4. Validate php-fpm.
5. Reload/start php<version>-fpm.service.
6. Render/update per-site nginx config.
7. Validate nginx.
8. Restart/reload per-site nginx.
9. Verify nginx AppArmor profile attached.
10. Run health check.
11. Collect recent AppArmor denials.

------------------------------------------------------------
ONE-SERVER SMOKE TESTING
------------------------------------------------------------

Add a script or command that can validate all supported AppArmor-capable services on one reusable test server.

Suggested script:

    scripts/smoke_apparmor_runtimes.sh

It should:
- accept host/config inputs
- run runtime apply for selected runtime fixtures
- not provision a new server per runtime
- collect systemd status
- collect journal logs
- collect AppArmor denials
- verify profile attachment for every systemd service
- emit a single summary table

Suggested output table:

    runtime     service              apparmor profile                  mode       active   attached   denials
    nginx       lawsnipe-nginx        bonesdeploy-lawsnipe-nginx        enforce    yes      yes        0
    django      lawsnipe-gunicorn     bonesdeploy-lawsnipe-gunicorn     complain   yes      yes        0
    rails       lawsnipe-puma         bonesdeploy-lawsnipe-puma         complain   yes      yes        0
    nuxt        lawsnipe-nuxt         bonesdeploy-lawsnipe-nuxt         complain   yes      yes        0
    sveltekit   lawsnipe-sveltekit    bonesdeploy-lawsnipe-sveltekit    complain   yes      yes        0
    next        lawsnipe-next         bonesdeploy-lawsnipe-next         complain   yes      yes        0
    laravel     php8.5-fpm pool       no per-project profile            n/a        yes      n/a        n/a

Do not require spinning up multiple servers.

For first implementation, smoke test can use one or two representative app services if full fixtures are too large:
- one Python/Gunicorn fixture
- one Node fixture
- existing nginx profile
- Laravel PHP-FPM pool path

But design the script so more runtime fixtures can be added.

------------------------------------------------------------
VALIDATION COMMANDS
------------------------------------------------------------

Add common validation helpers.

Useful checks:

    systemctl is-active <service>
    systemctl show -p MainPID --value <service>
    cat /proc/<pid>/attr/current
    grep '<profile_name>' /sys/kernel/security/apparmor/profiles
    journalctl -u <service> -n 100 --no-pager
    journalctl -k --since '5 minutes ago' | grep -i 'apparmor.*DENIED'

For app services, fail if:
- service is not active
- profile is not loaded
- service process is not attached to the expected profile
- nginx validation fails
- app health check fails

In complain mode:
- do not fail on denials by default
- print denials loudly

In enforce mode:
- fail on denials or service failure

------------------------------------------------------------
REGRESSION TESTS
------------------------------------------------------------

Add tests where practical.

Template/render tests:
- systemd_app service contains AppArmorProfile.
- systemd_app service uses unique RuntimeDirectory=<project>/<runtime>.
- systemd_app service does not use shared RuntimeDirectory=<project>.
- systemd_app service contains LogsDirectory or explicit log path handling.
- AppArmor profile includes app root read rules.
- AppArmor profile includes runtime dir write rules.
- AppArmor profile includes log dir write rules.
- AppArmor profile denies /root and /etc/ssh.
- nginx service keeps AppArmorProfile.
- Laravel does not render PHP-FPM AppArmor profile.
- Laravel does not render <project>-php-fpm.service.
- Laravel uses PHP-FPM pool backend.

Search guards:
- fail if Laravel runtime calls apparmor.setup_php_fpm.
- fail if Laravel runtime renders site-php-fpm.service.j2.
- fail if a systemd app service uses RuntimeDirectory={{ project_name }}.
- fail if any two service templates share the same RuntimeDirectory leaf.

------------------------------------------------------------
FILES TO REMOVE OR DEPRECATE
------------------------------------------------------------

For Laravel PHP-FPM old model:
- stop using src/bonesinfra/runtimes/laravel/assets/php/site-php-fpm.service.j2
- stop using src/bonesinfra/runtimes/laravel/assets/php/site-php-fpm-profile.j2
- stop calling apparmor.setup_php_fpm
- stop calling systemd.service for <project>-php-fpm.service
- stop using custom full php-fpm --fpm-config

Do not necessarily delete files in the first commit if that causes churn, but ensure they are no longer used.
Prefer deleting once tests confirm new path works.

------------------------------------------------------------
COMMIT PLAN
------------------------------------------------------------

Commit 1:
Introduce common AppArmor/systemd_app helpers.
Keep behavior minimal.
Add render tests.

Commit 2:
Move nginx AppArmor/profile loading to common helper if practical.
Fix RuntimeDirectory so nginx uses <project>/nginx, not shared <project>.

Commit 3:
Implement systemd_app descriptor support for one representative runtime first, preferably a Node runtime or Django.
Add profile attachment validation.

Commit 4:
Migrate remaining systemd_app runtimes to descriptors/stubs:
- django
- rails
- next
- nuxt
- sveltekit

They do not all need perfect app build support yet, but their service/profile model should be coherent.

Commit 5:
Ensure Laravel remains php_fpm_pool only and does not use PHP-FPM AppArmor.
Add guards.

Commit 6:
Add one-server smoke script and documentation.

------------------------------------------------------------
FINAL EXPECTED STATE
------------------------------------------------------------

After this pass:

- Per-site nginx uses AppArmor.
- Django/Gunicorn systemd app service can use AppArmor.
- Rails/Puma systemd app service can use AppArmor.
- Nuxt/Nitro systemd app service can use AppArmor.
- SvelteKit systemd app service can use AppArmor.
- Next systemd app service can use AppArmor.
- Vue has no app service; nginx AppArmor protects the serving layer.
- Laravel uses PHP-FPM pool isolation and skips per-project PHP-FPM AppArmor.
- No service shares RuntimeDirectory=<project>.
- Runtime apply validates that systemd services are actually attached to their AppArmor profiles.
- A single smoke script can test all supported service/profile combinations on one server.

Work style:
- Do not over-harden first.
- Make AppArmor broad enough to work, then tighten later.
- Avoid server-by-server manual debugging.
- Prefer generated tests and one-server smoke validation.
- Do not reintroduce the custom PHP-FPM systemd service model.
- End with a summary of changed files, tests run, smoke results, known denials, and remaining hardening TODOs.