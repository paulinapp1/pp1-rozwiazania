final=[3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
art=list(filter(lambda x:x>2.0, final))
total=sum(art)
mean=total/len(art)
print(f"Arithmetic mean for grades <> 2.0 is {round(mean, 2)}")