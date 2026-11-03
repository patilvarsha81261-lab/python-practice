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