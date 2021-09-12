class A(object):
    def __init__(self, a):
        self.a = a 
        print("A created")

class B(object):
    def __init__(self, b, c):
        self.b, self.c = b, c
        print("B created")

class C(A, B):
    def __init__(self,a, b, c, d):
        A.__init__(self, a)
        B.__init__(self, b, c)
        
        self.d = d
        print("C created")

cobj = C(2, 3, 4, 5)
