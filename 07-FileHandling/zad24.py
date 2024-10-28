import csv
with open("studentslist.txt", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            age = int(row['age'])
            if age < 30:
                print(f"{row['first_name']:8}{row['last_name']:8}{row['email']}")