pln=int(input('Enter amount in pln: '))
piec=0
dwa=0
jeden=0
while pln>=5:
    pln=pln-5
    piec=piec+1
while pln>=2:
    pln=pln-2
    dwa=dwa+1
while pln>=1:
    pln=pln-1
    jeden=jeden+1




print(piec, dwa, jeden)

