# Problem5:
# Write a program that takes a list of strings and returns a new list with the strings 
# sorted by their length in descending order.

x = ["suriya", "vijay", "Moses clinton", "Shyam Kumar", "wilson"]
y = sorted(x,key=len,reverse=True)
print(y)
