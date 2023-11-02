# Problem 1: Count Even Numbers in a List
# Write a function that takes a list of numbers and returns the count of even numbers in the list.

def count_even_numbers(input_list):
    count = 0
    for i in input_list:
        if i % 2 == 0:
            count += 1
    return f"The Count of even number in a list is {count}"

list1 = [10, 15, 25, 55, 60, 40, 32, 8, 41]
print(count_even_numbers(list1))
