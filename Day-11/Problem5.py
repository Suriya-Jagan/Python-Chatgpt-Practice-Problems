# Problem 5: Calculate Factorial (Using Recursion)
# Write a Python function to calculate the factorial of a given number using recursion.

def factorial(n):
    # Base case
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120
