from function.task_manager import main_task_manager

def start_command(str_arguments: str) -> int:
    try:
        description = str_arguments.strip()
        if not description:
            print("Error: Description cannot be empty.")
            return -1
        main_task_manager.start_task(description)
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return -1