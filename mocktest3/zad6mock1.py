import re

def f(vname):
    pattern = r"^[A-Za-z_][A-Za-z0-9_]{0,4}$"
    return bool(re.match(pattern, vname))

print(f("abcdef"))
print(f("Abc"))
print(f("_abc1"))
print(f("12345"))
print(f("a_123"))
print(f("a_1Bc"))
