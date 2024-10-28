def f(name):
    import re
    if re.match(r'^[A-Za-z_][A-Za-z0-9_]{0,4}$', name):
        return True
    else:
        return False
    

print(f("8abc"))
