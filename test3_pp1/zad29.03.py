def f(product,rinse,spin):
    total=0
    if product=='shoes':
        total+=20
    if product=='jacket':
        total+=40
    if product=='underwear':
        total+=70
    if rinse==True:
        total+=15
    if spin==True:
        total+=9
    return total

print(f('shoes',True,False))