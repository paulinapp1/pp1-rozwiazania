def f(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        return number1 % number2
    elif operator == '**':
        return number1 ** number2
    else:
        return "Invalid operator"

# Test cases
print(f(2, 3, "+"))   # Output will be 5
print(f(2, 3, "%"))   # Output will be 2
print(f(2, 3, "**"))  # Output will be 8
print(f(2, 3, "*"))   # Output will be 6
print(f(2, 3, "-"))   # Output will be -1
