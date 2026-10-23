# day02_even_odd.py

def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# Part 1: check single numbers until the user quits
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

# Part 2: check a range of numbers
print("\nNow let's check a range of numbers")
start = int(input("Start from: "))
end = int(input("End at: "))

for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")