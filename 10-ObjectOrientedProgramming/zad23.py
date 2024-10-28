class C:
    def __init__(self, name, surname, age, seniority):
        self.name=name
        self.age=age
        self.seniority=seniority
        self.surname=surname
    def __str__(self):
        if self.age>=18:
          return  self.surname.upper()+self.name[0].upper()+str(self.seniority)
        else:
           return self.surname.lower()+self.name[0].lower()+str(self.seniority)


person1=C("Anna", "May",17,7)
person2=C("George", "Brown", 21,4)
print(person1)
print(person2)
          