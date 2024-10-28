import json

with open("studenci2.json") as file:
    students_data=json.load(file)
limited_students=[]
for student in students_data:
    limited_student={
        "name":student["name"],
        "surname":student["surname"],
        "student_id":student["student_id"]

    }
limited_students.append(limited_student)
with open("limited.json","w") as file2:
    json.dump(limited_students, file2)
