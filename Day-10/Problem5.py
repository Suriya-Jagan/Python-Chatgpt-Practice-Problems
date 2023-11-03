# Problem 5: Anagram Detection
# Write a function that takes two strings as input and checks if they are anagrams of each other. 
# Anagrams are words or phrases formed by rearranging the letters of another. 
# For example, "listen" and "silent" are anagrams.

def is_anagram(str1, str2):
    sort1 = sorted(str1)
    sorted_str1 = "".join(sort1)
    sort2 = sorted(str2)
    sorted_str2 = "".join(sort2)
    if sorted_str1 == sorted_str2:
        return f"The given strings '{str1}' and {str2} are 'Anagram'"
    else:
        return f"The given strings '{str1}' and {str2} are 'Not an Anagram'"

str1 = "race"
str2 = "acer"
print(is_anagram(str1, str2))
