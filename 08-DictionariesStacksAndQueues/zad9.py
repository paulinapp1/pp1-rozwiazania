countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 67000000},
    {"name": "Japan", "population": 126500000},
    {"name": "Brazil", "population": 213500000}
]

print("COUNTRY\tPOPULATION")
index = 0
while index < len(countries):
    country = countries[index]
    print(f"{country['name']}\t{country['population']}") #\t to jest tabulacja
    index += 1
