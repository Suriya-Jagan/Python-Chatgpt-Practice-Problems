# Problem 1:
# Create a function that takes a string as input and returns the number of words in the string.

def find_len_of_string(input_string):
    words = input_string.split()
    return len(words)
input_string = input("Enter the string: ")
x = find_len_of_string(input_string)
print(x)
