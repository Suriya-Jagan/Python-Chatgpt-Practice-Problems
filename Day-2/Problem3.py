# Problem3:
# Write a function that removes duplicates from a list.

def remove_duplicates(mylist):
    mylist = set(mylist)
    return mylist
list1 = [100,25,45,66,78,66,100,25]
print(remove_duplicates(list1))
