x=int(input("Enter x:"))
y=int(input("Enter y:"))
if x>0 and y>0:
    print(f'P({x},{y}) is in the first quadrant of the coordinate')
if x>0 and y<0:
    print(f'P({x},{y}) is in the fourth quadrant of the coordinate')
if x<0 and y>0:
     print(f'P({x},{y}) is in the second quadrant of the coordinate')
if x<0 and y<0:
     print(f'P({x},{y}) is in the third quadrant of the coordinate')
if x==0 and y==0:
      print(f'P({x},{y}) is in the (0,0) point of the coordinate')
if x==0 or y==0:
      print(f'P({x},{y}) lies on the line')
