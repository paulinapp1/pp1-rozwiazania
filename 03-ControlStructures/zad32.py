question1=input("Are you interested in computer science? Y/N ")
question2=input("Do you like playing video games? Y/N ")
question3=input("Do you have an instagram account? Y/N ")
if question1=='Y':
    question1_1=True
    question1_1="Yes"
else:
    question1_1=False
    question1_1="No"

if question2=='Y':
    question2_2=True
    question2_2="Yes"
else:
    question2_2=False
    question2_2="No"

if question3=="Y":
    question3_3=True
    question3_3="Yes"
else:
    question3_3=False
    question3_3="No"

print(f"Interested in computer science: {question1_1} ")
print(f"Playing computer games: {question2_2}")
print(f"Has an Instagram account: {question3_3}")
