import datetime
import subprocess
from PyInquirer import (
    prompt,
    style_from_dict
)
from pathlib import Path

def create_directory(target_str, days=0, silent=False):
    if target_str is None:
        target= Path('.')
    else:
        target = Path(target_str)

    today = datetime.date.today() + datetime.timedelta(days=days)
    year  = str(today.year)
    month = str(today.month)
    day   = str(today.day)

    year_dir  = target.joinpath(year)
    month_dir = year_dir.joinpath(month)
    day_dir   = month_dir.joinpath(day)

    if not silent:
        print("Preview :: ", day_dir.absolute())
        questions = {
            'type': 'confirm',
            'name': 'confirm',
            'message': 'Is it okay to create the directories?',
            'default': True,
        }
        answers = prompt(questions)
        if not answers['confirm']:
            return

    day_dir.mkdir(parents=True)
    # subprocess.run(["explorer", day_dir])