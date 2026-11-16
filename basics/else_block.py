# Try-Except-Else

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("You entered:", number)
    print("Square:", number ** 2)
