def decimal_to_binary(decimal):
    binary = []
    
    # Iterate until the decimal number becomes 0
    while decimal > 0:
        remainder = decimal % 2  # Get the remainder when divided by 2
        binary.append(str(remainder))  # Store the remainder
        decimal //= 2  # Update the decimal by integer division
        
    # If the input was 0, return '0' as binary
    if not binary:
        return '0'
    
    # Reverse the list and join the remainders to get the binary equivalent
    binary.reverse()
    return ''.join(binary)

# Get input from the user

print(decimal_to_binary(12))

