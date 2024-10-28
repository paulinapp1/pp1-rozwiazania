arr=[i for i in range(1,20)]
divisible=list(filter(lambda x: x%2==0 and x%3==0,arr))
for num in divisible:
    print(num)