#Simple Bubble sorting algorithm

numbers = [5, 2, 9, 1, 7]
print("Start:", numbers)

n = len(numbers)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print("After pass", i + 1, ":", numbers)

print("Sorted:", numbers)


# day24_sorting_race.py
# full code sorting race with bubble, selection, insertion and merge sort
import random
import time


def bubble_sort(numbers):
    items = numbers[:]                 # copy, so the original list stays the same
    comparisons = 0
    n = len(items)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:                # already sorted, stop early
            break
    return items, comparisons


def selection_sort(numbers):
    items = numbers[:]
    comparisons = 0
    n = len(items)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            comparisons += 1
            if items[j] < items[smallest]:
                smallest = j
        items[i], items[smallest] = items[smallest], items[i]
    return items, comparisons


def insertion_sort(numbers):
    items = numbers[:]
    comparisons = 0
    for i in range(1, len(items)):
        value = items[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if items[j] > value:
                items[j + 1] = items[j]
                j -= 1
            else:
                break
        items[j + 1] = value
    return items, comparisons


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers[:], 0

    middle = len(numbers) // 2
    left, count_left = merge_sort(numbers[:middle])
    right, count_right = merge_sort(numbers[middle:])

    merged = []
    comparisons = count_left + count_right
    i = j = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, comparisons


def watch_bubble_sort():
    text = input("Type a few numbers separated by spaces (max 10): ")
    try:
        items = [int(x) for x in text.split()]
    except ValueError:
        print("Please type only numbers")
        return

    if len(items) < 2 or len(items) > 10:
        print("Please type between 2 and 10 numbers")
        return

    print("\nStart:", items)
    n = len(items)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        print(f"After pass {i + 1}:", items)
        if not swapped:
            break
    print("Sorted:", items)


def race():
    try:
        size = int(input("How many random numbers? (10 to 3000): "))
    except ValueError:
        print("Please type a number")
        return

    if size < 10 or size > 3000:
        print("Please choose between 10 and 3000")
        return

    data = [random.randint(1, 100000) for _ in range(size)]
    expected = sorted(data)

    algorithms = [
        ("Bubble sort", bubble_sort),
        ("Selection sort", selection_sort),
        ("Insertion sort", insertion_sort),
        ("Merge sort", merge_sort),
    ]

    print(f"\n{'Algorithm':<16}{'Comparisons':>13}{'Time (s)':>12}{'Correct':>10}")
    for name, function in algorithms:
        start = time.perf_counter()
        result, comparisons = function(data)
        seconds = time.perf_counter() - start
        print(f"{name:<16}{comparisons:>13,}{seconds:>12.4f}{str(result == expected):>10}")

    start = time.perf_counter()
    result = sorted(data)
    seconds = time.perf_counter() - start
    print(f"{'Python sorted()':<16}{'-':>13}{seconds:>12.4f}{str(result == expected):>10}")


while True:
    print("\n--- Sorting Race ---")
    print("1. Watch bubble sort step by step")
    print("2. Race all algorithms on random numbers")
    print("3. Quit")
    choice = input("Choose (1-3): ")

    if choice == "1":
        watch_bubble_sort()
    elif choice == "2":
        race()
    elif choice == "3":
        print("Bye! Day 24 done.")
        break
    else:
        print("Please choose 1, 2 or 3")