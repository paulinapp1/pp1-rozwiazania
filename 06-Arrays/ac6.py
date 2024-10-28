arr=[15,8,31,47,2,19]
sum=0
array=""
for i in arr:
    sum=sum+int(i)
    array=array+str(i)+' '

mean=sum//len(arr)
print("array", array)
print("arthimetic mean: ", mean)