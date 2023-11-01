# Problem 2:
# Write a function that checks if a string is a palindrome. The function should be 
# case-insensitive and should ignore spaces and punctuation.

def palindrome(input_string):
    input_string = input_string.lower()    
    import re
    matcher = re.finditer("[a-z]",input_string)
    result = ""
    for i in matcher:
        result += i.group()
    if result == result[::-1]:
        return f"The given string ({input_string}) is palindrome"
    else:
        return f"The given string ({input_string}) is not a palindrome"

print(palindrome("su- ri = y'a"))
print(palindrome("A man, a plan, a canal, Panama"))
