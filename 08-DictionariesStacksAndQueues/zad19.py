import json
with open("studenci2.json",'r', encoding='utf-8')as file:
    students_data=json.load(file)
limited_students=[]
for student in students_data:
    limited_student={
        "first name": student["name"],
        "last name": student["surname"],
        "student_id": student["student_id"]
    }
    limited_students.append(limited_student)
    with open("limited.json", 'w') as file:
     json.dump(limited_students, file, indent=4)