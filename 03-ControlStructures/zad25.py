number=int(input("Number of products purchased: "))
price=int(input("Product price"))
if(number>=2):
    amount=(number-2)
    precentage=(amount*price)*0.25
    payment=(2*price)+(amount*price)-precentage
    print("Amount to pay:", payment)
