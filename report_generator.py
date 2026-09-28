from datetime import datetime

def generate_report(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t["status"] == "Completed")
    pending = total - completed
    rate = completed / total * 100 if total else 0

    print("\n========== STUDY REPORT ==========")
    print(f"Generated on    : {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Total tasks     : {total}")
    print(f"Completed       : {completed}")
    print(f"Pending         : {pending}")
    print(f"Completion rate : {rate:.2f}%")
    print("\nTask Summary:")
    for t in tasks:
        print(f'{t["id"]}. {t["task"]} | {t["subject"]} | {t["deadline"]} | {t["status"]}')
