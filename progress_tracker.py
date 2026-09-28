def show_progress(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t["status"] == "Completed")
    pending = total - completed
    percentage = (completed / total * 100) if total else 0

    print("\n===== PROGRESS =====")
    print(f"Total Tasks      : {total}")
    print(f"Completed        : {completed}")
    print(f"Pending          : {pending}")
    print(f"Completion Rate  : {percentage:.2f}%")

    subjects = {}
    for task in tasks:
        subject = task["subject"]
        subjects.setdefault(subject, [0, 0])
        subjects[subject][0] += 1
        if task["status"] == "Completed":
            subjects[subject][1] += 1

    if subjects:
        print("\nSubject-wise Progress:")
        for subject, (count, done) in subjects.items():
            rate = done / count * 100
            print(f"{subject}: {rate:.2f}%")
