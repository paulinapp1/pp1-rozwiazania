def f(arr):
    big=""
    size=0
    for name in arr:
        if len(name)>size:
            big=name
            size=len(name)
    return big

print(f(["Genowefa", "Onufry", "Celestyna", "Alozjy", "Pankracy"]))