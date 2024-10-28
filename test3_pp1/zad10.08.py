import json

with open("data.json") as file:
    data = json.load(file)

for item in data:
    for key, value in item.items():
        print(f'{key}:{value}')
