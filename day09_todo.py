tasks = []

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
        print("Please choose 1, 2 or 3")