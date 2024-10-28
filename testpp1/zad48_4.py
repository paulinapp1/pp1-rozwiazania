def f(product_code):
    total=0
    for i in range(3):
        total=total+int(product_code[i])
    four= total%7
    if product_code[3]==str(four):
        return True
    else:
        return False

print(f("1082") )   
    