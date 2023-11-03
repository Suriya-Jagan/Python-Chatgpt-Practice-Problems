# Problem 3: Calculate Factorial
# Write a function to calculate the factorial of a given number. The factorial of a non-negative integer n, 
# denoted by n!, is the product of all positive integers less than or equal to n. 
# For example, 5! = 5 x 4 x 3 x 2 x 1 = 120.

def factorial(n):
    num = 1
    fact = 1
    while num <= n:
        fact *= num
        num += 1
    return fact

print(factorial(6))
