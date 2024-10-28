def num_of_words(word):
    list_of_words=word.split()
    return len(list_of_words)

def order(word):
    list_of_words=word.split()
    sort=sorted(list_of_words, key=len)
    return sort[::-1]

def alphabet(word):
    list_of_words=word.split()
    return sorted(list_of_words)

