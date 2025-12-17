#1
nums = [3, 5, 7, 5, 9, 3, 1]
unique_list = []

for x in nums:
    if x not in unique_list:
        unique_list.append(x)

print("After removing duplicates:", unique_list)
#2
numbers = [10, 15, 20, 25, 30, 35]
even_numbers = [n for n in numbers if n % 2 == 0]

print("Even numbers:", even_numbers)
#3
values = [12, 45, 7, 34, 89]
largest = second_largest = float('-inf')

for v in values:
    if v > largest:
        second_largest = largest
        largest = v
    elif v > second_largest and v != largest:
        second_largest = v

print("Second largest element:", second_largest)

#4
nested = [[4, 6, 8], [10, 20, 30], [1, 2, 3]]

for inner in nested:
    print("Sum:", sum(inner))

#5
import copy

data = [[1, 2], [3, 4]]
shallow = copy.copy(data)
deep = copy.deepcopy(data)

data[0][1] = 99

print("Original List:", data)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)
