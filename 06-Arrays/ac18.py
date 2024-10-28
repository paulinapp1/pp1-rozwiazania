stringinput=input("Enter a list of numbers separeted by space")
user_list=stringinput.split()
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

given_num=int(input("Enter number"))
count=0
for i in user_list:
    if i==given_num:
        count+=1

print(count)