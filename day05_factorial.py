"""number = int(input("Enter a number: "))

result = 1
for i in range(1, number + 1):
    result = result * i

print("Factorial of", number, "is", result)"""


#Twist 1: Recursive version

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

