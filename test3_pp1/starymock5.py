def f(first_letter,last_letter):
    counter=0
    with open("data.txt", encoding="UTF-8") as file:
        for line in file:
            words=line.split()
            for word in words:
                if word.startswith(first_letter) and word.endswith(last_letter):
                    counter+=1
    return counter
      

print(f("w","d"))
