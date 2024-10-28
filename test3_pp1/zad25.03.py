def f(num_of_products,price):
    payment=0
    discount=price-(price*(25/100))
    if num_of_products<=2:
        payment=num_of_products*price
    else:
        payment=(2*price)+(num_of_products-2)*discount
    return payment

print(f(5,40))

