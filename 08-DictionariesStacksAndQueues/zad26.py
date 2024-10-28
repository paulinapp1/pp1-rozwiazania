def maskify(cc):
    long=len(cc)-4
    result=""
    for letter in range(len(cc)):
        if letter<long:
            result+="#"
        else:
            result+=cc[letter]
    return result

print(maskify("4393192029"))