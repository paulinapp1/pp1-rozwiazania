#Hasło może mieć min 4 max 12 liter i _  i zwrocic true jak haslo jest prawidlowe
def f(p):
    import re
    if len(p)<4 or len(p)>12:
       return False
    
    result=re.findall(r"[A-Za-z_]",p)
    if len(result)>=1:
        return True

print(f("Ab_"))
