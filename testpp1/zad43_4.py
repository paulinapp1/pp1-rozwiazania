def f(name):
    result=""
    splitstr=name.split()
    for name in splitstr:
        result+=name[0]
    return result

print(f("Internet of Things") )

