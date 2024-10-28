#number=int(input("Enter number: "))

#for i in range(2, int(number**0.5)+1):
 #       if number%i is not 0:
  #      print(i, end=" ")
number = int(input("Enter number: "))
pomoc=False
for i in range(3, int(number**0.5) + 1):
    if number % i == 0:
        pomoc=True
    else:
        print(i)


        
