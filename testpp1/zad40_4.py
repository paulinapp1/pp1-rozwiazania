def f(number):
    str_number=str(number)
    visited=[]
    total=0
    for num in str_number:
        if num not in visited:
            count=str_number.count(num)
            if count>1:
                total+=int(num)*count
                visited.append(num)
    return total

print(f(1027))
