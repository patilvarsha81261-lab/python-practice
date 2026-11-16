# Custom Exception

class InvalidMarksError(Exception):
    pass

try:
    marks = float(input("Enter marks (0-100): "))

    if not 0 <= marks <= 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")

    print("Marks:", marks)

except ValueError:
    print("Please enter a valid number.")

except InvalidMarksError as error:
    print("Error:", error)
