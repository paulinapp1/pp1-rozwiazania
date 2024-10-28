import re
def f(first_letter,last_letter):
    pattern = r'\b' + first_letter + r'\w*' + last_letter + r'\b'
    with open("data.txt","r",encoding='utf-8')as file:
        data=file.read()
        startend=re.findall(pattern,data)

    return len(startend)

print(f("w","d"))