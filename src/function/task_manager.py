from datetime import datetime

class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = datetime.now().isoformat()

    def end(self):
        self.end_time = datetime.now().isoformat()

    def __str__(self):
        return (f"Task ID: {self.task_id}\n"
                f"Description: {self.description}\n"
                f"Start time: {self.start_time}\n"
                f"End time: {self.end_time}\n")


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def start_task(self, description):
        task = Task(self.next_id, description)
        task.start()
        self.tasks.append(task)
        self.next_id += 1
        print(f"Started Task ID: {task.task_id}")
        return task.task_id

    def end_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id and task.end_time is None:
                task.end()
                print(f"Ended Task ID: {task.task_id}")
                return 0
        print(f"Task ID {task_id} not found or already ended.")
        return -1

    def list_tasks(self):
        for task in self.tasks:
            print(task)

main_task_manager = TaskManager()