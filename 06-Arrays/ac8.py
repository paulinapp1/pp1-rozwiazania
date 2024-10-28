def star(n):
    result=""
    for i in range(n):
        result=result+"*"
    return result

arr=[12,6,4,9,10]
for i in arr:
    print(f"{i} : {star(i)}")
