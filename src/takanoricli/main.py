import click

from takanoricli import __version__
from .create import mktd


@click.group()
@click.version_option(version=__version__, prog_name="Takanori CLI")
def main():
    pass


def register_cmds():
    cmds = [
        mktd
    ]

    for cmd in cmds:
        main.add_command(cmd)


def cli():
    from importlib import metadata
    eps = metadata.entry_points()
    if eps.get("takanoricli"):
        mycli_eps = eps["takanoricli"]
        for ep in mycli_eps:
            plugin = ep.load()
            main.add_command(plugin)
    register_cmds()
    main()
