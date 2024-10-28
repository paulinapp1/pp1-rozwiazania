text="I completely agree with you"
new_text=text.split()
num_of_letters=list(map(lambda word:len(word),new_text))
print(f"No. of letters in words : {num_of_letters}")