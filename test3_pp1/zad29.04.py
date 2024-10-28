def f(amount_to_pay):
    coins = [5, 2, 1]  # Available coin denominations
    total_coins = 0

    for coin in coins:
        # Count how many coins of each denomination can be used
        count = amount_to_pay // coin
        total_coins += count
        amount_to_pay -= count * coin

    return total_coins

# Test cases
print(f(23))  # Output will be 6
print(f(8))   # Output will be 3
print(f(2))   # Output will be 1
print(f(0))   # Output will be 0
