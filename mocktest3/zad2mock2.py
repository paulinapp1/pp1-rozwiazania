def f(x, y, d):
    for num in range(x, y + 1):
        if d in str(num):
            return True
    return False



print(f(100,120,"11"))