def to_binary(n):
    stack = []
    
    while n > 0:
        remainder = n % 2
        stack.append(remainder)
        n //= 2
    
    binary = ""
    while stack:
        binary += str(stack.pop())
    
    return binary

print(to_binary(18))