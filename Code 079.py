a = int(input("First Number: "))
b = int(input("Second Number: "))

while b != 0:
    a, b = b, a % b

print("GCD =", a)
