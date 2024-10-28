def f(sentence):
    result=""
    for word in sentence:
        if word!=" ":
         result+=word
    return result

print(f("integrated development environment") )
