file = open("test.txt", "r")

text = file.read()

print(len(text.split()))

file.close()
