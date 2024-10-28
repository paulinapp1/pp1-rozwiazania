hours=int(input("Enter hours: "))
rate=float(input("Enter rate: "))
if hours>=40:
    print("Pay: ",hours*(1.5*rate))
else:
    print("Pay: ", hours*rate)



