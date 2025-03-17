import json
import csv

def load_tasks(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("\nTask List:")
    print("ID | Task Name | Completed | Priority")
    print("-" * 40)
    for task in tasks:
        print(f"{task['id']} | {task['task']} | {task['completed']} | {task['priority']}")

def calculate_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = round(sum(task['priority'] for task in tasks) / total_tasks, 1) if total_tasks else 0
    
    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority}")

def convert_json_to_csv(json_filename, csv_filename):
    tasks = load_tasks(json_filename)
    
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])
    print(f"Tasks successfully saved to {csv_filename}")

def main():
    json_filename = "/Users/ibrokhimkamolov/Documents/Analytics_Studies/Python/Pythonhomework/lesson-10/homework/tasks.json"
    csv_filename = "tasks.csv"
    
    tasks = load_tasks(json_filename)
    display_tasks(tasks)
    calculate_statistics(tasks)
    convert_json_to_csv(json_filename, csv_filename)
    
    # Example modification: Mark the first task as completed
    tasks[0]['completed'] = True
    save_tasks(json_filename, tasks)
    print("\nUpdated tasks saved to tasks.json")
    
if __name__ == "__main__":
    main()