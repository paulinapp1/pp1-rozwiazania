#Tablica dwuwymiarowa zawiera ile osob wsiadlo do autobusu i ile wysiadlo zwrocic ile zostalo w autobusie
def f(arr2d):
    number_of_people=0
    for i in range(len(arr2d)):
        number_of_people += arr2d[i][0]
        number_of_people -= arr2d[i][1]
    return number_of_people



print(f([[3,0]]))
print(f([[3,0],[6,1]]))
print(f([[6,0],[5,0]]))
print(f([[4,0],[10,8]]))