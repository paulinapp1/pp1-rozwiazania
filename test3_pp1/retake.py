def f(product_code):
    sum=0
    for num in range(len(product_code)):
        if num<3:
            sum+=int(product_code[num])
    remainder=sum%7
    if product_code[-1]==str(remainder):
        return True
    else:
        return False
    
print(f("1114"))
    
