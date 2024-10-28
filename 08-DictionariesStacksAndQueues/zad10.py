import json

with open("data.json") as file:
    data = json.load(file)
n=0
while n<len(data):
 row=data[n]
 for key,value in row.items():
   print(f"{key} : {value}")
 n+=1


 #country = countries[index]
  #  print(f"{country['name']}\t{country['population']}")