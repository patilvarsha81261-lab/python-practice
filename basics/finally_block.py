# Finally Block

try:
    number = int(input("Enter a number: "))
    print("Square:", number ** 2)

except ValueError:
    print("Please enter an integer.")

finally:
    print("Program execution completed.")
