import json
from pathlib import Path


class Task:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def toggle_status(self):
        self.status = not self.status

    def display(self):
        return f"{self.id}.{self.name} {'✓' if self.status else '✗'}"

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'status': self.status}

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['name'], data['status'])


class TaskManager:
    def __init__(self, file_path, tasks=None):
        self.file_path = Path(file_path)
        self.tasks = tasks if tasks is not None else []

    def load_tasks(self):
        if self.file_path.exists():
            with open(self.file_path, "r") as tf:
                try:
                    data = json.load(tf)
                    self.tasks = [Task.from_dict(d) for d in data]
                except json.JSONDecodeError:
                    self.tasks.clear()
        else:
            self.file_path.touch()
            self.tasks.clear()
        return self.tasks

    def show_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(task.display())
        else:
            print("You have no tasks.")

    def add_task(self):
        user_task = input("Enter your task: ").strip()
        if user_task:
            new_task = Task(len(self.tasks) + 1, user_task, False)
            self.tasks.append(new_task)
            print("Task successfully added.")
        else:
            print("Task can't be empty.")

    def reassign_task_ids(self):
        for index, task in enumerate(self.tasks, start=1):
            task.id = index

    def delete_task(self):
        self.show_tasks()
        try:
            rm_task = int(input("Enter task number to delete: "))
        except ValueError:
            print("Task doesn't exist.")
            return

        for index, task in enumerate(self.tasks):
            if task.id == rm_task:
                del self.tasks[index]
                print("Task successfully deleted.")
                self.reassign_task_ids()
                break
        else:
            print("Task doesn't exist.")

    def change_status(self):
        self.show_tasks()
        try:
            change_task = int(input("Enter task number to change: "))
        except ValueError:
            print("Task doesn't exist.")
            return

        for task in self.tasks:
            if task.id == change_task:
                task.toggle_status()
                print("Status successfully changed.")
                break
        else:
            print("Task doesn't exist.")

    def save_tasks(self):
        with open(self.file_path, 'w') as tf:
            json.dump([task.to_dict() for task in self.tasks], tf, indent=4)

    def menu(self):
        while True:
            print("\n---Task Manager Menu---\n")
            print("1.Show Tasks")
            print("2.Add Tasks")
            print("3.Remove Tasks")
            print("4.Change Tasks")
            print("5.Exit and Save \n")

            user_input = input("Choose an option (1-5): ")

            if user_input == "1":
                self.show_tasks()
            elif user_input == "2":
                self.add_task()
            elif user_input == "3":
                self.delete_task()
            elif user_input == "4":
                self.change_status()
            elif user_input == "5":
                self.save_tasks()
                break
            else:
                print("Enter a valid number.")


if __name__ == "__main__":
    task_manager = TaskManager("tasks.json")
    task_manager.load_tasks()
    task_manager.menu()
