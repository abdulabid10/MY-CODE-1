a = int(input("First Number: "))
b = int(input("Second Number: "))

x = a
y = b

while y != 0:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

print("LCM =", lcm)
