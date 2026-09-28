import json
from datetime import datetime
from input_validator import valid_date, non_empty

def load_tasks(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

def next_id(tasks):
    return max((t["id"] for t in tasks), default=0) + 1

def add_task(tasks, path):
    subject = non_empty(input("Subject: "))
    title = non_empty(input("Task: "))
    deadline = input("Deadline (YYYY-MM-DD): ").strip()
    while not valid_date(deadline):
        print("Invalid date. Use YYYY-MM-DD.")
        deadline = input("Deadline (YYYY-MM-DD): ").strip()

    tasks.append({
        "id": next_id(tasks),
        "subject": subject,
        "task": title,
        "deadline": deadline,
        "status": "Pending"
    })
    save_tasks(tasks, path)
    print("Task added successfully.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nID | Subject | Task | Deadline | Status")
    print("-" * 65)
    for t in tasks:
        print(f'{t["id"]} | {t["subject"]} | {t["task"]} | {t["deadline"]} | {t["status"]}')

def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def update_task(tasks, path):
    try:
        task_id = int(input("Task ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return
    task = find_task(tasks, task_id)
    if not task:
        print("Task not found.")
        return
    new_title = input(f'New task name [{task["task"]}]: ').strip()
    new_deadline = input(f'New deadline [{task["deadline"]}]: ').strip()
    if new_title:
        task["task"] = new_title
    if new_deadline:
        if valid_date(new_deadline):
            task["deadline"] = new_deadline
        else:
            print("Invalid deadline; keeping old value.")
    save_tasks(tasks, path)
    print("Task updated.")

def delete_task(tasks, path):
    try:
        task_id = int(input("Task ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    task = find_task(tasks, task_id)
    if not task:
        print("Task not found.")
        return
    tasks.remove(task)
    save_tasks(tasks, path)
    print("Task deleted.")

def complete_task(tasks, path):
    try:
        task_id = int(input("Task ID to mark complete: "))
    except ValueError:
        print("Invalid ID.")
        return
    task = find_task(tasks, task_id)
    if not task:
        print("Task not found.")
        return
    task["status"] = "Completed"
    save_tasks(tasks, path)
    print("Task marked as completed.")
