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


# ---- Laravel build script ----


def test_laravel_build_script_has_err_trap():
    c = _read("runtimes/laravel/deployment/02_run_build.sh")
    helpers.assert_contains(c, "trap '")
    helpers.assert_contains(c, "ERR")
    helpers.assert_contains(c, "$LINENO")
    helpers.assert_contains(c, "$BASH_COMMAND")


def test_laravel_build_script_labels_each_phase():
    c = _read("runtimes/laravel/deployment/02_run_build.sh")
    for label in [
        "Installing Composer dependencies",
        "Entering Laravel maintenance mode",
        "Installing frontend dependencies",
        "Building frontend assets",
        "Running migrations",
        "Rebuilding Laravel caches",
    ]:
        helpers.assert_contains(c, label)


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
