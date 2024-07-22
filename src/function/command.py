from commands import test
from commands import start
from commands import end
from commands import list

def menu(_):
    for key in commands.keys():
        print("- ", key)
    return 0

def exit_program(_):
    print("程式即將結束...")
    return 1

commands = {
    "test": test.index,
    "menu": menu,
    "exit": exit_program,
    "start" : start.start_command,
    "end": end.end_command,
    "list": list.list_command
}

def exec_commands(command_name: str, str_arguments: str):
    for key, value in commands.items():
        if key == command_name:
            return_code = value(str_arguments)
            if return_code == 1:
                return 1
            return 0
    print("[exec_commands] no command found")
    return -1
    

def get_commands():
    return commands