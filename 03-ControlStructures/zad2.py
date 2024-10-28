hours=input("Enter hours: ")
rate=input("Enter rate: ")
try:
    hours2=int(hours)
    rate2=float(rate)
except:
    print("Enter numerical value")
    
if hours2>=40:
    print("Pay: ",hours2*(1.5*rate2))
else:
    print("Pay: ", hours2*rate2)

