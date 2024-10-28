import re
def f(array):
    counter=0
    formula= r'^[a-z0-9_]{4,12}$'
    for username in array:
        if re.match(formula,username):
            counter+=1
    return counter



arr=["uek","water_7_x","anna.may","a_b_c_d_e_f"]
print(f(arr))