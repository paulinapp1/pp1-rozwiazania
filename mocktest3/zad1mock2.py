def f(n):
    str_n=str(n)
    max=0
    min=100000
    counter=0
    for digit in range(len(str_n)):
        if int(str_n[digit])%2!=0:
            counter+=1
            if int(str_n[digit])>max:
                max=int(str_n[digit])
    for digit in range(len(str_n)):
        if int(str_n[digit])%2!=0:
            counter+=1
            if int(str_n[digit])<min:
                min=int(str_n[digit])
    result=max-min
    if counter==0:
        return -1
    else:
     return result


print(f(10852))
print(f(7235973))
print(f(846206))


