class A(object):
    def method1(self):
        print("A's method1")

class C(A):
    def method1(self):
        print("C's method1")
        # A.method1(self)
        super(C, self).method1()

class D(C):
    def method1(self):
        print("D's method1")
        # C.method1(self)
        super(D, self).method1()

obj1 = D()
obj1.method1()