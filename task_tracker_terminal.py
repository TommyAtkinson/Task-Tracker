import json
import os
import datetime

# File to store tasks
TASKS_FILE = "tasks_terminal.json"

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

# Print the menu
def print_menu():
    print("""1. List all tasks
2. Add a new task
3. Update an existing task
4. Delete an existing task
5. List tasks that are done
6. List tasks that are in progress
7. List tasks that are to do
8. List tasks that are not done
9. Exit""")

# List tasks with optional status filter
def list_tasks(tasks, status_filter=None):
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        if status_filter is None or task["Status"] in status_filter:
            print(json.dumps(task, indent=4))

# Main program
def main():
    tasks = load_tasks()
    start = input("Would you like to access your task tracker (Yes/No): ")

    if start.lower() == "yes":
        while True:
            print_menu()
            action = input("Select a number for the action you would like to do (1-9): ")

            if action == "1":  # List all tasks
                list_tasks(tasks)

            elif action == "2":  # Add a new task
                description = input("Describe the task: ").strip()
                if not description:
                    print("Error: Description cannot be empty.")
                    continue
                status = input("Status of the task (todo, in-progress, done): ").lower().strip()
                if status not in ["todo", "in-progress", "done"]:
                    print("Error: Status must be 'todo', 'in-progress', or 'done'.")
                    continue
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

            elif action == "3":  # Update an existing task
                task_id = input("Enter the ID of the task to update: ").strip()
                try:
                    task_id = int(task_id)
                except ValueError:
                    print("Error: Task ID must be a number.")
                    continue
                for task in tasks:
                    if task["ID"] == task_id:
                        description = input("Enter new description (leave blank to keep current): ").strip()
                        status = input("Enter new status (todo, in-progress, done, leave blank to keep current): ").lower().strip()
                        if description:
                            task["Description"] = description
                        if status:
                            if status not in ["todo", "in-progress", "done"]:
                                print("Error: Status must be 'todo', 'in-progress', or 'done'.")
                                continue
                            task["Status"] = status
                        task["Updated at"] = datetime.datetime.now().isoformat()
                        save_tasks(tasks)
                        print("Task updated successfully:")
                        print(json.dumps(task, indent=4))
                        break
                else:
                    print("Task not found.")

            elif action == "4":  # Delete an existing task
                task_id = input("Enter the ID of the task to delete: ").strip()
                try:
                    task_id = int(task_id)
                except ValueError:
                    print("Error: Task ID must be a number.")
                    continue
                for i, task in enumerate(tasks):
                    if task["ID"] == task_id:
                        tasks.pop(i)
                        save_tasks(tasks)
                        print(f"Task '{task_id}' deleted successfully.")
                        break
                else:
                    print("Task not found.")

            elif action == "5":  # List tasks that are done
                list_tasks(tasks, status_filter="done")

            elif action == "6":  # List tasks that are in progress
                list_tasks(tasks, status_filter="in-progress")

            elif action == "7":  # List tasks that are to do
                list_tasks(tasks, status_filter="todo")

            elif action == "8":  # List tasks that are not done
                list_tasks(tasks, status_filter=["todo", "in-progress"])

            elif action == "9":  # Exit the program
                print("Exiting task tracker.")
                break

            else:
                print("Invalid action. Please select a number between 1 and 9.")

    else:
        print("Task tracker not started.")

if __name__ == "__main__":
    main()