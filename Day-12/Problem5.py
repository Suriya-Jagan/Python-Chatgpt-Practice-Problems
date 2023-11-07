# Problem 5: Word Frequency in a Sentence
# Write a function that takes a sentence as input and returns a dictionary where the keys are unique words, 
# and the values are the frequencies of those words in the sentence.

def word_freq(sentence):
    d ={}
    y = x.lower().split()
    for i in y:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

x = "suriya has suriya has vijay ajith tammanna has tammanna suriya"
print(word_freq(x))
