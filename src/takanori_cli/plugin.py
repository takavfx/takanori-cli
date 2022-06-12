import click
from importlib import metadata
from cookiecutter.main import cookiecutter


@click.group()
def plugin():
    """Commands for Takanori CLI plugin."""
    pass


@plugin.command()
def create():
    """Create Takanori CLI plugin."""
    cookiecutter("https://github.com/takavfx/takanori-cli-plugin-template.git")


@plugin.command()
def info():
    """Display loaded Takanori CLI plugins."""
    eps = metadata.entry_points()
    if eps.get("takanoricli"):
        mycli_eps = eps["takanoricli"]
        for ep in mycli_eps:
            print("+", ep.name, "=", ep.value)
    else:
        print("- Coudn't find any Takanori CLI plugins.")
