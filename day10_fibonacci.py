"""n = int(input("How many Fibonacci numbers? "))

a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b"""


#Twist 1: Generator with yield

"""def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for number in fibonacci_generator(10):
    print(number, end=" ")"""


#Twist 2: Check if a number is a Fibonacci number


"""def is_fibonacci(x):
    a, b = 0, 1
    while a < x:
        a, b = b, a + b
    return a == x

num = int(input("Enter a number: "))
if is_fibonacci(num):
    print(num, "is a Fibonacci number")
else:
    print(num, "is not a Fibonacci number")"""


#Full combined code



# day10_fibonacci.py

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_fibonacci(x):
    a, b = 0, 1
    while a < x:
        a, b = b, a + b
    return a == x


try:
    count = int(input("How many Fibonacci numbers to show? "))
    if count < 0:
        print("Please type a positive number")
        exit()
except ValueError:
    print("Please type a valid number")
    exit()

print("Fibonacci series:")
for number in fibonacci_generator(count):
    print(number, end=" ")
print()

try:
    num = int(input("\nCheck a number: "))
except ValueError:
    print("Please type a valid number")
    exit()

if num >= 0 and is_fibonacci(num):
    print(num, "is a Fibonacci number")
else:
    print(num, "is not a Fibonacci number")