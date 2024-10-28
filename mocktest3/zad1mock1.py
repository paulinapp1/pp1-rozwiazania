def f(word):
    if len(word) == 0:
        return ""
    elif len(word) == 1:
        return word.upper()

    wave = []
    for i in range(len(word)):
        waved_word = word[:i].lower() + word[i].upper() + word[i + 1:].lower()
        wave.append(waved_word)
    
    return "-".join(wave)

print(f("book"))