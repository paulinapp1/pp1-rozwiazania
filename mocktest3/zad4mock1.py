def f(fnc,prods):
    mapped_ids = map(fnc, prods)
    return ','.join(mapped_ids)


prods = ["water", "cheese", "tomato"]

fnc1 = lambda x: "id:" + x[:2]
result1 = f(fnc1, prods)
print(result1)  

fnc2 = lambda x: (x[0] + x[-1]).upper()
result2 = f(fnc2, prods)
print(result2)  
