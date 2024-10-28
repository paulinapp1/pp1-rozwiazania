def f(detector):
    current_count=0
    max_count=0
    for status in detector:
        if status=="+":
            current_count+=1
        else:
            current_count=0
        if current_count>=3:
            max_count=1
    if max_count==1:
        return True
    else:
        return False
    
print(f("+-++-++-+---"))