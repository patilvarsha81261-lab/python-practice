#single inheritance

# Parent class
class Animal:
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
d.bark()