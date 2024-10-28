import re
text="To be, or not to be, that is the question"
words=re.findall(r'\w+', text)
print(len(words))