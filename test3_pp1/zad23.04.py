def f(text, letter):
    result=list(filter(lambda x:x==letter, text))
    return len(result)


print(f("You never get a second chance to make a first impression","e"))