# Problem 1: Reverse a Sentence
# Write a function that takes a sentence (a string) as input and returns the sentence with its words reversed. 
# For example, if the input is "Hello, world!", the output should be "olleH, dlrow!".

def words_reversed(input_str):
    list1 = input_str.split()
    list2 = []
    for i in list1:
        reversing = i[::-1]
        list2.append(reversing)
    merged = " ".join(list2)
    return merged

string1 = "A boy stands in the corner of the school"
print(words_reversed(string1))
