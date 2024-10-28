with open("number4.txt", 'w')as file:
    for i in range(1,11):
        second=i**2
        third=i**3
        file.write(f"{i},{second},{third}\n")
    