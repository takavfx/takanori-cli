from email.policy import default
import click
import datetime
from pathlib import Path


@click.command()
@click.argument("target", default=".")
@click.option("-d", "--days", default=0, help="Delta days from today's date.")
@click.option("-s", "--silent", is_flag=True, help="Execute command without confirm.")
def mktd(target: str, days: int, silent: bool):
    """Make date directories to a given path."""
    target_path = Path(target)

    today = datetime.date.today() + datetime.timedelta(days=days)
    year = str(today.year)
    month = str(today.month)
    day = str(today.day)

    year_dir = target_path.joinpath(year)
    month_dir = year_dir.joinpath(month)
    day_dir = month_dir.joinpath(day)

    if not silent:
        print("Preview :: ", day_dir.absolute())
        click.confirm('Do you want to continue?', default=True, abort=True)

    day_dir.mkdir(parents=True)
