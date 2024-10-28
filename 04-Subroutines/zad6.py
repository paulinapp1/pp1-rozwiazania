def compute_pay(hours,rate):
    if hours >= 40:
        pay = hours * (1.5 * rate)
    else:
        pay = hours * rate
    return pay

hours=int(input("Enter hours: "))
rate=float(input("Enter rate: "))
print(compute_pay(hours, rate))