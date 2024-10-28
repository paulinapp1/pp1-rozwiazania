name=input("Enter name: ")
length=len(name)
index=0
while index<=length:
    print(name[index], ord(name[index]))
    index=index+1