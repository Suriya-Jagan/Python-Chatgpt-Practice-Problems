#Problem2:
# Create a function that takes a list of numbers and returns the list sorted in descending order.
def dec_order(list1):
    list1 = sorted(list1,reverse=True)
    return list1

lists = [10, 30, 40, 20, 10, 5, 50, 15]
print(dec_order(lists))