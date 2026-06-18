The problem is pretty clear: **your “pool” file is actually being used as the entire PHP-FPM master config**, and it leaves PHP-FPM’s global logging path unspecified.

Your template only has:

```ini
[global]
daemonize = no
```

then the pool config. It does **not** set `error_log`, `pid`, worker output behavior, access logs, slow logs, or PHP error-log paths.  The systemd service then starts PHP-FPM with this file as the whole config via `--fpm-config {{ laravel_php_fpm_pool_config_path }}`.  PHP’s own docs say the global `error_log` default is `#INSTALL_PREFIX#/log/php-fpm.log`, and if set to `syslog` it logs through syslog instead. ([PHP][1])

So PHP-FPM falls back to `/var/log/php-fpm.log`, but your service runs as the runtime user, not root, and has `ProtectSystem=strict`.   With `ProtectSystem=strict`, systemd makes the whole filesystem read-only except API filesystems, unless specific paths are allow-listed with `ReadWritePaths=`. ([man7.org][2]) That is why `/var/log/php-fpm.log` fails.

The second bug is that your validation does not catch this. `php_fpm.py` validates the config with `_sudo=True`, so the test runs as root, but the actual service runs as `runtime_user`.   That means runtime apply can say “config is valid” and then immediately install a service that cannot start.

## Stable design

I would not use `/var/log/php-fpm.log` at all for this architecture. You are not running the distro PHP-FPM service. You are running a **per-site, sandboxed, unprivileged PHP-FPM instance**, so all PHP-FPM-owned runtime files must be explicit and inside paths that the service can write.

The smallest stable model is:

```ini
[global]
daemonize = no
pid = {{ paths.runtime_socket_dir }}/php-fpm.pid
error_log = {{ paths.runtime_socket_dir }}/php-fpm-error.log
log_level = notice

[{{ laravel_php_fpm_pool_name }}]
user = {{ runtime_user }}
group = {{ runtime_group }}

listen = {{ laravel_php_fpm_socket_path }}
listen.owner = {{ runtime_user }}
listen.group = {{ runtime_group }}
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
php_admin_value[error_log] = {{ paths.runtime_socket_dir }}/php-worker-error.log

access.log = {{ paths.runtime_socket_dir }}/php-fpm-access.log
slowlog = {{ paths.runtime_socket_dir }}/php-fpm-slow.log
```

That matches your existing systemd/AppArmor shape because `/run/<project>` is already the runtime socket directory, the service already allows writing there via `ReadWritePaths={{ paths.runtime_socket_dir }}`, and the AppArmor profile already allows `{{ paths.runtime_socket_dir }}/** rwk`.    PHP-FPM supports `catch_workers_output`, which redirects worker stdout/stderr into the main error log, and supports per-pool `access.log` and `slowlog`. ([PHP][1])

## Better long-term version

For persistent logs, create a per-site log directory during runtime provisioning:

```text
/var/log/bonesdeploy/<project>/
```

owned by `runtime_user:runtime_group`, mode `0750`, then add:

```ini
error_log = /var/log/bonesdeploy/{{ project_name }}/php-fpm-error.log
php_admin_value[error_log] = /var/log/bonesdeploy/{{ project_name }}/php-worker-error.log
access.log = /var/log/bonesdeploy/{{ project_name }}/php-fpm-access.log
slowlog = /var/log/bonesdeploy/{{ project_name }}/php-fpm-slow.log
```

and update the service/AppArmor:

```ini
ReadWritePaths={{ paths.runtime_socket_dir }} /var/log/bonesdeploy/{{ project_name }} {{ paths.current }}/storage
```

Systemd also has `LogsDirectory=`, which can create directories under `/var/log` and expose `$LOGS_DIRECTORY`, but it may recursively adjust ownership if an existing directory has the wrong owner. ([man7.org][2]) Given your “permissions are a provisioning-time contract” principle, I’d probably have pyinfra create the exact log directory explicitly instead of relying on systemd to mutate it.

## Refactor plan

First, rename the template mentally: `php-fpm-pool.conf.j2` is not just a pool file. It is a **complete per-site FPM config** because the service passes it as `--fpm-config`. Either rename it to `php-fpm.conf.j2`, or split it into a real master config plus pool include. Do not leave it as an ambiguous “pool config.”

Second, make the config self-contained. Add explicit `error_log`, `pid`, worker output capture, PHP worker error log, optional access log, and optional slowlog. Never let this per-site service fall back to `/var/log/php-fpm.log`.

Third, change validation to test the same identity that runs production. Keep root validation if useful, but add a runtime-user validation step:

```bash
sudo -u {{ runtime_user }} /usr/sbin/php-fpm{{ php_version }} --test --fpm-config /srv/conf/{{ project }}/php-fpm.conf
```

That would have caught this exact failure before systemd tried to start the service.

Fourth, add a regression test around the rendered template. The test should assert that the PHP-FPM config contains:

```text
error_log =
pid =
catch_workers_output = yes
php_admin_flag[log_errors] = on
php_admin_value[error_log] =
```

and that none of those point at `/var/log/php-fpm.log`.

Fifth, decide whether logs are ephemeral or persistent. For fastest stabilization, put FPM logs under `/run/<project>`. For production quality, add `/var/log/bonesdeploy/<project>` as a runtime-provisioned path and allow it in systemd/AppArmor.

The immediate bug is not PHP 8.5. The bug is that BonesInfra generated a sandboxed non-root FPM service but left PHP-FPM using root-era global defaults.

[1]: https://www.php.net/manual/en/install.fpm.configuration.php "PHP: Configuration - Manual"
[2]: https://man7.org/linux/man-pages/man5/systemd.exec.5.html "systemd.exec(5) - Linux manual page"
