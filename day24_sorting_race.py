numbers = [5, 2, 9, 1, 7]
print("Start:", numbers)

n = len(numbers)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print("After pass", i + 1, ":", numbers)

print("Sorted:", numbers)