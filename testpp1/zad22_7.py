import re
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
sum=0
for temperature in temperatures:
    sum+=int(temperature)

avg=sum/len(temperatures)
print(avg)

