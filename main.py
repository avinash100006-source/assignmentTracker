from task_manager import load_tasks, add_task, list_tasks, update_task, delete_task, complete_task
from progress_tracker import show_progress
from deadline_manager import show_deadlines
from report_generator import generate_report

DATA_FILE = "data/tasks.json"

def menu():
    print("\n===== STUDENT STUDY & ASSIGNMENT TRACKER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. View Progress")
    print("7. View Deadlines")
    print("8. Generate Report")
    print("9. Exit")

def main():
    tasks = load_tasks(DATA_FILE)
    while True:
        menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task(tasks, DATA_FILE)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            update_task(tasks, DATA_FILE)
        elif choice == "4":
            delete_task(tasks, DATA_FILE)
        elif choice == "5":
            complete_task(tasks, DATA_FILE)
        elif choice == "6":
            show_progress(tasks)
        elif choice == "7":
            show_deadlines(tasks)
        elif choice == "8":
            generate_report(tasks)
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-9.")

if __name__ == "__main__":
    main()
