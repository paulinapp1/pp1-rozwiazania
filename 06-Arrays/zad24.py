myarray=[15,8,31,47,2,19]
sum=0
for number in range(len(myarray)):
    sum+=myarray[number]

length=len(myarray)
mean=round(sum/length)
print(mean)