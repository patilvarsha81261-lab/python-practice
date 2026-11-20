expenses = []

while True:
    print("\n1. Add expense")
    print("2. Show expenses")
    print("3. Show total")
    print("4. Quit")
    choice = input("Choose (1-4): ")

    if choice == "1":
        name = input("What did you spend on? ")
        amount = float(input("Amount: "))
        expenses.append({"name": name, "amount": amount})
        print("Added")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet")
        else:
            for i, item in enumerate(expenses, 1):
                print(i, item["name"], item["amount"])

    elif choice == "3":
        total = 0
        for item in expenses:
            total = total + item["amount"]
        print("Total:", total)

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Please choose 1 to 4")