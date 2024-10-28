cprice=int(input("Current product price: "))
pprice=price=int(input("Previous product price: "))
procent=1.00-(cprice/pprice)
procent2=int(procent*100)
if procent2>=10:
    print("Buy the product!")
    print(f"Product price reduced by: {procent2}%")
