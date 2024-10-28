name1=input("Enter first person name: ")
age1=int(input("Enter first person age: "))
name2=input("Enter second person name: ")
age2=int(input("Enter second person age: "))
if age1>=18 and age2>=18:
    print(f'{name1} and {name2} is an adult')
elif age1>=18 and age2<18:
     print(f'{name1} is an adult and {name2} is not an adult')
elif age2>=18 and age1<18:
      print(f'{name2} is an adult and {name1} is not an adult')
else:
      print(f'{name1} and {name2} are not adults')
    
      
  