import random
with open("numbers3.txt", 'w') as file:
        for _ in range(1,51):
            random_number = random.randint(100, 999)
            file.write(str(random_number) + '\n')
