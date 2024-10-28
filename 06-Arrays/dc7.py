myarray=[[2,5,4],[9,0,3]]

print(myarray)
print(len(myarray))
print(len(myarray[0]))
print(myarray[1][1])
second_row = myarray[1]
for element in second_row:
    print(element, end=" ")
print()
for row in myarray:
    for element in row:
        print(element, end=" ")
    print()

for row in myarray:
    print(row[-1])

