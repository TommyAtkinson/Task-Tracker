import datetime
import json

created_at = datetime.datetime.now().isoformat()
updated_at = datetime.datetime.now().isoformat()

x = {
    "ID": "None",
    "Description": "None",
    "Status": "None",
    "Created at": created_at,
    "Updated at": updated_at,
}

# convert into JSON:
y = json.dumps(x, indent=4)

# the result is a JSON string:
print(y)

start = input("Would you like to access your task tracker: ")

if start == "Yes":

    print("""1. List all tasks
    2. Add a new task
    3. Update an existing task
    4. Delete an existing task
    5. Lists tasks that are done
    6. List all tasks  that are in progress
    7. List all tasks that are to do""")

    action = input("Select a number for the action you would like to do: ")

    if action == "1":



    elif action == "2":

        id = input("Name the task: ")
        description = input("Describe the task: ")
        status = input("Status of the task e.g. 'todo', 'in-progress', 'done': ")
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()


    elif action == "3":

    elif action == "4":

    elif action == "5":

    elif action == "6":

    elif action == "7":

    else: