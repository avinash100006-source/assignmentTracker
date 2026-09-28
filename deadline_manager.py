from datetime import datetime

def show_deadlines(tasks):
    today = datetime.now().date()
    upcoming = []
    overdue = []

    for task in tasks:
        try:
            date = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
        except ValueError:
            continue
        if task["status"] != "Completed":
            if date < today:
                overdue.append(task)
            else:
                upcoming.append(task)

    upcoming.sort(key=lambda x: x["deadline"])
    overdue.sort(key=lambda x: x["deadline"])

    print("\n===== DEADLINES =====")
    print("\nOverdue:")
    if overdue:
        for t in overdue:
            print(f'- {t["task"]} ({t["subject"]}) - {t["deadline"]}')
    else:
        print("None")

    print("\nUpcoming:")
    if upcoming:
        for t in upcoming:
            print(f'- {t["task"]} ({t["subject"]}) - {t["deadline"]}')
    else:
        print("None")
