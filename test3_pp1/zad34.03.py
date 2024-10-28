def minimum_coins(amount):
    # Initialize the count of each coin denomination
    coins_5 = 0
    coins_2 = 0
    coins_1 = 0

    while amount >= 5:
        coins_5 += 1
        amount -= 5

    while amount >= 2:
        coins_2 += 1
        amount -= 2

    while amount >= 1:
        coins_1 += 1
        amount -= 1

    return coins_5, coins_2, coins_1

print(minimum_coins(18))