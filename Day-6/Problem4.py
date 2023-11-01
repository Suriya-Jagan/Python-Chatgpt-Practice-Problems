# Problem 4:
# Create a function that takes a list of strings and returns a new list with the strings 
# sorted by their length in ascending order.

def sort_string_by_lenght(string):
    sorted_strings = sorted(string, key=len)
    return sorted_strings

str1 = ["apple", "banana", "Cherry", "data", "fig"]
print(sort_string_by_lenght(str1))
