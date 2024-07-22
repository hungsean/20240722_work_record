from function.task_manager import main_task_manager
from tabulate import tabulate
from wcwidth import wcswidth

def format_description(description, width):
    ellipsis = '...'
    ellipsis_width = wcswidth(ellipsis)
    current_width = wcswidth(description)
    if current_width > width:
        trimmed_description = description
        while wcswidth(trimmed_description) + ellipsis_width > width:
            trimmed_description = trimmed_description[:-1]
        return trimmed_description + ellipsis
    else:
        return description + ' ' * (width - current_width)

def list_command(_) -> int:
    try:
        description_width = 20
        tasks = [
            [task.task_id, format_description(task.description, description_width), task.start_time, task.end_time]
            for task in main_task_manager.tasks
        ]
        if not tasks:
            print("No tasks found.")
            return 0

        headers = ["Task ID", "Description", "Start Time", "End Time"]
        table = tabulate(tasks, headers, tablefmt="fancy_grid")
        print(table)
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return -1