"""Operation ordering and separation of concerns in deploy plans."""

from . import helpers

SETUP_PLAN = helpers.SRC_DIR / "bonesinfra/deploys/setup/plan.py"
SETUP_PACKAGES = helpers.SRC_DIR / "bonesinfra/deploys/setup/packages.py"
SETUP_USERS = helpers.SRC_DIR / "bonesinfra/deploys/setup/users.py"
SETUP_DIRECTORIES = helpers.SRC_DIR / "bonesinfra/deploys/setup/directories.py"
SETUP_PLACEHOLDER = helpers.SRC_DIR / "bonesinfra/deploys/setup/placeholder.py"
SETUP_FIREWALL = helpers.SRC_DIR / "bonesinfra/deploys/setup/firewall.py"
SETUP_FAIL2BAN = helpers.SRC_DIR / "bonesinfra/deploys/setup/fail2ban.py"
SETUP_UNATTENDED_UPGRADES = helpers.SRC_DIR / "bonesinfra/deploys/setup/unattended_upgrades.py"
SETUP_BONESREMOTE = helpers.SRC_DIR / "bonesinfra/deploys/setup/bonesremote.py"
SETUP_SUDOERS = helpers.SRC_DIR / "bonesinfra/deploys/setup/sudoers.py"
HELPERS_NEOVIM = helpers.SRC_DIR / "bonesinfra/deploys/helpers/neovim.py"
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
    helpers.assert_contains(c, "fail2ban.configure")
    helpers.assert_contains(c, "unattended_upgrades.configure")
    helpers.assert_contains(c, "users.install_authorized_key")
    helpers.assert_contains(c, "bonesremote.install")
    helpers.assert_contains(c, "sudoers.install")


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


def test_setup_installs_sudoers_in_bonesinfra():
    c = helpers.read(SETUP_PLAN)
    helpers.assert_contains(c, "sudoers.install")
    c = helpers.read(SETUP_BONESREMOTE)
    helpers.assert_not_contains(c, "bonesremote init")
    c = helpers.read(SETUP_SUDOERS)
    helpers.assert_contains(c, "visudo")
    helpers.assert_contains(c, 'mode="0440"')
    helpers.assert_contains(c, "bonesremote_global_link")


def test_setup_uses_resolved_placeholder_paths():
    c1 = helpers.read(SETUP_DIRECTORIES)
    helpers.assert_contains(c1, "placeholder_web_root")
    c2 = helpers.read(SETUP_PLACEHOLDER)
    helpers.assert_contains(c2, "placeholder_index")


def test_setup_seeds_bare_repo_post_receive_hook():
    c = helpers.read(SETUP_DIRECTORIES)
    helpers.assert_contains(c, '"Install bare repo post-receive hook"')
    helpers.assert_contains(c, "dest=f\"{paths['repo']}/hooks/post-receive\"")
    helpers.assert_contains(c, "user=ctx.config.deploy_user")
    helpers.assert_contains(c, 'mode="0755"')


def test_bare_repo_init_sets_default_branch():
    c = helpers.read(SETUP_DIRECTORIES)
    helpers.assert_contains(c, '"Set bare repo default branch"')
    helpers.assert_contains(c, "git --git-dir")
    helpers.assert_contains(c, "symbolic-ref HEAD refs/heads/{ctx.config.branch}")


def test_post_receive_hook_execs_bonesremote():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/assets/hooks/post-receive")
    helpers.assert_contains(c, "set -euo pipefail")
    helpers.assert_contains(c, "SITE=${SITE%.git}")
    helpers.assert_contains(c, 'exec sudo bonesremote hook post-receive --site "$SITE"')


def test_setup_avoids_usermod_for_existing_runtime_user():
    c = helpers.read(SETUP_USERS)
    helpers.assert_contains(c, "host.get_fact(Users)")
    helpers.assert_contains(c, "gpasswd -a")


def test_git_not_in_runtime_group():
    c = helpers.read(SETUP_USERS)
    helpers.assert_not_contains(c, "_ensure_group_membership(ctx.config.deploy_user, ctx.runtime.runtime_group)")
    helpers.assert_not_contains(c, "ctx.runtime.release_group")


def test_shared_is_runtime_owned_private_state():
    c = helpers.read(SETUP_DIRECTORIES)
    shared_block = c.split('path=paths["shared"]')[1].split(")")[0]
    helpers.assert_contains(shared_block, "user=ctx.runtime.runtime_user")
    helpers.assert_contains(shared_block, "group=ctx.runtime.runtime_group")
    helpers.assert_contains(shared_block, 'mode="0750"')


def test_releases_are_root_owned_group_readable():
    c = helpers.read(SETUP_DIRECTORIES)
    releases_block = c.split('path=paths["releases"]')[1].split(")")[0]
    helpers.assert_contains(releases_block, 'user="root"')
    helpers.assert_contains(releases_block, "group=ctx.runtime.runtime_group")
    helpers.assert_contains(releases_block, 'mode="2750"')


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


def test_setup_fail2ban_configures_sshd_jail_and_service():
    c = helpers.read(SETUP_FAIL2BAN)
    helpers.assert_contains(c, '"/etc/fail2ban/jail.local"')
    helpers.assert_contains(c, '"fail2ban"')
    helpers.assert_contains(c, "ssh_port=int(ctx.config.port)")


def test_setup_unattended_upgrades_installs_apt_configs():
    c = helpers.read(SETUP_UNATTENDED_UPGRADES)
    helpers.assert_contains(c, '"/etc/apt/apt.conf.d/20auto-upgrades"')
    helpers.assert_contains(c, '"/etc/apt/apt.conf.d/50unattended-upgrades"')


def test_helpers_neovim_installs_config_from_repo():
    c = helpers.read(HELPERS_NEOVIM)
    helpers.assert_contains(c, '"https://github.com/AlextheYounga/myneovim.git"')
    helpers.assert_contains(c, "git clone --depth=1")
    helpers.assert_contains(c, "reset --hard FETCH_HEAD")


# ---- runtime plan ----


def test_runtime_plan_calls_all_steps():
    c = helpers.read(RUNTIME_PLAN)
    helpers.assert_contains(c, "packages.install_apt")
    helpers.assert_contains(c, "apparmor.setup")
    helpers.assert_contains(c, "nginx.setup")
    helpers.assert_contains(c, "template_runtime.load")
    helpers.assert_contains(c, "nginx.start_services")
    helpers.assert_not_contains(c, "doctor.run")


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


def test_setup_installs_podman_networking():
    c = helpers.read(SETUP_PACKAGES)
    helpers.assert_contains(c, '"podman"')
    helpers.assert_contains(c, '"netavark"')
    helpers.assert_contains(c, '"aardvark-dns"')
    helpers.assert_contains(c, '"passt"')
    helpers.assert_contains(c, '"slirp4netns"')


# ---- ssl plan ----


def test_ssl_uses_certbot():
    c = helpers.read(SSL_PLAN)
    helpers.assert_contains(c, "certbot certonly")
    helpers.assert_contains(c, "ssl_enabled")


def test_setup_installs_openssl_for_nginx_default_deny_cert():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/deploys/setup/packages.py")
    helpers.assert_contains(c, '"openssl"')


def test_runtime_nginx_falls_back_when_domain_empty():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/deploys/runtime/nginx.py")
    helpers.assert_contains(c, "ctx.config.domain or ctx.config.preview_domain")
    helpers.assert_contains(
        c,
        'raise ValueError("domain or preview_domain is required for nginx config")',
    )


def test_ssl_requires_real_domain_for_router_render():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/deploys/ssl/plan.py")
    helpers.assert_not_contains(c, 'raise ValueError("domain is required for ssl nginx config")')
    helpers.assert_contains(c, "nginx_server_name = ctx.config.domain")


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


def test_laravel_nginx_validates_without_creating_runtime_dir():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/nginx.py")
    helpers.assert_ordering(
        c,
        "laravel-site-nginx.conf.j2",
        "nginx -t",
    )
    helpers.assert_not_contains(c, "runtime_socket_dir")


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
