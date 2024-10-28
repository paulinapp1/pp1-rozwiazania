#Tablica arr ma liczby całkowite (np 4,4,4,4,3,3,3,2,2,2,2). Wszystkie się powtarzają parzystą ilość razy a 
#jedna nieparzysta ilość razy. Zwróć tą liczbę
def f(n):
   for num in n:
    if  n.count(num)%2!=0:
      return num
    
arr=[4,4,4,4,3,3,3,2,2,2,2]
print(f(arr))