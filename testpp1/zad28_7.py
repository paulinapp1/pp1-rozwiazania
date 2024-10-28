import re
with open("data.txt",'r', encoding='utf-8')as file:
    data=file.read()
    six=re.findall(r'\w{6,}',data)
print(len(six))
