# Problem5:
# Write a function that takes a string as input and returns a new string 
# with each word reversed while preserving the order of the words.

def reverse_words(list_of_words):
    list_of_words = list_of_words.split()
    l = []
    for i in list_of_words:
        reversed = i[::-1]
        l.append(reversed)
    reversed_words = " ".join(l)
    return reversed_words

string_input = "I had a lots of friends in my school"
print(reverse_words(string_input))
