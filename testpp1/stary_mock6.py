import json
def f(age,course,average):
    with open("data(2).json", "r")as file:
       content= json.loads(file)
    for key,value in content.items():
        if key["age"]>=age

