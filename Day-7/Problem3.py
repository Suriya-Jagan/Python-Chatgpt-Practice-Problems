# Problem 3: Find the Median
# Write a function that takes a list of numbers and returns the median (middle value) of the 
# numbers in the list. You can assume the list is already sorted.

def find_median(input_list):
    for i in input_list:
        if len(input_list) % 2 == 0:
            return input_list[int(((len(input_list))/2)-1)], input_list[int(((len(input_list))/2))]
        else:
            return input_list[int(((len(input_list))/2)-1)]

list1 = [10, 20, 30, 40, 50, 60, 70]
print(find_median(list1))
