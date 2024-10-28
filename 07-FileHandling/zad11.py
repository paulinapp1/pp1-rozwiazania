file=open('numbers.txt', 'r')
lines=file.readlines()
sum=0
for line in lines:
    sum=sum+int(line)


print(sum)
file.close()