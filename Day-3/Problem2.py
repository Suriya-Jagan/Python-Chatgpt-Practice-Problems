#Problem2:
# Create a function that takes a string as input and returns the reverse of the string 
# without using slicing or the reverse() method.

def rev_string(inputsring):
    l = len(inputsring)
    output = []
    for i in range(l-1,-1,-1):
        x = inputsring[i]
        output.append(x)
    
    rev = "".join(output)
    return rev
print(rev_string("Pasta"))


#Method2
def revstring(inputstring):
    rev = ""
    for i in inputstring:
        rev = i + rev
    return rev
print(revstring("Pastor"))
