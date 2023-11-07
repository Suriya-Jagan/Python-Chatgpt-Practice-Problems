# Problem 2: Merge Dictionaries
# Create a function that takes two dictionaries as input and merges them into a new dictionary. 
# If there are common keys, add their values together.

def merge_dict(x, y):
    d = {}
    for i, j in x.items():
        d[i] = j
    for i, j in y.items():
        if i in d:
            d[i] += j
        else:
            d[i] = j
    return d

x = {"s":5, "u": 6, "r":3, "i":8}
y = {"u":2, "m":5, "i": 6}
print(merge_dict(x,y))
