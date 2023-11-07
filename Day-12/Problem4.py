# Problem 4: Find Common Elements in Dictionaries
# Create a function that takes two dictionaries as input and returns a new dictionary containing 
# key-value pairs that are common to both input dictionaries.

def common_dict(d1, d2):
    common_d = {}
    for i, j in d1.items():
        if i in d2.keys():
            common_d[i] = j
    for i, j in d2.items():
        if i in common_d.keys():
            common_d[i] = j
    return common_d

d1 = {"a":20, "b":30, "c":40, "d":50}
d2 = {"c":40, "d":60, "e":50, "f":70}
print(common_dict(d1, d2))

