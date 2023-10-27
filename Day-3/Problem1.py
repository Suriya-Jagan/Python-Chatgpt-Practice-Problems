# Problem 1:
# Write a function that takes a list of numbers and returns the sum of all the even numbers in the list.
def sumevenno(l):
    l1 = l.split(",")
    l2 = []
    sumeven = 0
    for i in l1:
        l3 = int(i)
        l2.append(l3)
    
    for i in l2:
        if i % 2 == 0:
            sumeven += i
        else:
            pass
    return sumeven

x = sumevenno("10,25,30,37,42,50,59,64")
print(x)

#Method 2:
def sum_even_no(input_string):
    numbers = input_string.split(",")
    even_numbers = [int(i) for i in numbers if int(i) % 2 ==0]
    return sum(even_numbers)
x = sum_even_no("10,25,30,37,42,50,59,64")
print(x)