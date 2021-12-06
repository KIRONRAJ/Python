strng = input("Enter a word to check for palindrome :")

if strng == strng[::-1]:
    print("The", strng, "is a Palindrome")
else:
    print("The", strng, "is not a Palindrome")
