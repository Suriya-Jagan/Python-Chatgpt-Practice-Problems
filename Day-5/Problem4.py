# Problem 4:
# Write a Python program to remove duplicates from a list while preserving the order of the remaining elements.

l = [10, 20, 20, 30, 40, 40, 50, 10, 60]
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        pass
print(l1)
