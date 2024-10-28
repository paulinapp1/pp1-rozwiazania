my_array=[-15,8,-31,47,-2,19]
max=0
min=0
for value in my_array:
    if int(value)>max:
        max=int(value)
    
for value in my_array:
    if int(value)<min:
        min=(value)

print(min)
print(max)