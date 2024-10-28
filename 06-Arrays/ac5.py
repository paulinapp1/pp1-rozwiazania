arr=[-15,8,-31,47,-2,19]
max=0
min=1000
for i in arr:
    if int(i)>max:
        max=i

for i in arr:
    if int(i)<min:
        min=i

print("max", max)
print("min", min)