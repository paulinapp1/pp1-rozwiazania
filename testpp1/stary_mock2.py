def f(human_age):
    dogyear=0
    if human_age==1:
        dogyear=10
    if human_age==2:
        dogyear=20
    if human_age>2:
        for year in range(human_age-1):
            dogyear=20+4*year
    return dogyear

print(f(15))

