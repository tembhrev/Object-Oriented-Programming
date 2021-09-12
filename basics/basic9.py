class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        string = "("+str(self.x)+","+str(self.y)+")"
        return string

pt1 = Point(3,4)
pt2 = Point(8,9)
print(str(pt1))
print(pt2)
