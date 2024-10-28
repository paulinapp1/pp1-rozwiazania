def f(player1,player2):
    play1=0
    play2=0
    important=['A','K','Q','J','T']
    for card in player1:
        if card in important:
            play1+=10
        else:
            play1+=int(card)
    for card in player2:
        if card in important:
            play2+=10
        else:
            play2+=int(card)
    if play1>play2:
        return True
    else:
        return False

print(f("9532","K8")  )
