import re
def f(t):
    total=0
    expression=r'\d+'
    numbers=re.findall(expression,t)
    for number in numbers:
        if int(number)>0:
            total+=int(number)
    return total
    

print(f("water12, and 3play is not 8"))
