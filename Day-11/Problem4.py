# Problem 4: Palindrome Checker
# Create a function that checks whether a given word or phrase is a palindrome 
# (reads the same forwards and backward) and returns a boolean value.

def is_palindrome(input_string):
    input_string = input_string.lower()
    if input_string == input_string[::-1]:
        return True
    else:
        return False

string1 = "suriya"
string2 = "kayak"
print(is_palindrome(string1))
print(is_palindrome(string2))
