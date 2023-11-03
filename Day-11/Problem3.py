# Problem 3: Swap Values
# Write a Python function to swap the values of two variables.

def swap_variables(a, b):
    temp = a
    a = b
    b = temp
    return a, b

x = 10
y = 20
x, y = swap_variables(x, y)
print("x = ", x)
print("y = ", y)
