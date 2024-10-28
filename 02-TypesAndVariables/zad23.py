import math
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
p=(a+b+c)/2
area=p*(p-a)*(p-b)*(p-c)
print("Triangle area: ",math.sqrt(area))
print("Triange circumference: ", a+b+c)
