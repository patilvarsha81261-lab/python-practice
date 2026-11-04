#simple version of calculator

"""a = float(input("First number: "))
op = input("Operation (+ - * /): ")
b = float(input("Second number: "))

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)
else:
    print("Unknown operation")"""

# day14_calculator.py

print("Calculator. Operations: +  -  *  /  **  %")
print("Type 'quit' at any time to stop.")

while True:
    first = input("\nFirst number: ")
    if first.lower() == "quit":
        break

    op = input("Operation (+ - * / ** %): ")
    if op.lower() == "quit":
        break

    second = input("Second number: ")
    if second.lower() == "quit":
        break

    try:
        a = float(first)
        b = float(second)
    except ValueError:
        print("Please type valid numbers")
        continue

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a / b)
    elif op == "**":
        print("Result:", a ** b)
    elif op == "%":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a % b)
    else:
        print("Unknown operation")

print("Bye! Day 14 done.")