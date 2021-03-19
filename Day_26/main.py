# List Comprehension
# normally we used a for loop fro iterated a list
import random

numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)

# with list comprehension work with Python sequences->string, list, range or tuple (in dict work too)
new_list = [n + 1 for n in numbers]

name = "Edgar"
new_name = [letter for letter in name ]

new_range = [n+1 for n in range(1, 5)]
new_range = [n*2 for n in range(1, 5)]


# Conditional list comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Nelson", "Edgar", "Wilmer", "Deysy"]
new_names = [name for name in names if len(name) < 6]
new_names = [name.upper() for name in names if len(name) >= 6]

# dict comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
students_score = {student:random.randint(20, 100) for student in names}
#->{'Alex': 42, 'Nelson': 52, 'Edgar': 45, 'Wilmer': 70, 'Deysy': 71}

# conditional dict comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_students)