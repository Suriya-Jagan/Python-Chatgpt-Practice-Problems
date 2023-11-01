# Problem4:
# Create a function that finds the intersection of two lists.

def find_intersection(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    return s1.intersection(s2)
list1 = [10, 20, 50, 60, 25, 55, 40]
list2 = [20, 25, 35, 45, 75, 15, 50]
print(find_intersection(list1, list2))
