# Problem5:
# Write a Python program to merge two sorted lists into one sorted list.

l1 = [10,5,3,8,11,4]
l2 = [25,12,45,14,36,8]
l1 = sorted(l1)
l2 = sorted(l2)
l1.extend(l2)
l = sorted(l1)
print(l)
