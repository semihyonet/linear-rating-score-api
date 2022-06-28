import os


def database_migrate():
    commands = ["cd ..", 'python3 -m manage migrate accommodations', "python3 -m manage migrate review"]
    for command in commands:
        os.system(command)


