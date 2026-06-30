from bonesinfra.deploys.setup import (
    bonesremote,
    directories,
    fail2ban,
    firewall,
    packages,
    placeholder,
    sudoers,
    unattended_upgrades,
    users,
)
from bonesinfra.deploys.setup.packages import BASE_SYSTEM_PACKAGES, SUPPLEMENTARY_PACKAGES


def deploy_setup(ctx):
    paths = ctx.paths_dict
    all_pkgs = BASE_SYSTEM_PACKAGES + SUPPLEMENTARY_PACKAGES

    packages.install_system(all_pkgs)
    users.install_rust()
    users.ensure_users_and_groups(ctx)
    directories.setup_repo_and_project(ctx, paths)
    placeholder.seed(ctx, paths)
    firewall.configure(ctx)
    fail2ban.configure(ctx)
    unattended_upgrades.configure()
    users.install_authorized_key(ctx)
    bonesremote.install()
    sudoers.install(ctx, paths)
