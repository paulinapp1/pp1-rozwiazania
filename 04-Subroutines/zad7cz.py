def different(n1,n2,n3):
    if n1==n2 and n1==n3 and n2==n3:
        return True
    else:
        return False
    
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if different(num1,num2,num3)==False:
    print(f"Numbers {num1}, {num2}, {num3} are different")