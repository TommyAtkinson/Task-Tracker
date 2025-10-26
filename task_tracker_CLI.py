import json
import sys
import os
import datetime

# File to store tasks
TASKS_FILE = "tasks_CLI.json"

# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)  # Create empty file if it doesn't exist
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: Corrupted tasks file. Starting with empty task list.")
        return []

# Save tasks to JSON file
def save_tasks(tasks):
    try:
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Get the next available ID
def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["ID"] for task in tasks) + 1

# List tasks with optional status filter
def list_tasks(tasks, status_filter=None):
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        if status_filter is None or task["Status"] in status_filter:
            print(json.dumps(task, indent=4))

# Add a new task
def add_task(tasks, description, status):
    if not description:
        print("Error: Description cannot be empty.")
        return
    if status not in ["todo", "in-progress", "done"]:
        print("Error: Status must be 'todo', 'in-progress', or 'done'.")
        return
    task = {
        "ID": get_next_id(tasks),
        "Description": description,
        "Status": status,
        "Created at": datetime.datetime.now().isoformat(),
        "Updated at": datetime.datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully:")
    print(json.dumps(task, indent=4))

# Update a task
def update_task(tasks, task_id, description=None, status=None):
    try:
        task_id = int(task_id)  # Ensure ID is an integer
    except ValueError:
        print("Error: Task ID must be a number.")
        return
    for task in tasks:
        if task["ID"] == task_id:
            if description:
                task["Description"] = description
            if status and status in ["todo", "in-progress", "done"]:
                task["Status"] = status
            elif status:
                print("Error: Status must be 'todo', 'in-progress', or 'done'.")
                return
            task["Updated at"] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully:")
            print(json.dumps(task, indent=4))
            return
    print("Task not found.")

# Delete a task
def delete_task(tasks, task_id):
    try:
        task_id = int(task_id)  # Ensure ID is an integer
    except ValueError:
        print("Error: Task ID must be a number.")
        return
    for i, task in enumerate(tasks):
        if task["ID"] == task_id:
            tasks.pop(i)
            save_tasks(tasks)
            print(f"Task '{task_id}' deleted successfully.")
            return
    print("Task not found.")

# Main program
def main():
    tasks = load_tasks()
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py <action> [arguments]")
        print("Actions: list, list-done, list-not-done, list-in-progress, add, update, delete")
        print("Examples:")
        print("  python task_tracker.py add 'Buy groceries' todo")
        print("  python task_tracker.py update 1 'Buy groceries urgently' in-progress")
        print("  python task_tracker.py delete 1")
        return

    action = sys.argv[1].lower()
    if action == "list":
        list_tasks(tasks)
    elif action == "list-done":
        list_tasks(tasks, status_filter="done")
    elif action == "list-not-done":
        list_tasks(tasks, status_filter=["todo", "in-progress"])
    elif action == "list-in-progress":
        list_tasks(tasks, status_filter="in-progress")
    elif action == "add" and len(sys.argv) == 4:
        add_task(tasks, sys.argv[2], sys.argv[3])
    elif action == "update" and len(sys.argv) >= 3:
        description = sys.argv[3] if len(sys.argv) > 3 else None
        status = sys.argv[4] if len(sys.argv) > 4 else None
        update_task(tasks, sys.argv[2], description, status)
    elif action == "delete" and len(sys.argv) == 3:
        delete_task(tasks, sys.argv[2])
    else:
        print("Invalid action or arguments.")

if __name__ == "__main__":
    main()