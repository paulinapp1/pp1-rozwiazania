def f(number,even):
    total_even=0
    total_uneven=0
    str_num=str(number)
    for digit in str_num:
        if int(digit)%2==0:
            total_even+=int(digit)
        else:
            total_uneven+=int(digit)
    if even==True:
        return total_even
    else:
        return total_uneven
    

print(f(3124,True) )
print(f(13115,True) )
