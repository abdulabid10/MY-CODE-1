file = open("test.txt", "r")

text = file.read().lower()

count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print(count)

file.close()
