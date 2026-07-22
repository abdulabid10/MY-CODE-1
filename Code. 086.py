n = int(input("Enter a number: "))

square = n * n
sum_digit = 0

while square > 0:
    sum_digit += square % 10
    square //= 10

if sum_digit == n:
    print("Neon Number")
else:
    print("Not a Neon Number")
