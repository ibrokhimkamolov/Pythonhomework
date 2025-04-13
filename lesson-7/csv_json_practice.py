import csv
import json

# Task class
class Task:
    def __init__(self, task_id, title, description, due_date='', status='Pending'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_list(self):
        return [self.task_id, self.title, self.description, self.due_date, self.status]

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


# --- CSV functions ---
def save_tasks_csv(tasks, filename='tasks.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow(task.to_list())

def load_tasks_csv(filename='tasks.csv'):
    tasks = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Avoid empty lines
                    task = Task(*row)
                    tasks.append(task)
    except FileNotFoundError:
        pass
    return tasks


# --- JSON functions ---
def save_tasks_json(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

def load_tasks_json(filename='tasks.json'):
    tasks = []
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data:
                task = Task(**item)
                tasks.append(task)
    except FileNotFoundError:
        pass
    return tasks


# --- Main program ---
def main():
    print("Welcome to the To-Do Application!")
    print("Choose storage format:")
    print("1. CSV")
    print("2. JSON")
    file_format = input("Enter 1 or 2: ")

    if file_format == '1':
        load_tasks = load_tasks_csv
        save_tasks = save_tasks_csv
    else:
        load_tasks = load_tasks_json
        save_tasks = save_tasks_json

    tasks = load_tasks()

    while True:
        print("\nTo-Do Menu:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            desc = input("Enter Description: ")
            due = input("Enter Due Date (YYYY-MM-DD) [optional]: ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            tasks.append(Task(task_id, title, desc, due, status))
            print("✅ Task added!")

        elif choice == '2':
            print("\n📋 All Tasks:")
            for task in tasks:
                print(task)

        elif choice == '3':
            id_to_update = input("Enter Task ID to update: ")
            for task in tasks:
                if task.task_id == id_to_update:
                    print("Leave empty to keep the current value.")
                    title = input("Enter new Title: ") or task.title
                    desc = input("Enter new Description: ") or task.description
                    due = input("Enter new Due Date: ") or task.due_date
                    status = input("Enter new Status: ") or task.status

                    task.title = title
                    task.description = desc
                    task.due_date = due
                    task.status = status
                    print("✅ Task updated!")
                    break
            else:
                print("⚠️ Task not found.")

        elif choice == '4':
            id_to_delete = input("Enter Task ID to delete: ")
            before = len(tasks)
            tasks = [task for task in tasks if task.task_id != id_to_delete]
            if len(tasks) < before:
                print("✅ Task deleted.")
            else:
                print("⚠️ Task not found.")

        elif choice == '5':
            status_filter = input("Enter status to filter by (e.g., Pending): ")
            filtered = [task for task in tasks if task.status.lower() == status_filter.lower()]
            print(f"\n📌 Tasks with status '{status_filter}':")
            for task in filtered:
                print(task)

        elif choice == '6':
            save_tasks(tasks)
            print("💾 Tasks saved successfully.")

        elif choice == '7':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


# --- Start the program ---
if __name__ == '__main__':
    main()