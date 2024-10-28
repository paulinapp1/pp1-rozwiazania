def f(fnc, res):
    filtered_results = list(filter(fnc, res))
    if filtered_results:
        return max(filtered_results) - min(filtered_results)
    else:
        return None

res = [95, 90, 20, 50, 70]

fnc1 = lambda x: x > 50
print(f(fnc1, res)) 

fnc2 = lambda x: x > 30 and x < 90
print(f(fnc2, res))  

