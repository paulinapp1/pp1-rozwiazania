def f(d):
    total_sum=0
    values=[]
    result=0
    for value in d.values():
        total_sum+=value
        values.append(value)
    avg=total_sum/len(values)
    for value in d.values():
        if value>avg:
            result+=1
    return result

print(f({"LO231":150,"BA787":120,"NZ15":30}) )
print(f({"LO231":150,"BA787":20,"NZ15":30}) )
    

