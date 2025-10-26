import json
import datetime

# List to store all tasks
tasks = []

def print_menu():
    print("""1. List all tasks
2. Add a new task
3. Update an existing task
4. Delete an existing task
5. List tasks that are done
6. List tasks that are in progress
7. List tasks that are to do""")

def list_tasks(status_filter=None):
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        if status_filter is None or task["Status"] == status_filter:
            print(json.dumps(task, indent=4))

# Main program
start = input("Would you like to access your task tracker (Yes/No): ")

if start.lower() == "yes":
    while True:  # Loop to keep the program running until the user exits
        print_menu()
        action = input("Select a number for the action you would like to do (or 'exit' to quit): ")

        if action == "1":  # List all tasks
            list_tasks()

        elif action == "2":  # Add a new task
            task_id = input("Name the task (ID): ")
            description = input("Describe the task: ")
            status = input("Status of the task (e.g., 'todo', 'in-progress', 'done'): ").lower()
            created_at = datetime.datetime.now().isoformat()
            updated_at = datetime.datetime.now().isoformat()

            task = {
                "ID": task_id,
                "Description": description,
                "Status": status,
                "Created at": created_at,
                "Updated at": updated_at
            }
            tasks.append(task)
            print("Task added successfully:")
            print(json.dumps(task, indent=4))

        elif action == "3":  # Update an existing task
            task_id = input("Enter the ID of the task to update: ")
            for task in tasks:
                if task["ID"] == task_id:
                    description = input("Enter new description (leave blank to keep current): ")
                    status = input("Enter new status (todo, in-progress, done, leave blank to keep current): ").lower()
                    if description:
                        task["Description"] = description
                    if status:
                        task["Status"] = status
                    task["Updated at"] = datetime.datetime.now().isoformat()
                    print("Task updated successfully:")
                    print(json.dumps(task, indent=4))
                    break
            else:
                print("Task not found.")

        elif action == "4":  # Delete an existing task
            task_id = input("Enter the ID of the task to delete: ")
            for i, task in enumerate(tasks):
                if task["ID"] == task_id:
                    tasks.pop(i)
                    print(f"Task '{task_id}' deleted successfully.")
                    break
            else:
                print("Task not found.")

        elif action == "5":  # List tasks that are done
            list_tasks(status_filter="done")

        elif action == "6":  # List tasks that are in progress
            list_tasks(status_filter="in-progress")

        elif action == "7":  # List tasks that are to do
            list_tasks(status_filter="todo")

        elif action.lower() == "exit":  # Exit the program
            print("Exiting task tracker.")
            break

        else:
            print("Invalid action. Please select a number between 1 and 7, or 'exit'.")

else:
    print("Task tracker not started.")