"""n = int(input("How many Fibonacci numbers? "))

a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b"""


#Twist 1: Generator with yield

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for number in fibonacci_generator(10):
    print(number, end=" ")