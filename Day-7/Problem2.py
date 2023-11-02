# Problem 2: Reverse a List
# Create a function that takes a list and returns a new list with the elements reversed.
# Do not use the reverse() method.

def reverse_list(list1):
    list1 = list1[::-1]
    return list1

l = [10, "suriya", 20, 30, "SJ"]
print(reverse_list(l))
