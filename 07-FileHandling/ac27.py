import re
def f(expression):
    words=re.findall(r'\b\w+\b', expression)
    return len(words)

expression="To be, or not to be, that is the question"
print(f(expression
))