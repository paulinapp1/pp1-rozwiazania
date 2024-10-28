def f(x, y, digit):
    counter = 0
    for i in range(x, y + 1):
        number = str(i)  # Convert the number to a string to check each digit
        counter += number.count(str(digit))  # Count occurrences of the digit in the number string
    return counter

print(f(10,15,1))
        