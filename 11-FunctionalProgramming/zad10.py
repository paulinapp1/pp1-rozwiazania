def avg_speed(distance,hours,minutes):
    time=hours+(minutes/60)
    return distance/time
distance=int(input('Enter distance in km: '))
hours=int(input('Enter number of travel hours: '))
minutes=int(input('Enter number of travel minutes:  '))
avg=round(avg_speed(distance,hours,minutes),2)
print(f"Average speed: {avg} km/h")
