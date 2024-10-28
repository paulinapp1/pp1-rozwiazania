def computegrade(score):
   if score>=0.9:
    grade="A"
   if score>=0.8 and score<0.9:
    grade="B"
   if score>=0.7 and score<0.8:
    grade="C"
   if score>=0.6 and score<0.7:
    grade="D"
   if score<0.6:
    grade="F"
   return grade


score=input("Enter score: ")
try:
    score = float(score)  
    if score < 0.0 or score > 1.0:  
        print("Score should be between 0.0 and 1.0")
    else:
        print(computegrade(score))
except ValueError:
    print("Wrong value")