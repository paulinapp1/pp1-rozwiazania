def count_occurences(touple,n):
    occurences=touple.count(n)
    return occurences
sample_tuple = (50, 20, 40, 50, 30, 50)
print(count_occurences(sample_tuple,50))