results=[37,51,44,23,78,92,39,84,83,51]
def min_pts(limit):
    return lambda pts: pts>=limit
a=70
b=40
c=30
resulta=list(filter(min_pts(a), results))
print(f"Min {a} pts: {resulta}")
resultb=list(filter(min_pts(b), results))
print(f"Min {b} pts: {resultb}")
resultc=list(filter(min_pts(c), results))
print(f"Min {c} pts: {resultc}")