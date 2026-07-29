source = open("test.txt", "r")
data = source.read()
source.close()

copy = open("copy.txt", "w")
copy.write(data)
copy.close()
