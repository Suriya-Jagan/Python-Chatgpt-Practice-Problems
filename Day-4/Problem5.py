# Write a function that takes a list of strings and returns a dictionary where the 
# keys are the strings, and the values are the lengths of the strings.

def dict_string_len(l):
    x = {i :len(i) for i in l}
    return x

print(dict_string_len(["suriya", "Vijay", "Abhishek", "Wilson Akash"]))


def dict_string_len(l):
    d = {}
    for i in l:
        d[i] = len(i)
    return d

print(dict_string_len(["suriya", "Vijay", "Abhishek", "Wilson Akash"]))
