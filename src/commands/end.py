from function.task_manager import main_task_manager

def end_command(str_arguments: str) -> int:
    try:
        task_id = int(str_arguments.strip())
        return main_task_manager.end_task(task_id)
    except ValueError:
        print("Error: Task ID must be an integer.")
        return -1
    except Exception as e:
        print(f"Error: {e}")
        return -1