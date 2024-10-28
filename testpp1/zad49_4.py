def f(dice):
    max_count = 0  # Variable to store the maximum consecutive count
    current_count = 1  # Initialize the count for the first digit
    max_digit = None  # Variable to store the digit with the maximum consecutive count
    
    # Iterate through the sequence starting from the second digit
    for i in range(1, len(dice)):
        # Check if the current digit is the same as the previous one
        if dice[i] == dice[i - 1]:
            current_count += 1  # Increment the consecutive count if it's the same digit
        else:
            # If the count for the current digit is greater than the maximum count so far
            if current_count > max_count:
                max_count = current_count  # Update the maximum count
                max_digit = dice[i - 1]  # Update the digit with the maximum count
            current_count = 1  # Reset the count for a new digit
        
    # Check for the count of the last digit sequence
    if current_count > max_count:
        max_count = current_count
        max_digit = dice[-1]
    
    return int(max_digit)

print(f("5233165554211111"))

        
        
            
