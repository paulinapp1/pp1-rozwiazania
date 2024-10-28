licznik=0
sum=0
while True:
        number=int(input("Enter number: "))
        if number==0:
            break
        licznik=licznik+1
        sum=sum+number
    
mean=sum/licznik
print(f"Quantity={licznik}, Sum={sum}, Mean={mean}")
        