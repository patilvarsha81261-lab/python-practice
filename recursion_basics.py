
# Recursion: Factorial, Fibonacci, Digit Sum and Power

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)


def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


# Main Program
num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a non-negative number.")
else:
    print("Factorial =", factorial(num))
    print("Fibonacci =", fibonacci(num))
    print("Sum of Digits =", sum_of_digits(num))
    print("Power of 2 =", power(2, num))

    print("\nFirst 10 Fibonacci Numbers:")
    for i in range(10):
        print(fibonacci(i), end=" ")
