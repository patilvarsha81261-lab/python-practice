"""number = int(input("Enter a number: "))

result = 1
for i in range(1, number + 1):
    result = result * i

print("Factorial of", number, "is", result)"""


#Twist 1: Recursive version

"""def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))"""


#Twist 2: Compare both and time them

"""import time

def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

n = int(input("Enter a number: "))

start = time.perf_counter()
a = factorial_loop(n)
loop_time = time.perf_counter() - start

start = time.perf_counter()
b = factorial_recursive(n)
recursive_time = time.perf_counter() - start

print("Loop result:", a)
print("Recursive result:", b)
print("Same answer?", a == b)
print("Loop time:", loop_time)
print("Recursive time:", recursive_time)"""



def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    num = int(input("Enter a number: "))
    print("Factorial:", factorial(num))
except ValueError:
    print("Please enter a valid integer.")

