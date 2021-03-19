## Average Height
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_heights = 0
number_of_students = 0
print(student_heights)
for height in student_heights:
    total_heights += height
    number_of_students += 1
    print(total_heights)

print(number_of_students)
height = round(total_heights / number_of_students)
print(height)

# functional solution
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)