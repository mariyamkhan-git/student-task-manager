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
        
def mark_task_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"Task '{tasks[index]['title']}' marked as completed.")
    else:
        print("Invalid task number.")


def main():
    add_task("Study Git")
    add_task("Practice Django")

    print("Before completion:")
    view_tasks()

    mark_task_completed(0)

    print("\nAfter completion:")
    view_tasks()

if __name__ == "__main__":
    main()