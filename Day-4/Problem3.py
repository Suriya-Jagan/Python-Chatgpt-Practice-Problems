# Problem 3:
# Write a Python program to find the most frequent element in a list.

l = [10, 20, 30, 50, 50, 20, 30, 40, 20, 10, 50, 10, 50]
d = {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
most_frequent_element = max(d, key=d.get)
print(most_frequent_element)