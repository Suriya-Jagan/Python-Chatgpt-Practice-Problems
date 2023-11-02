# Problem3:
# Write a function that takes a string as input and returns the reverse of the string 
# without using slicing or the reverse() method.

def reversed_string(str1):
    reverse = ""
    for i in str1:
        reverse = i + reverse
    return reverse
string1 = "Bala Krishnan"
print(reversed_string(string1))
