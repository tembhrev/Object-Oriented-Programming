class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        self.__z = 0

    def __str__(self):
        string = "("+str(self.x)+","+str(self.y)+","+str(self.__z)+")"
        return string

pt1 = Point(3,4)
print(str(pt1))
print(pt1.x, pt1.y, pt1.z)
