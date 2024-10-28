def f(x,y):
    nums=[]
    for i in range(x,y):
        if i%2==0 and i%3==0 and i%4!=0:
            nums.append(i)
    return sum(nums)


print(f(1,20))
