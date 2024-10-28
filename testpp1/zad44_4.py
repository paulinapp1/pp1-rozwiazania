def f(password):
    unique=[]
    if len(password)<6:
        return False
    for letter in password:
        if letter not in unique:
            count=password.count(letter)
            if count==1:
                unique.append(letter)
    if len(unique)>=6:
        return True
    else:
        return False
    
print(f("qwerty"))
    