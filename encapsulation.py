# encapsulation can be achived by variable and attribute as a private and provide getter and setter method



class Student:
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
print("rollno:", rollno)




