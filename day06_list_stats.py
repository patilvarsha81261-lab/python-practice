#list 

"""nums = [4, 8, 15, 16, 23, 42]

print("Numbers:", nums)
print("Sum:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Average:", sum(nums) / len(nums))
print("Sorted (high to low):", sorted(nums, reverse=True))"""







# day06_list_stats.py
from collections import Counter

# 1. Create nums FIRST
try:
    text = input("Enter numbers separated by commas: ")
    nums = [int(x) for x in text.split(",")]
except ValueError:
    print("Please type only numbers separated by commas")
    exit()

# 2. Median
sorted_nums = sorted(nums)
n = len(sorted_nums)
mid = n // 2

if n % 2 == 1:
    median = sorted_nums[mid]
else:
    median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2

# 3. Mode (uses nums, so it must come after step 1)
mode = Counter(nums).most_common(1)[0][0]

# 4. Print results
print("Numbers:", nums)
print("Sum:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Average:", sum(nums) / n)
print("Median:", median)
print("Mode:", mode)
print("Sorted (high to low):", sorted(nums, reverse=True))