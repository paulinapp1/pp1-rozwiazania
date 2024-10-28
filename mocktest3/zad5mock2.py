import math
class C:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        if self.x>0 and self.y>0:
            self.location=1
        elif self.x<0 and self.y>0:
            self.location=2
        elif self.x<0 and self.y<0:
            self.location=3
        else:
            self.location=4
    def m1(self):
        if self.x == 0 or self.y == 0:
            return 0
        elif self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
    def m2(self,a,b):
        if a>0 and self.x>0 and b>0 and self.y>0:
            return True
        elif a<0 and self.x<0 and b<0 and self.y<0:
            return True
        elif a<0 and self.x<0 and b>0 and self.y>0:
            return True
        elif a>0 and self.x>0 and b<0 and self.y<0:
            return True
        else:
            return False
    def m3(self, a, b):
        distance = math.sqrt((self.x - a) ** 2 + (self.y - b) ** 2)
        return distance > 5
            


p = C(2, 3)
print(p.m1())      # Output: 1
print(p.m2(7, 4))  # Output: True
print(p.m2(-3, 1)) # Output: False
print(p.m3(8, 5))  # Output: True
print(p.m3(4, 7))  # Output: False

p1 = C(0, 5)
print(p1.m1())     # Output: 0
print(p1.m2(4, 7)) # Output: False
print(p1.m2(-7, 0))# Output: True
        

        

        