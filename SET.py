#1
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference (s1 - s2):", s1 - s2)
print("Symmetric Difference:", s1 ^ s2)

#2
a = {10, 20, 30, 40}
b = {30, 40, 50}

common = a & b
a = a - common
b = b - common

print("Set A after removal:", a)
print("Set B after removal:", b)

#3
x = {1, 2}
y = {1, 2, 3, 4}

if x.issubset(y):
    print("x is a subset of y")
else:
    print("x is not a subset of y")

  
#4
  nums = {5, 12, 7, 20, 3}
limit = 10

for n in nums:
    if n > limit:
        print(n)

#5
lst = [1, 2, 3, 2, 4, 1, 5]

unique_set = set(lst)
unique_list = list(unique_set)

print("Unique List:", unique_list)
