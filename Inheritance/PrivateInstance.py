class A(object):
    def __init__(self):
        self.a = 10
        self.__b = 20

class B(A):
    def __init__(self):
        self.c = 30
        A.__init__(self)

    def __str__(self):
        string= "a:"+str(self.a)+" b:"+str(self.__b)+" c:"+str(self.c)
        return string

obj1 = B()
print(obj1)
