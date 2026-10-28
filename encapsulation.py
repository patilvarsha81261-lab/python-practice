# encapsulation can be achived by variable and attribute as a private and provide getter and setter method



"""class Student:
    def __init__(self):
        self.__name=""
        self.__rollno=0

    def setMethod(self, name, rollno):
        self.__name = name
        self.__rollno=rollno

    def getMethod(self):
        return self.__name , self.__rollno

student = Student()

name = input("enter name:")
rollno = input("enter rollno:")

student.setMethod(name, rollno)

name,rollno = student.getMethod()

print("name:",name)
print("rollno:", rollno)"""


"""Q1. Write a Python program to create a class BankAccount that performs basic banking operations.

The program should satisfy the following requirements:
1. Create a class named BankAccount with one attribute, balance.
2. Define a method deposit(amount) to deposit the specified amount into the account.
3. Define a method withdraw(amount) to withdraw the specified amount from the account, provided sufficient balance is available.
4. Define a method getBalance() that returns the current account balance.
5. Create an object of the BankAccount class.
6. Accept the deposit and withdrawal amounts from the user.
7. Display appropriate messages after each transaction and show the final account balance."""


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def getBalance(self):
        return self.balance


b = BankAccount()

amount = int(input("Enter deposit amount: "))
b.deposit(amount)

amount = int(input("Enter withdraw amount: "))
b.withdraw(amount)

print("Current Balance:", b.getBalance())



        
    
    





