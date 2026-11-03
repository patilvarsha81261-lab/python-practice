"""numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = int(input("Number to find: "))

low = 0
high = len(numbers) - 1
steps = 0
found = False

while low <= high:
    steps = steps + 1
    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Found at position", mid)
        found = True
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if found == False:
    print("Not found")

print("Steps taken:", steps)"""


# day13_binary_search.py


def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2

        if numbers[mid] == target:
            return mid, steps
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, steps


def linear_search(numbers, target):
    steps = 0

    for i in range(len(numbers)):
        steps += 1
        if numbers[i] == target:
            return i, steps

    return -1, steps


# 1. A sorted list of 1000 numbers: 1, 3, 5, ... 1999
numbers = list(range(1, 2000, 2))
print("List has", len(numbers), "numbers (1, 3, 5, ... 1999)")

# 2. Ask for the target
try:
    target = int(input("Number to find: "))
except ValueError:
    print("Please type a valid number")
    exit()

# 3. Run both searches
b_pos, b_steps = binary_search(numbers, target)
l_pos, l_steps = linear_search(numbers, target)

# 4. Show results
if b_pos == -1:
    print("Not found in the list")
else:
    print("Found at position", b_pos)

print("Binary search steps:", b_steps)
print("Linear search steps:", l_steps)