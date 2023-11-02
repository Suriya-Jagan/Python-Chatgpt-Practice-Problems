# Problem1:
# Write a function that takes a string as input and returns the string with all vowels removed.

def without_vowels(input_string):
    input_string = input_string.lower()
    string = ""
    vowels = "aeiou"
    for i in input_string:
        if i not in vowels:
            string += i
    return string

inputstring = "SurIya Jagannathan"
print(without_vowels(inputstring))
