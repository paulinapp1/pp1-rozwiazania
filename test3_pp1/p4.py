def f(fnc,prods):
    result=map(fnc,prods)
    return ",".join(result)

prods = ["water","cheese","tomato"] 
fnc1 = lambda x: "id:"+x[:2] 
print(f(fnc1,prods)) 
fnc2 = lambda x: (x[0]+x[-1]).upper() 
print(f(fnc2,prods) )
