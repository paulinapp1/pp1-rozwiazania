def f(number):
    str_n=str(number)
    counter=0
    for num in str_n:
        if str_n.count(num)>1:
            counter+=str_n.count(num)
    return counter

print(f(1027))
print(f(230335))