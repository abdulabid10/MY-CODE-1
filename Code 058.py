a = float(input("First Side: "))
b = float(input("Second Side: "))
c = float(input("Third Side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")
