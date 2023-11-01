# Problem 3:
# Write a program that counts the number of vowels in a given string.

input_string = input("Enter the string: ").lower()
vowels = ["a", "e", "i", "o", "u"]
count = 0
for i in input_string:
    if i in vowels:
        count += 1
    else:
        pass
print(f"The Number of Vowels in a string: {count}")
