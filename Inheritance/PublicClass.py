class A(object):
    name = "interesting"
    def __init__(self):
        self.a, self.b = 10, 20

class B(A):
    def __init__(self):
        self.c = 30
        A.__init__(self)
    def __str__(self):
        string = "a:"+str(self.a)+" b:"+str(self.b)+" c:"+str(self.c)
        string += "& name : "+B.name
        return string
obj1 = B()
print(obj1)
print(B.name)