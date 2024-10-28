import re

def count_vowels(text):
    vowels = re.findall(r'[aeiouAEIOU]', text)
    return len(vowels)

text = "To be, or not to be, that is the question"
num_vowels = count_vowels(text)
print(f"The number of vowels in the text is: {num_vowels}")