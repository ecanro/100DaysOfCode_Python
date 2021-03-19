student_dict = {
    "students": ["Saed", "Noé", "José"],
    "score": [85, 84, 90]
}

# looping through dictionaries
for (key, value) in student_dict.items():
    print(value)

import pandas

students_data_frame = pandas.DataFrame(student_dict)
print(students_data_frame)
for(index, row) in students_data_frame.iterrows():
    print(index)
    print(row)
    #print(row.students)
    if row.students == "Saed":
        print(row.score)
