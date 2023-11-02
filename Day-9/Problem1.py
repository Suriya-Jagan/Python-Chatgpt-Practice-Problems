# Problem1: 
# Write a program that takes a list of numbers and returns the sum of all the odd numbers in the list.

l = [10, 15, 25, 16, 27, 28, 36, 11]
sum_of_odd = 0
for i in l:
    if i % 2 != 0:
        sum_of_odd += i
print(sum_of_odd)
