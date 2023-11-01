# Problem2:
# Write a function that checks if a given string is a palindrome.

def Palindrome(n):
    n = n.lower()
    if n == n[::-1]:
        return "Given string is palindrome"
    else:
        return "Given string is not a palindrome"

print(Palindrome("Madam"))
