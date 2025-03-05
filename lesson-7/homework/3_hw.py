import json
import csv
from abc import ABC, abstractmethod

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(data["task_id"], data["title"], data["description"], data.get("due_date"), data["status"])

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class StorageStrategy(ABC):
    @abstractmethod
    def save(self, tasks):
        pass
    
    @abstractmethod
    def load(self):
        pass

class JSONStorage(StorageStrategy):
    FILE_NAME = "tasks.json"
    
    def save(self, tasks):
        with open(self.FILE_NAME, "w") as file:
            json.dump([task.to_dict() for task in tasks], file)

    def load(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                return [Task.from_dict(data) for data in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

class CSVStorage(StorageStrategy):
    FILE_NAME = "tasks.csv"
    
    def save(self, tasks):
        with open(self.FILE_NAME, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                reader = csv.DictReader(file)
                return [Task.from_dict(row) for row in reader]
        except FileNotFoundError:
            return []

class ToDoApp:
    def __init__(self, storage_strategy):
        self.storage = storage_strategy
        self.tasks = self.storage.load()

    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD): ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ")
        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(task)
    
    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new Title: ") or task.title
                task.description = input("Enter new Description: ") or task.description
                task.due_date = input("Enter new Due Date (YYYY-MM-DD): ") or task.due_date
                task.status = input("Enter new Status (Pending/In Progress/Completed): ") or task.status
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self):
        status = input("Enter status to filter (Pending/In Progress/Completed): ")
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print("No tasks found with that status.")
            return
        for task in filtered_tasks:
            print(task)

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved successfully!")

    def menu(self):
        while True:
            print("""
Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Exit
""")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    storage_type = input("Choose storage format (json/csv): ").strip().lower()
    storage = JSONStorage() if storage_type == "json" else CSVStorage()
    app = ToDoApp(storage)
    app.menu()
