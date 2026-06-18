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
    helpers.assert_contains(c, "bonesremote.install_authorized_key")
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
    helpers.assert_contains(c, "doctor.run")


def test_runtime_applies_apparmor_and_nginx():
    c = helpers.read(RUNTIME_APPARMOR)
    helpers.assert_contains(c, "apparmor_parser -r")
    helpers.assert_contains(c, "aa-enforce")
    helpers.assert_contains(c, "apparmor_enabled_param")
    c2 = helpers.read(RUNTIME_NGINX)
    helpers.assert_contains(c2, "per-site nginx")


def test_runtime_plan_ordering():
    c = helpers.read(RUNTIME_PLAN)
    helpers.assert_ordering(
        c,
        "packages.install_apt",
        "template_runtime.load",
    )


def test_runtime_excludes_ssl_logic():
    c = helpers.read(RUNTIME_PLAN)
    helpers.assert_not_contains(c, "certbot")


def test_runtime_socket_dir_runtime_user_owned():
    c = helpers.read(RUNTIME_NGINX)
    helpers.assert_contains(c, 'path=paths["runtime_socket_dir"]')
    helpers.assert_contains(c, 'user=data["runtime_user"]')
    helpers.assert_contains(c, 'group=data["runtime_group"]')
    helpers.assert_contains(c, 'mode="0750"')


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


def test_runtime_nginx_falls_back_when_ssl_domain_empty():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/deploys/runtime/nginx.py")
    helpers.assert_contains(c, 'data.get("ssl_domain") or "_"')


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


def test_laravel_php_fpm_validates_before_enable():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/php_fpm.py")
    helpers.assert_ordering(
        c,
        "--test --fpm-config",
        "Enable and start per-project PHP-FPM service",
    )


def test_laravel_creates_socket_dir_before_nginx_validation():
    c = helpers.read(helpers.SRC_DIR / "bonesinfra/runtimes/laravel/nginx.py")
    helpers.assert_ordering(
        c,
        "Ensure runtime socket directory exists before nginx validation",
        "nginx -t",
    )
