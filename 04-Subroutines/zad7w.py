bmi=lambda height, weight: weight/(height**2)
h=float(input("Enter height: "))
w=int(input("Enter weight: "))
h2=h/100
print(int(bmi(h2,w)))