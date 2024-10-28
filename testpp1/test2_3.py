def f(cards):
    result=0
    important=['A','K','Q','J','T']
    for card in cards:
        if card in  important:
            result+=10
        else:
            result+=int(card)

    return result

print(f("234AJ7"))
