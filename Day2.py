#1
def even_list(a):
    r = []
    for i in a:
        if i % 2 == 0:
            r.append(i)
    return r

a = [1, 2, 3, 4, 5, 6]
print("Even numbers:", even_list(a))

#2
def char_count(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

s = "astha"
print("Character count:", char_count(s))
#3
def is_pal(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False

n = 121
print("Is palindrome:", is_pal(n))
#4

def avg(*a):
    t = 0
    for i in a:
        t += i
    return t / len(a)

print("Average:", avg(10, 20, 30, 40))
#5
def common(a, b):
    r = []
    for i in a:
        if i in b and i not in r:
            r.append(i)
    return r

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print("Common elements:", common(a, b))
