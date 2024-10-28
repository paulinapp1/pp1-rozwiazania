with open("zad23.txt", "w")as file:
        for number in range(1,10):
            second=number**2
            third=number**3
            file.write(f"{number}, {second}, {third}"+"\n")


