# Problem 1: Calculate the Sum of Digits
# Write a function that takes an integer as input and returns the sum of its digits.

def sum_of_digits(n):
    sum = 0
    str1 = str(n)
    length = len(str1)
    for i in range(length):
        sum += int(str1[i])
    return sum
print(sum_of_digits(5165))
