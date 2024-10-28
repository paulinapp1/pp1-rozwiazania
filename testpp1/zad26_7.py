import re
text="To be, or not to be, that is the question"
vowels=re.findall(r'[aeiouAEIOU]', text)
print(len(vowels))