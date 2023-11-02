# Problem4:
# Create a function that takes a list of strings and returns a new list 
# containing only the strings with more than 5 characters.

def more_than_5_char(list_string):
    string_0f_5 = []
    for i in list_string:
        if len(i) > 5:
            string_0f_5.append(i)
    return string_0f_5

list_of_string = ["Suriya", "Vijay", "Shyam Kumar", "Wilson", "Moses", "Yuvan", "Dhanush"]
print(more_than_5_char(list_of_string))
