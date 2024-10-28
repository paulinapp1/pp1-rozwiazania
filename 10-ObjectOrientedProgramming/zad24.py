class C:
    def __init__(self, points, n):
        self.points=points
        self.n=n
    def first(self):
        counter=0
        for row in self.points:
            if row[0]>0 and row[1]>0:
                counter+=1
        if counter==self.n:
            return True
        else:
            return False

cor1=C([[2,3],[1,8],[-6,4],[3,-7]], 3)
result=cor1.first()
print(result)
        