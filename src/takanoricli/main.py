import click

from .create import mkdd


@click.group()
def main():
    pass


def register_cmds():
    cmds = [
        mkdd
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
