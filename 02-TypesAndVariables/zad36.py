buys=float(input("Enter the buying price: "))
sells=float(input("Enter the selling price: "))
print("Bank buys EUR: ", round(buys,4))
print("Bank sells EUR: ", round(sells,4))
spread=sells-buys
print("Spread",round(spread,4))
