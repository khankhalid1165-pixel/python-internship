# todo.py

TODO_FILE = "tasks.txt"


def load_tasks():
    tasks = []
    try:
        with open(TODO_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        open(TODO_FILE, "w").close()  # create empty file
    return tasks


def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for t in tasks:
            file.write(t + "\n")


def view_tasks(tasks):
    print("\nYour To-Do List:")
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()


def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added!\n")
    else:
        print("Task cannot be empty!\n")


def remove_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Enter a valid number!\n")


def main():
    tasks = load_tasks()

    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
