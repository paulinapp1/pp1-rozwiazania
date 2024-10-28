score=float(input("Enter score: "))
if score<0.0 and score>1.0:
    print("You've entered a wrong score")

if score>=0.9:
    print("A")
if score>=0.8 and score<0.9:
    print("B")
if score>=0.7 and score<0.8:
    print("C")
if score>=0.6 and score<0.7:
    print("D")
if score<0.6:
    print("F")




