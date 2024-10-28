arr1=[4,36,1,28,9,44,5] 
arr2=[5,1,36]
result=[]
for i in arr2:
    if i in arr1:
        result.append(i)

if len(result)==len(arr2):
    print("True")
else:
    print("False")
