
# day07_prime_number.py

# 1. Take input
try:
    number = int(input("Enter a number: "))

    # 2. Check prime number
    if number <= 1:
        print(number, "is not a prime number")

    elif number == 2:
        print(number, "is a prime number")

    else:
        is_prime = True

        # 3. Check divisibility
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        # 4. Display result
        if is_prime:
            print(number, "is a prime number")
        else:
            print(number, "is not a prime number")

except ValueError:
    print("Invalid input! Please enter a valid integer.")
