# Problem 4: Count Characters
# Create a function that takes a string and a character as input and counts the number of times
# the character appears in the string.

def count_char(string, char):
    count = string.count(char)
    return f"The '{char}' character is appeared {count} times in the string"

str1 = "You cannot end a sentence with because because because is a conjunction"
print(count_char(str1, "because"))
