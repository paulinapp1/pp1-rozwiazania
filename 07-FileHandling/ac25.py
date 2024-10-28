import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
temperatures=[int(temp) for temp in temperatures]

average=sum(temperatures)/len(temperatures)
print(average)
