class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print("Object created")

    def printDetails(self):
        print(self.x, self.y)

pt1 = Point(4, 6)
pt1.printDetails()
pt2 = Point(-3, 8)
pt2.printDetails()
