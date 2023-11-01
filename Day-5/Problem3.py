#Problem3:
#Create a function that takes a list of numbers and returns the product of all the numbers in the list.

def Product_of_list(input_list):
    product = 1
    for i in input_list:
        product *= i
    return f"The Product of the given list is {product}"

l1 = [1, 2, 3, 4, 5, 6]
print(Product_of_list(l1))
