with open('meatandfish.txt', 'r') as meat:
    content=meat.read()
with open('grainsandbread.txt', 'r') as grains:
    content2=grains.read()
with open('allproducts.txt', 'w') as all:
    all.write(content)
    all.write(content2)