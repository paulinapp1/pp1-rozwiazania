time=input("Enter time (24-hour format: )")
time2=int(time[:2])
j=0
if time2>=13 and time2<=24:
    for i in range(12,24):
        if time2==i:
            print(f"time in 12-hour format: {j}:{time[3:5]}")
        j=j+1
