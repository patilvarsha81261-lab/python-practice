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