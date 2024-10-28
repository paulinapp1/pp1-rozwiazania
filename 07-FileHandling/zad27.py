import re

text = "To be, or not to be, that is the question"

# Find all occurrences of words in the text
words = re.findall(r'\b\w+\b', text)

# Count the number of words found
num_words = len(words)

print(f"The number of words in the text is: {num_words}")
