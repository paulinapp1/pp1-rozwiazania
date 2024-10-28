height=float(input("Enter your height in cm: "))
weight=int(input("Enter your weight in kg: "))
bmi=weight/(height**2)
print("Your BMI index", bmi)
if bmi>=18.5 and bmi<=24.99:
    print("Correct weight: true")
else:
    print("Correct weight: false")