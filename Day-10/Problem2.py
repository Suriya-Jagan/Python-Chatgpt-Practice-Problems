# Problem 2: List Intersection
# Write a function that takes two lists as input and returns a new list containing elements
# that are common in both input lists.

def list_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    list_intersect = list(set1.intersection(set2))
    return list_intersect

l1 = [10, 20, 30, 40, 50, 60]
l2 = [40, 50, 60, 70, 80, 90]
print(list_intersection(l1,l2))
