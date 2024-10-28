def words(a):
    words = a.split()  # Split the text into words
    return len(words)
  
def longtoshort(a):
    words=a.split()
    return sorted(words, key=len, reverse=True) 
def alphabet(word):
    words = word.split()
    
    return sorted(words, key=len)



a="An apple a day keeps the doctor away"
print(words(a))
print(longtoshort(a))
print(alphabet(a))