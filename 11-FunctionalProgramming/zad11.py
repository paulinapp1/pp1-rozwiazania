distance=int(input('Enter distance in km: '))
hours=int(input('Enter number of travel hours: '))
minutes=int(input('Enter number of travel minutes:  '))
time=hours+(minutes/60)
avg_speed= lambda x,y: x/y
result=round(avg_speed(distance,time),2)

print(f"Average speed: {result} km/h")