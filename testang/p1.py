def f(n):
    odds=[]
    str_n=str(n)
    for digit in str_n:
        if int(digit)%2!=0:
            odds.append(int(digit))
    return max(odds)-min(odds)



print(type(f(10852)))