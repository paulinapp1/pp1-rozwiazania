def f(text):
    result=""
    for letter in range(len(text)):
        if letter!=len(text)-1:
            result+=text[letter]+"-"
        else:
            result+=text[letter]
    return result

print(f("UEK"))
