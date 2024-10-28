person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
print("A: ")
print(person)
print("B: ")
print(person["name"])
print("C: ")
print(person["hobby"][1])
person["surname"]="Nowak"

person["married"]=not person["married"]

person["gender"]="Male"

person["hobby"]=person["hobby"] +["bicycle"]

person["phone"]["work"] = "313131444"

print("Updated dictionary")
print(person)

#odczytaj słownik -stworz nowy slownik ktory bedzie zawieral elementy alfabetycznie