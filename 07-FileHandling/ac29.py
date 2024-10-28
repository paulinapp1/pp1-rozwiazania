def f(filename):
    with open(filename+".txt", 'r', encoding='utf-8') as file:
        lines=file.readlines()