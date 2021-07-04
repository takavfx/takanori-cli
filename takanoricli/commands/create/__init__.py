"""Create commands set.

Usage:
    taka create daydir [--silent|-s] [--days=<days>] [<target>]
    taka create daydir [--silent|-s] <target> 

Options:
    --silent, -s    Silent results before create directory.
    --days=<days>   Days to timedelta from today. [default: 0]
    target          Target directory to create sub-directories.
"""

from docopt import docopt

from .func import create_directory

def main():
    args = docopt(__doc__)
    
    if args['daydir']:
        create_directory(
                args['<target>'],
                int(args['--days']),
                silent=args['--silent']
            )