#simple version of bank account

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount
            print("Withdrew", amount)


account = BankAccount("Varsha", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(500)
print("Balance:", account.balance)








# day15_bank_account.py

FILENAME = "balance.txt"


class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = self.load_balance()
        self.history = []

    def load_balance(self):
        try:
            with open(FILENAME, "r") as f:
                return float(f.read())
        except (FileNotFoundError, ValueError):
            return 0.0

    def save_balance(self):
        with open(FILENAME, "w") as f:
            f.write(str(self.balance))

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be more than zero")
        self.balance += amount
        self.history.append(f"Deposited {amount}")
        self.save_balance()

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be more than zero")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"You only have {self.balance}, cannot withdraw {amount}"
            )
        self.balance -= amount
        self.history.append(f"Withdrew {amount}")
        self.save_balance()

    def show_history(self):
        if len(self.history) == 0:
            print("No transactions yet")
        else:
            for i, item in enumerate(self.history, 1):
                print(i, item)


account = BankAccount("Varsha")

while True:
    print(f"\n--- {account.owner}'s Account ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show balance")
    print("4. Show history")
    print("5. Quit")
    choice = input("Choose (1-5): ")

    if choice == "1" or choice == "2":
        try:
            amount = float(input("Amount: "))
            if choice == "1":
                account.deposit(amount)
                print("Deposited", amount)
            else:
                account.withdraw(amount)
                print("Withdrew", amount)
        except InsufficientFundsError as error:
            print("Error:", error)
        except ValueError as error:
            print("Error:", error)

    elif choice == "3":
        print("Balance:", account.balance)

    elif choice == "4":
        account.show_history()

    elif choice == "5":
        print("Bye! Day 15 done.")
        break

    else:
        print("Please choose 1 to 5")