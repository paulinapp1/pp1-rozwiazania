binary=input("Enter binary: ")
if len(binary)>5:
    print("You've entered a wrong number")
first=int(binary[0])
second=int(binary[1])
third=int(binary[2])
fourth=int(binary[3])

print(((first*(2**3))+(second*(2**2))+(third*2)+(fourth*1)))

