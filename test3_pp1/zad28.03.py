def f(n):
    str_num=str(n)
    is_correct=False
    is_frompol=False
    if len(str_num)==13:
        is_correct=True
    if str_num[0:3]=="590":
        is_frompol=True
    return is_frompol, is_correct

print(f(5911230094938))


