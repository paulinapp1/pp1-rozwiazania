data=[("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
 ("Jackson","Peter"),("Johnson","Rick"),
 ("Lewis","Terry"),("Clarke","Robin")]
for last_name, first_name in data:
    new_name=last_name.upper()
    print(f"{new_name}, {first_name}")