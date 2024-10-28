import random
dice_1= random.randint(1,6)
guess=int(input("Your lucky guess: "))
if dice_1==guess:
    print("Congratulations :)")
else:
    print("Better luck next time :()")

print(dice_1)