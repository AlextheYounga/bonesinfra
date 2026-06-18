import sys

from bonesinfra.infra.pyinfra_runner import run as run_deploy


def run_plan(deploy, ctx):
    if not ctx.host:
        print("Error: missing host in bones.toml", file=sys.stderr)
        sys.exit(3)
    run_deploy(
        hostname=ctx.host,
        ssh_user=ctx.ssh_user,
        ssh_port=ctx.ssh_port,
        data=ctx.deploy_data,
        deploy=deploy,
    )
