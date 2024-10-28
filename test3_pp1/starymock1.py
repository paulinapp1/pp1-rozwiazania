def f(player1,player2):
    cards=["A","K","Q","J","T"]
    result1=0
    result2=0
    for card in player1:
        if card in cards:
            result1+=10
        else:
            result1+=int(card)
    for card in player2:
        if card in cards:
            result2+=10
        else:
            result2+=int(card)
    if result1>=result2:
        return True
    else:
        return False
    

print(f("AJ972","AQT72") )
print(f("9532","K8") )
    
