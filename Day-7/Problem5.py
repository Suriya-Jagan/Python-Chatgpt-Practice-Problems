# Problem 5: Remove Duplicates from a String
# Write a function that takes a string as input and returns a new string with 
# duplicate characters removed while preserving the original order.

def remove_duplicate_string(string_input):
    string_input = string_input.lower()
    l =[]
    for i in string_input:
        if i not in l:
            l.append(i)
    removed_duplicate_string = "".join(l)
    return removed_duplicate_string

string_input = "SuriyaJagannajthan"
print(remove_duplicate_string(string_input))
