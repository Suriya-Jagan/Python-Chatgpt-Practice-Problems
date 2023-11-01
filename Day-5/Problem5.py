# Problem 5:
# Create a function that takes a list of strings and returns a new list with 
# all the strings sorted in alphabetical order.

# x = "pasta"
# u = sorted(x)
# x = "".join(u)
# print(x)

def sorted_string_list(string_list):
    sorted_list = []
    for i in string_list:
        sorting = "".join(sorted(i.lower()))
        sorted_list.append(sorting)
    return sorted_list

string_list = ["suriya", "vijay", "wilson", "Shyam"]
print(sorted_string_list(string_list))
