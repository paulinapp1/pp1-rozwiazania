stringinput=input("Enter a list of numbers separeted by space")
user_list=stringinput.split()
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
even=[]
odd=[]
for i in user_list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

final=even+odd

print(final)
