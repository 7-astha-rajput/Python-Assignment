#1
t = (5, 9, 2, 8, 1)
max_val = min_val = t[0]

for i in t:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Maximum:", max_val)
print("Minimum:", min_val)

#2
pairs = [("A", 10), ("B", 20), ("C", 30)]
d = {}

for key, value in pairs:
    d[key] = value

print("Dictionary:", d)


#3
nums = (1, 2, 3, 2, 4, 2, 5)
target = 2
count = 0

for n in nums:
    if n == target:
        count += 1

print("Occurrence of", target, ":", count)

#4
tup = (10, [20, 30], 40)

tup[1][0] = 99   # modifying list inside tuple

print("Modified Tuple:", tup)


#5
t1 = (1, 2, 3)
t2 = (4, 5, 6)

t1, t2 = t2, t1

print("Tuple 1:", t1)
print("Tuple 2:", t2)
