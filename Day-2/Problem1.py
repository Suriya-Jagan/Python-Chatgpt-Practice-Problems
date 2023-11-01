# Problem1:
# Write a function that finds the largest and smallest elements in a list.

def find_largest_smallest(mylist):
    mylist = list(mylist)
    largest = smallest = mylist[0]
    for i in mylist:
        if i > largest:
            largest = i
        elif i < smallest:
            smallest = i
    return f"Largest number in given List is {largest} and the Smallest number in given List is {smallest}"
print(find_largest_smallest([10,20,30,40,60,5,4,55]))
