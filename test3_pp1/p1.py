def f(word):
    words=[]
    if len(word)==1:
        return word.upper()
    for i in range(len(word)):
        waved=word[:i].lower()+word[i].upper()+word[i+1:].lower()
        words.append(waved)
    return "-".join(words)

print(f("A"))
