temp={"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
result=list(filter(lambda val: temp[val]>0, temp))
print(result)