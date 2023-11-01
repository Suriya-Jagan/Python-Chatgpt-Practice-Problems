# Problem 2:
# Create a function that takes a list of numbers and returns the sum of all the odd numbers in the list.

def sum_odd(l):
    sum_of_odd = 0
    for i in l:
        if i % 2 !=0:
            sum_of_odd += i
    return sum_of_odd

list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sum_odd(list))
