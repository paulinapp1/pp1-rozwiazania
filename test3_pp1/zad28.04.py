def f(binary_number):
    for digit in binary_number:
        if digit != '0' and digit != '1':
            return False
    return True

print(f("100a10"))