file1 = open("a.txt", "r")
file2 = open("b.txt", "r")

new = open("new.txt", "w")
new.write(file1.read())
new.write(file2.read())

file1.close()
file2.close()
new.close()
