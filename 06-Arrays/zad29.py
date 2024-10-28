myarray=[4,36,12,28,9,44,5]
secarray=[4,22,36,12,28,5]
unique=[]
for number in range(len(myarray)):
        if myarray[number] not in secarray:
            unique.append(myarray[number])

print(unique)