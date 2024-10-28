def f(previous_price, current_price):
    step1=previous_price-current_price
    step2=(step1/previous_price)*100
    if step2>=10:
        return True
    else:
        return False
    
print(f(140,140))
