def f(dice):
    current_count=1
    max_count=0
    digit=None
    for number in range(len(dice)):
        if dice[number]==dice[number-1]:
            current_count+=1
        else:
            max_count=max(max_count,current_count)
            digit=dice[number-1]
            current_count=1
    
    if current_count>max_count:
        max_count=current_count
        digit=dice[-1]
    
    return digit
print(f("52331655544"))

