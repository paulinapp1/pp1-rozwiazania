def f(card_number):
    result=""
    for number in range(len(card_number)):
        if number==0 or number==1:
            result+=card_number[number]
        elif number>1 and number<=11:
            result+="*"
        else:
            result+=card_number[number]
    return result

print(f("5290312400019022") )
