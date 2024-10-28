myarray=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
max=""
for word in range(len(myarray)):
    if len(myarray[word])>len(max):
        max=myarray[word]

print(max)