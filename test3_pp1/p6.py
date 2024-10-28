def f(vname):
    import re
    if len(vname)>5:
        return False
    if re.match(r"^[A-Za-z_][A-Za-z0-9_]{0,4}$",vname):
        return True
    else:
        return False
    
print(f("abc"))
print(f("abcdef"))
print(f('8abc'))
print(f('_4x'))