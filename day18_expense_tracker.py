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
        
        
        
        
        
        
        
        
# day18_expense_tracker.py
import json
from datetime import datetime

FILENAME = "expenses.json"
CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Other"]


def load_expenses():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=2)


def choose_category():
    for i, category in enumerate(CATEGORIES, 1):
        print(f"  {i}. {category}")
    try:
        number = int(input("Category number: "))
        if 1 <= number <= len(CATEGORIES):
            return CATEGORIES[number - 1]
    except ValueError:
        pass
    print("Invalid choice, using Other")
    return "Other"


def add_expense(expenses):
    name = input("What did you spend on? ").strip()
    if name == "":
        print("Name cannot be empty")
        return

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Please type a number")
        return

    if amount <= 0:
        print("Amount must be more than zero")
        return

    category = choose_category()
    expenses.append({
        "name": name,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d"),
    })
    save_expenses(expenses)
    print("Added")


def show_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses yet")
        return

    print(f"\n{'#':<4}{'Date':<12}{'Category':<10}{'Name':<20}{'Amount':>10}")
    for i, item in enumerate(expenses, 1):
        print(f"{i:<4}{item['date']:<12}{item['category']:<10}"
              f"{item['name']:<20}{item['amount']:>10.2f}")


def show_summary(expenses):
    if len(expenses) == 0:
        print("No expenses yet")
        return

    totals = {}
    for item in expenses:
        category = item["category"]
        totals[category] = totals.get(category, 0) + item["amount"]

    print("\nSpending by category:")
    for category, total in sorted(totals.items(), key=lambda pair: pair[1], reverse=True):
        print(f"{category:<10}{total:>10.2f}")
    print(f"{'Total':<10}{sum(totals.values()):>10.2f}")


def delete_expense(expenses):
    if len(expenses) == 0:
        print("No expenses yet")
        return

    show_expenses(expenses)
    try:
        number = int(input("Number to delete: "))
    except ValueError:
        print("Please type a number")
        return

    if number < 1 or number > len(expenses):
        print("No expense with that number")
        return

    removed = expenses.pop(number - 1)
    save_expenses(expenses)
    print("Deleted:", removed["name"])


expenses = load_expenses()

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. Show all expenses")
    print("3. Spending by category")
    print("4. Delete an expense")
    print("5. Quit")
    choice = input("Choose (1-5): ")

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        show_expenses(expenses)
    elif choice == "3":
        show_summary(expenses)
    elif choice == "4":
        delete_expense(expenses)
    elif choice == "5":
        print("Bye! Day 18 done.")
        break
    else:
        print("Please choose 1 to 5")