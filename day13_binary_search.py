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



"""def binary_search(numbers, target):
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


# Sorted list of 1000 numbers
numbers = list(range(1, 2000, 2))

print("List has", len(numbers), "numbers")

# Take input from user
try:
    target = int(input("Number to find: "))
except ValueError:
    print("Please enter a valid number")
    exit()

# Perform Binary Search
position, steps = binary_search(numbers, target)

# Display result
if position != -1:
    print("Element found at index:", position)
else:
    print("Element not found")

print("Binary search steps:", steps)"""


#Write a Python program to find the first occurrence (index number) of a targeted element from the given sorted list using Binary Search.



"""def first_occurrence(numbers, target):
    low = 0
    high = len(numbers) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            result = mid
            high = mid - 1

        elif numbers[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return result


numbers = [10, 20, 20, 20, 30, 40, 50]

target = int(input("Enter target element: "))

result = first_occurrence(numbers, target)

if result != -1:
    print("First occurrence found at index:", result)
else:
    print("Element not found")"""



#Write a Python program to find the last occurrence (index number) of a targeted element from the given sorted list using Binary Search.



def last_occurrence(numbers, target):
    low = 0
    high = len(numbers) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            result = mid
            low = mid + 1
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


numbers = [10, 20, 20, 20, 30, 40, 50]
target = int(input("Enter target element: "))

result = last_occurrence(numbers, target)

if result != -1:
    print("Last occurrence found at index:", result)
else:
    print("Element not found")

