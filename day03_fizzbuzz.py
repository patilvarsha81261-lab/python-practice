# day03_fizzbuzz.py
# FizzBuzz with custom range and numbers, zero check, counters and file output

# 1. Inputs come FIRST (with try/except for letters)
try:
    start = int(input("Start from: "))
    end = int(input("End at: "))
    a = int(input("First number (like 3): "))
    b = int(input("Second number (like 5): "))
except ValueError:
    print("Please type only numbers")
    exit()

# 2. Zero check
if a == 0 or b == 0:
    print("Numbers cannot be zero")
    exit()

# 3. Counters
fizz = 0
buzz = 0
fizzbuzz = 0

# 4. Loop, saving output to a file too
with open("fizzbuzz_output.txt", "w") as f:
    for i in range(start, end + 1):
        if i % a == 0 and i % b == 0:
            result = "FizzBuzz"
            fizzbuzz += 1
        elif i % a == 0:
            result = "Fizz"
            fizz += 1
        elif i % b == 0:
            result = "Buzz"
            buzz += 1
        else:
            result = str(i)

        print(result)
        f.write(result + "\n")

# 5. Summary
print("Fizz:", fizz)
print("Buzz:", buzz)
print("FizzBuzz:", fizzbuzz)
print("Saved to fizzbuzz_output.txt")