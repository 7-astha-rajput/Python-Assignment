# 1Quest
text = input("Enter string: ")
vowels = consonants = digits = special = 0

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)

# 2 Quest
sentence = input("Enter sentence: ")
words = sentence.split()
rev_words = []

for w in words:
    rev_words.append(w[::-1])

output = " ".join(rev_words)
print("Result:", output)

#3 Quest

value = input("Enter string: ")

if value == value[::-1]:
    print("Palindrome String")
else:
    print("Not a Palindrome String")

#4 Quest

name = input("Enter string: ")
count = {}

for char in name:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

for key, val in count.items():
    print(key, ":", val)

# 5Quest
name = "Astha"

try:
    name[0] = 'Z'
except TypeError as err:
    print("Error:", err)
