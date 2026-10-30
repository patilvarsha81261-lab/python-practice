"""tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Quit")
    choice = input("Choose (1-3): ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task)
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Please choose :1, 2 or 3")"""






# day09_todo.py

FILENAME = "todo.txt"


def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for i, task in enumerate(tasks, 1):
            print(i, task)


def get_task_number(tasks):
    try:
        number = int(input("Task number: "))
    except ValueError:
        print("Please type a number")
        return None
    if number < 1 or number > len(tasks):
        print("No task with that number")
        return None
    return number - 1


tasks = load_tasks()

while True:
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Quit")
    choice = input("Choose (1-5): ")

    if choice == "1":
        text = input("Enter a task: ").strip()
        if text:
            tasks.append("[ ] " + text)
            save_tasks(tasks)
            print("Task added")
        else:
            print("Task cannot be empty")

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        show_tasks(tasks)
        index = get_task_number(tasks)
        if index is not None:
            tasks[index] = tasks[index].replace("[ ]", "[x]", 1)
            save_tasks(tasks)
            print("Marked as done")

    elif choice == "4":
        show_tasks(tasks)
        index = get_task_number(tasks)
        if index is not None:
            removed = tasks.pop(index)
            save_tasks(tasks)
            print("Deleted:", removed)

    elif choice == "5":
        print("Bye! Day 9 done.")
        break

    else:
        print("Please choose 1 to 5")
