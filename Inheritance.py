#single inheritance

# Parent class
"""class Animal:
    def eat(self):
        print("Animal is eating")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Object of parent class
a = Animal()

# Object of child class
d = Dog()

# Parent object
a.eat()

# Child object
d.eat()
d.bark()"""


# write a program to create parant class student , with attribute name, rollno. 
# Create 1 child class marks that store marks of 3 sun.
#  Display the student details along with total marks and avg.
# initialize all varlues throght constructor ,by gating input values from user.


# Parent class
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

# Child class
class Marks(Student):
    def __init__(self, name, rollno, m1, m2, m3):
        super().__init__(name, rollno)

        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def display(self):
        total = self.m1 + self.m2 + self.m3
        avg = total / 3

        print("\n----- Student Details -----")
        print("Name:", self.name)
        print("Roll Number:", self.rollno)
        print("Subject 1 Marks:", self.m1)
        print("Subject 2 Marks:", self.m2)
        print("Subject 3 Marks:", self.m3)
        print("Total Marks:", total)
        print("Average Marks:", avg)


# Get input from user
name = input("Enter student name: ")
rollno = int(input("Enter roll number: "))

m1 = float(input("Enter subject 1 marks: "))
m2 = float(input("Enter subject 2 marks: "))
m3 = float(input("Enter subject 3 marks: "))

# Create object
s = Marks(name, rollno, m1, m2, m3)

# Display details
s.display()
    
         