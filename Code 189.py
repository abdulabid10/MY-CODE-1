file = open("result.txt", "w")

file.write("Rahim : 85\n")
file.write("Karim : 90")

file.close()

file = open("result.txt", "r")
print(file.read())
file.close()
