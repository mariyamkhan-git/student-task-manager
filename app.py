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

def main():
    print("Student Task Manager")

    add_task("Study Git")
    add_task("Study Django")

    print(tasks)


if __name__ == "__main__":
    main()