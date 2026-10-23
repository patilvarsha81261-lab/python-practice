# day02_even_odd.py

def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

while True:
    value = input("Enter a number (or 'q' to quit): ")

    if value.lower() == "q":
        print("Bye! Day 2 done.")
        break

    try:
        number = int(value)
        print(f"{number} is {even_or_odd(number)}")
    except ValueError:
        print("That's not a valid number. Please type digits only.")