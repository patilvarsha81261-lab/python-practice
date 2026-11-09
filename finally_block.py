
# Square of a Number with Exception Handling

try:
    number = int(input("Enter an integer: "))

    square = number ** 2

    print("Number:", number)
    print("Square:", square)

    if number > 0:
        print("Number is positive.")
    elif number < 0:
        print("Number is negative.")
    else:
        print("Number is zero.")

except ValueError:
    print("Invalid input! Please enter an integer.")

finally:
    print("Program execution completed.")
