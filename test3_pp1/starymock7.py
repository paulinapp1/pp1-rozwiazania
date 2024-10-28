def f(arr):
    import re
    result=0
    for username in arr:
       if re.match(r"^[a-z0-9_]{4,12}$",username):
           result+=1
    return result
   

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]) )