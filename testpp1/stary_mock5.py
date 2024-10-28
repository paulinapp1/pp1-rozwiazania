import re
def f(first_letter,last_letter):
    with open("data.txt", 'r', encoding='UTF-8')as file:
        content=file.read()
        expression=r'\b'+first_letter+r'\w*'+last_letter+r'\b'
        result=re.findall(expression,content)
    return len(result)

print(f("w","d"))

