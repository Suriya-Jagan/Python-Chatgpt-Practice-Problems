# Create a function that takes two lists and returns a new list containing elements
# that are common in both input lists.

def common_list(list1, list2):
    list1.extend(list2)
    commonlist = set(list1)
    commonlist = list(commonlist)
    return commonlist

l1 = [10, 20, 30, 40, 50, 60]
l2 = [40, 50, 60, 70, 80, 90]
print(common_list(l1, l2))