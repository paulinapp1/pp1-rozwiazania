import re

text = "To be, or not to be, that is the question"


# Find all occurrences of vowels in the text
vowels = re.findall(r'[aeiouAEIOU]', text)

# Count the number of vowels found
num_vowels = len(vowels)

print(f"The number of vowels in the text is: {num_vowels}")
