# Problem 1:
# Write a function that takes a list of words and returns a new list 
# containing only the words with 4 or more letters.

def more_than_4_words(l):
    l1 = []
    for i in l:
        if len(i)>=4:
            l1.append(i)
        else:
            pass
    return l1
list_input= ["under taker", "kil", "wils", "suriya", "joe"]
print(more_than_4_words(list_input))
