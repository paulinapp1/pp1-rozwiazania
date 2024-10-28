def f(c):
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    sorted_cards = []

    for card in c:
        for index in range(len(cards)):
            if card == cards[index]:
                sorted_cards.append(index)
    
    sorted_cards.sort()
    sorted_string = ""
    
    for card in range(len(sorted_cards)):
        sorted_string += cards[sorted_cards[card]]

    return sorted_string




print(f("AJQ41"))
