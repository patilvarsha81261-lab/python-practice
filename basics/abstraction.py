from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Rectangle class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Circle class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# Take input from user
length = int(input("Enter length: "))
width = int(input("Enter width: "))
radius = int(input("Enter radius: "))


# Create Rectangle object
r = Rectangle(length, width)
print("Area of Rectangle:", r.area())


# Create Circle object
c = Circle(radius)
print("Area of Circle:", c.area())