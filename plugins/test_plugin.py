name = "test plugin"
commands = ["test"]

def run(command, args):
    if command in commands:
        print(args)
    else:
        print(f"ERROR: I can't see this command on {name} commands list")