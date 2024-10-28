def f(d):
    parked=[]
    left=[]
    for car, status in d:
        if status=="in":
            parked.append(car)
        elif status=="out":
            parked.remove(car)
    parked.sort()
    return parked

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))