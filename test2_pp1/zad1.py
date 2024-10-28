#Utwórz funkcje f(n) która zwraca True jeśli n jest w ciągu fibonnaciego, w przeciwnym razie False
def is_fibonacci(n):
    a=0
    b=1
    while a<=n:
        if a==n:
            return True
        a,b=b,a+b
    return False
        
        
 





# Przykłady użycia funkcji
print(is_fibonacci(5))  # True, ponieważ 5 należy do ciągu Fibonacciego (0, 1, 1, 2, 3, 5)
print(is_fibonacci(7))  # False, ponieważ 7 nie należy do ciągu Fibonacciego
print(is_fibonacci(8))  # True, ponieważ 8 należy do ciągu Fibonacciego (0, 1, 1, 2, 3, 5, 8)

