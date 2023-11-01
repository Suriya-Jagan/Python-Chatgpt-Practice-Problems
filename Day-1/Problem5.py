# Problem5:
# Create a function that takes a list and returns the unique elements in it.

def l(l1):
    unique = list(set(l1))
    return unique
list1 = [10,20,20,30,30]
print(l(list1))
