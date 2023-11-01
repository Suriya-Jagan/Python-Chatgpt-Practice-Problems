# Problem1:
# Write a Python program to find the factorial of a number.

n = int(input("Enter a number for Factorial: "))
x = 1
for i in range(1,n+1):
    x *=i
print(x)
