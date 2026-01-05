tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index + 1}. {task['task']} - {status}")

def complete_task():
    view_tasks()
    task_number = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

while True:
    print("\nStudent Task Management System")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        break
    else:
        print("Invalid option.")
