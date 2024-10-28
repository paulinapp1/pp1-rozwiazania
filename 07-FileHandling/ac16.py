def f(file):
    filename=file
    counter=0
    with open(file+'.txt') as files:
        lines=files.readlines()
        for line in lines:
            counter+=1

    return counter, filename

print(f("movies"))