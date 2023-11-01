# Problem2:
# Create a Python program to find the sum of all even numbers in a list.

mylist = list(input("Enter the list with space: ").split())
mylist = list((int(i) for i in mylist))
sum = 0
for i in mylist:
    if i%2==0:
        sum +=i 
print(sum)
