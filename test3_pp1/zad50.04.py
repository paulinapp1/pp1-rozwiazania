def f(n):
    fact = 1
    for i in range(1, n + 1):  # Start the range from 1 and include 'n' in the loop
        fact *= i
    return fact

print(f(5))  # Calculate the factorial of 5
