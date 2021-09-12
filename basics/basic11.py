class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        self.__z = 0
        print("Object created with", self.__printDetails())

    def __printDetails(self):
        print(self.x, self.y, self.__z)

pt1 = Point(3,4)
pt1.__printDetails()
