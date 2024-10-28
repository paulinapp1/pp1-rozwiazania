import re

def f(mnumbers):
    valid_count = 0
    for number in mnumbers:
        if re.match(r'^[+-]?[1-7a-dA-D]+$', number):
            valid_count += 1
    return valid_count

print(f(["A15", "-31", "7abC", "+D1", "-gH"]))
print(f(["A05", "-3+1", "7ab8C", "+D1", "-22k"]))







