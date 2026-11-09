
# Multilevel Inheritance

class Animal:
    def eat(self):
        print("Animal is eating...")

    def sleep(self):
        print("Animal is sleeping...")


class Mammal(Animal):
    def walk(self):
        print("Mammal is walking...")


class Dog(Mammal):
    def bark(self):
        print("Dog is barking...")

    def display(self):
        print("This is a Dog class.")


# Creating Object
dog = Dog()

dog.display()
dog.eat()
dog.sleep()
dog.walk()
dog.bark()
