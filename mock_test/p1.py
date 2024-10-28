def f(player1,player2):
    values = ["A","K","Q","J","T"]
    score1=0
    score2=0
    for card in range(len(player1)):
        if card in values:
            score1+=10
        else:
            score1+=int(card)
    for card2 in range(len(player2)):
        if card2 in values:
            score2+=10
        else:
            score2+=int(card)
    if score1>=score2:
        return True
    else:
        return False
    
print(f("9532", "K8"))




