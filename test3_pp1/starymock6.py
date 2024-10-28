def f(years,course):
    import json
    
    with open("data.json", "r")as file:
        counter=0
        json_file=json.load(file)
        for student in json_file:
            age=0
            if student["age"]>=years:
                age=1
            for study_course in student["studies"]["courses"]:
                if study_course["name"]==course: 
                    avg=sum(study_course["grades"])/len(study_course["grades"])
                    if avg>=4:
                        if age==1:
                            counter+=1
    return counter



print(f(21,'statistics'))

