tasks = []

def add_task(task):
    tasks.append({
        "title": task,
        "completed": False
    })
    
def export_tasks():

    with open("tasks.txt", "w") as file:

        for task in tasks:
            file.write(task["title"] + "\n")

def view_tasks():

    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks")

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "

        print(f"{index}. [{status}] {task['title']}")


def main():

    add_task("Study Git")
    add_task("Practice Django")

    view_tasks()


if __name__ == "__main__":
    main()