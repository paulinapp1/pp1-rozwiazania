def star(n):
    result=""
    for i in range(n):
        result+="*"
    return result

myarray=[12,6,4,9,10]
for number in range(len(myarray)):
    print(f"{myarray[number]}: {star(myarray[number])}")
    
