decimal=int(input("Enter a decimal number: "))
dec2=decimal
binary=""
while decimal>0:
    remainder=decimal%2
    binary=str(remainder)+binary
    decimal=decimal//2

print(f'{dec2}(10)={binary}(2)')