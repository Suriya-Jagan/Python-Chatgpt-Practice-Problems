# Problem 4: Count Occurrences of a Word
# Create a function that takes a list of words and a word as input. 
# The function should return the number of times the given word appears in the list.

def Count_Occurrences(list_input, Words):
    count = 0
    for i in list_input:
        if i == Words:
            count += 1
    return f"The Word '{Words}' has been Occurred {count} times in a given list"

List1 = ["suriya", "vijay", "suriya", "wilson", "shyam", "suriya", "wilson", "suriya", "vijay"]
word = "suriya"
Counted_Occurrence = Count_Occurrences(List1, word)
print(Counted_Occurrence)
