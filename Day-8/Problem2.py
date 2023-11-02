# Problem2:
# Create a function that takes a string as input and counts the number of words in the string. 
# You can assume that words are separated by spaces.

def Count_words(word_string):
    list = word_string.split()
    count = 0
    for i in list:
        count += 1
    return count

string = "Suriya have the confidence to land in a high paid data analyst or data scientist job"
print(Count_words(string))
