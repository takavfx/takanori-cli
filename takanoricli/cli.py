import os
import sys
import glob
import importlib
import takanoricli

here = os.path.abspath(os.path.dirname(__file__))


def main():
    files = glob.glob('{}/commands/*'.format(here))
    
    commands = []
    for f in files:
        basename = os.path.basename(f)
        name, _ = os.path.splitext(basename)
        commands.append(name)
    
    exclude_files = [
        '__init__',
        '__pycache__'
    ]
    for ex in exclude_files:
        if ex in exclude_files: commands.remove(ex)

    ## Get commands, identify and execute.
    if len(sys.argv) < 2:
        print('It needs command with taka.')
        print("Available commands are :", commands)
        return 0

    command = sys.argv[1]

    if command == '--version' or command == '-v':
        print('takanori-cli version :', takanoricli.__version__)

    elif command == '--help' or command == '-h':
        print("Available commands are :", commands)
        print("To read command helps, execute 'taka [command] [--help | -h]'.")

    elif command in commands:
        module = importlib.import_module('takanoricli.commands.' + command)
        module.main()
        
    else:
        print("Command or option '{command}' is not available.".format(command=command))
        print("Available commands are :", commands)
