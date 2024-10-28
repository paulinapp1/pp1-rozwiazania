import re
def f(filename):
    with open(filename+".txt", "r", encoding='utf-8')as file:
        content=file.read()
        sixletters=re.findall(r'\b\w{6,}\b',content)
    return len(sixletters)

print(f("allproducts"))