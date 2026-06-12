import sys
import json

action = sys.argv[1]

if action == "add":
    task_description = sys.argv[2]
    print("Adding task:", task_description)

    with open("./task.json", "r") as f:
        existing_tasks = json.load(f)

        new_item = {
            "id": len(existing_tasks) + 1,
            "description": task_description,
            "status": "todo"
        }

        existing_tasks.append(new_item)

        with open("./task.json", "w") as f:
            json.dump(existing_tasks, f, indent=4)

elif action == "update":
    task_id = int(sys.argv[2])
    new_description = sys.argv[3]

    with open("./task.json", "r") as f:
        existing_tasks = json.load(f)

    for task in existing_tasks:
        if task["id"] == task_id:
            task["description"] = new_description

    with open("./task.json", "w") as f:
        json.dump(existing_tasks, f, indent=4)

elif action == "delete":
    task_id = int(sys.argv[2])

    with open("./task.json", "r") as f:
        existing_tasks = json.load(f)

    existing_tasks = [task for task in existing_tasks if task["id"] != task_id]

    with open("./task.json", "w") as f:
        json.dump(existing_tasks, f, indent=4)
    
    print(f"Task {task_id} has been deleted successfully!")

elif action in ["mark-in-progress", "mark-done"]:
    task_id = int(sys.argv[2])

    new_status = "in-progress" if action == "mark-in-progress" else "done"

    with open("./task.json", "r") as f:
        existing_tasks = json.load(f)

    for task in existing_tasks:
        if task["id"] == task_id:
            task["status"] = new_status

    with open("./task.json", "w") as f:
        json.dump(existing_tasks, f, indent=4)

    print(f"Task {task_id} marked as {new_status}!")

elif action == "list":

    with open("./task.json", "r") as f:
        existing_list = json.load(f)
    
    print("You want to list all tasks!")
    for task in existing_list:
        print(f"[{task['status']}] ID: {task['id']} - {task['description']}")

else:
    print("I don't know that command.")

