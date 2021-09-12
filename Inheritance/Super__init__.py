class A(object):
    def __init__(self, a):
        self.a  = a 
        print("A's __init__")

    def method1(self):
        print("A's method1 : a is ", self.a)

class C(A):
    def __init__(self, c, a):
        
        self.c = c 
        print("C 's init")
        # A.__init__(self, a)
        super(C, self).__init__(a)

    def method1(self):
        print("C's method1 : c is ", self.c)
        # A.method1(self)
        super(C, self).method1()

obj1 = C(17, 22)
obj1.method1()
        