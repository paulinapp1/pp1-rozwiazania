import json
student_data = {
    "name": "Alice",
    "age": 20,
    "gender": "female",
    "is_international": False,
    "subjects": ["Mathematics", "Computer Science", "History"],
    "email": "alice@example.com",
     "address": "123 Main St"

}


with open("student.json", "w") as file:
    json.dump(student_data, file, indent=6)
