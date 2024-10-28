import random
def display_array(arr):
    print('-' * 48)
    print('|', end='')
    for num in arr:
        print(f'{num:^5}|', end='')
    print('\n' + '-' * 48)

array = [random.randint(1, 999) for _ in range(8)]
display_array(array)
