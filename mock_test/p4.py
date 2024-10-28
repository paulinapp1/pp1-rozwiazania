def f(subjects):
    max_avg=0
    max_subject=""
    for subject,score in subjects.items():
        total=sum(score)
        avg=total/len(score)
        if avg>max_avg:
            max=max_avg
            max_subject=subject

    return max_subject

   

subjects={"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}
print(f(subjects))

