# Problem4:
# Create a function that takes a list of numbers and returns the average of the numbers.

def avg_num(l):
    sum = 0
    for i in l:
        sum += i
    avg = sum / (len(l))
    return avg

list1 = [10, 20, 30, 40, 50, 60]
print(avg_num(list1))
