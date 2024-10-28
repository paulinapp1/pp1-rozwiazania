def f(register):
    current_status=0
    for status in register:
        if status=='+':
            current_status+=1
        else:
            current_status=current_status-1
    return current_status

print(f("+-+++++-"))
