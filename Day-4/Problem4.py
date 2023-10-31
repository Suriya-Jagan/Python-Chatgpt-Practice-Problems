# Problem 4:
# Create a dictionary with student names as keys and their corresponding scores as values. 
# Write a program that finds the student with the highest score.

d = {"Suriya": 66, "Vijay":96, "Arnold": 99, "Anand": 99, "Mukes": 70}
highest_score = max(d.values())
print(highest_score)
best_students = [std for std, score in d.items() if score == highest_score]

if len(best_students) == 1:
    print(f"The student with the highest score is {best_students[0]} with a score of {highest_score}")
else:
    print(f"The students with the highest score are {', '.join(best_students)} with the score of {highest_score}")
