# day03_fizzbuzz.py

# Simple version: 1 to 30 with 3 and 5
"""for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)"""



# day03_fizzbuzz.py

start = int(input("Start from: "))
end = int(input("End at: "))
a = int(input("First number (like 3): "))
b = int(input("Second number (like 5): "))

for i in range(start, end + 1):
    if i % a == 0 and i % b == 0:
        print("FizzBuzz")
    elif i % a == 0:
        print("Fizz")
    elif i % b == 0:
        print("Buzz")
    else:
        print(i)