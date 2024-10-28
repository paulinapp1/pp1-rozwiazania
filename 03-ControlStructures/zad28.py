number=input("Enter EAN-13 article number:")
if len(number)>13:
    print("Article number incorrect")
    if number[0]==5 and number[1]==9 and number[2]==0:
        print("Article manufactured in Poland")
else:
    print("Article number correct")
#if number[0]==5 and number[1]==9 and number[2]==0:
 #   print("Article manufactured in Poland")