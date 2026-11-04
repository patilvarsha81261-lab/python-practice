#simple code

# Parent class
class Animal:
    def sound(self):
        print("Animal makes sound")


# Child class 1
class Dog(Animal):
    def sound(self):
        print("Dog barks")


# Child class 2
class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Create objects
a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()
