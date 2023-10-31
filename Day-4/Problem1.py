#Problem1:
# Write a Python function to count the number of occurrences of each element in a list
# and return the result as a dictionary.
l1 = [10, 20, 30, 30, 40, 50, 10, 20, 30, 50, 60, 10, 40, 30]
d = {}
for i in l1:
    d[i] = l1.count(i)
print(d)
