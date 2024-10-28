import re
with open("data.txt", 'r', encoding="utf-8") as file:
        text = file.read()
        words = re.findall(r'\b\w{6,}\b', text)
        for word in words:
            print(word)