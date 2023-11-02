# Problem3:
# Write a function that takes a list of words and returns the longest word from the list.

def longest_word(list_string):
    word = ""
    for i in list_string:
        if len(i) > len(word):
            word = i
    return word

list1 = ["suriya", "vijay", "wilson", "shyam kumar", "moses"]
print(longest_word(list1))
