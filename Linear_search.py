#simple linear search

"""def linearSearch(number, target):
    for number in numbers:
        if number == target:
            return 1
        return -1

numbers = [10, 20, 1, 15, 35]
target = 1
result = linearSearch(numbers, target)
if result != -1:
    print(target, "is not found in", numbers)
else:    
    print(target, "is not found in", numbers)"""



#Question 1: Find the index of the target element using Linear Search.


# Question 1: Find the index of the target element using Linear Search

def linearSearch(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


numbers = [12, 25, 37, 48, 59, 65, 72]
target = 48

result = linearSearch(numbers, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
