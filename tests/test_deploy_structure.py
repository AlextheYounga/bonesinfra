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


def test_setup_adds_deploy_user_to_runtime_group():
    c = helpers.read(SETUP_USERS)
    helpers.assert_contains(c, "_ensure_group_membership(ctx.config.deploy_user, ctx.runtime.runtime_group)")


def test_setup_shared_dir_is_setgid_and_traversable():
    c = helpers.read(SETUP_DIRECTORIES)
    shared_block = c.split('path=paths["shared"]')[1].split(")")[0]
    helpers.assert_contains(shared_block, 'mode="2775"')


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


def test_setup_installs_openssl_for_nginx_default_deny_cert():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/deploys/setup/packages.py")
    helpers.assert_contains(c, '"openssl"')


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
    helpers.assert_contains(c, "validate_config")


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


def test_ssl_uses_acme_webroot():
    c = helpers.read(SSL_PLAN)
    helpers.assert_contains(c, "acme_webroot")


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
        "cleanup_orphaned_pools(ctx, php_version)",
        "php_fpm_pool.render_pool",
        "php_fpm_pool.validate_php_fpm",
        "php_fpm_pool.reload_php_fpm",
    )


def test_laravel_deploy_does_not_setup_php_fpm_apparmor():
    c = helpers.read(LARAVEL_DEPLOY)
    helpers.assert_not_contains(c, "apparmor")
    helpers.assert_ordering(
        c,
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
        "validate_config",
        "Ensure nginx service is enabled and started",
        "Ensure per-site nginx service is enabled and started",
        "systemctl reload nginx",
    )


def test_runtime_nginx_installs_default_deny_before_validation():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/deploys/runtime/nginx.py")
    helpers.assert_ordering(c, "install_default_deny_server", "validate_config")


def test_ssl_installs_default_deny_before_validation():
    c = helpers.read(SSL_PLAN)
    helpers.assert_ordering(c, "install_default_deny_server", "router.conf.j2", "validate_config")


def test_ssl_installs_default_deny_once():
    c = helpers.read(SSL_PLAN)
    assert c.count("install_default_deny_server") == 1
