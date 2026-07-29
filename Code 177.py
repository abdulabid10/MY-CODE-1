def palindrome(text):
    return text == text[::-1]

text = input("Enter string: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
