def f(password):
    unique=[]
    if len(password)<6:
        return False
    for letter in password:
        if password.count(letter)==1:
            unique.append(letter)
    if len(unique)>=6:
        return True
    else:
        return False
print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f(""))
