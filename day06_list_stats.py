
# day06_list_stats.py
from collections import Counter

# 1. Take input
text = input("Enter numbers separated by commas: ")

try:
    nums = [int(x.strip()) for x in text.split(",")]

    if not nums:
        print("Please enter at least one number")
        exit()

except ValueError:
    print("Invalid input! Please enter only numbers.")
    exit()

# 2. Calculate statistics
total = sum(nums)
maximum = max(nums)
minimum = min(nums)
average = total / len(nums)

# 3. Sort numbers
sorted_nums = sorted(nums)

# 4. Calculate Median
n = len(sorted_nums)
mid = n // 2

if n % 2 == 0:
    median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
else:
    median = sorted_nums[mid]

# 5. Calculate Mode
count = Counter(nums)
mode = count.most_common(1)[0][0]

# 6. Display results
print("\n----- List Statistics -----")
print("Numbers:", nums)
print("Sum:", total)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)
print("Median:", median)
print("Mode:", mode)
print("Ascending Order:", sorted_nums)
print("Descending Order:", sorted(nums, reverse=True))
