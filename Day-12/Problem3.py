# Problem 3: Sort Dictionary by Values
# Write a function that takes a dictionary and returns a new dictionary with the same keys 
# but sorted by their values in ascending order.


def sort_dict(dict):
    y = sorted(dict.items(),key= lambda x:x[1])
    return y

x = {"5":5, "6":6, "2":2, "1":1, "4":4, "3":3}
print(sort_dict(x))
