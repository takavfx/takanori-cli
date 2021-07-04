import os
import sys
import glob
import importlib
import takacli

here = os.path.abspath(os.path.dirname(__file__))


def main():
    files = glob.glob('{}/commands/*'.format(here))

    commands = []
    for f in files:
        commands.append(os.path.basename(f))
    
    exclude_files = ['__init__.py']
    for i in exclude_files: commands.remove(i)

    command = sys.argv[1]

    if command == '--version' or command == '-v':
        print(takacli.__version__)

    elif command == '--help' or command == '-h':
        print("Available commands are :", commands)
        print("To read command helps, execute 'taka [command] [--help, -h]'.")

    elif command in commands:
        module = importlib.import_module('takacli.commands.' + command)
        module.main()
        
    else:
        print("Command '{command}' is not available.".format(command=command))
        print("Available commands are :", commands)
