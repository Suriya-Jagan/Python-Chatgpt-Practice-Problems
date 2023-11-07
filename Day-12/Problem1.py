# Problem 1: Count Character Frequency
# Write a function that takes a string as input and returns a dictionary where the keys are characters, 
# and the values are the frequencies of those characters in the string.

def count_freq(string):
    d = {}
    for i in string:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

str = "wilsonakashsuriya"
print(count_freq(str))
