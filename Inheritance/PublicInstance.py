class A(object):
    def __init__(self):
        self.a, self.b = 10, 20

    def method1(self):
        print("Class A's method 1")

class B(A):
    def __init__(self):
        self.c  = 30
        A.__init__(self)
    def __str__(self):
        string ="a :"+str(self.a)+" b :"+str(self.b)+"c :"+str(self.c)
        return string

obj1 = B()
print(obj1)
obj1.a += 25
print(obj1)