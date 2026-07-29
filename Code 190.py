file = open("test.txt", "r")

text = file.read()

word = input("Enter word: ")

if word in text:
    print("Found")
else:
    print("Not Found")

file.close()
