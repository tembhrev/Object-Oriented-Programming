class A:
    def __init__(self) -> None:
        val1 = 10

    def method1(self):
        print("method 1 of A")

class B(A):
    def __init__(self):
        myvar = 20
    
    def method1(self):
        print("method 1 of B")

    def method2(self):
        A.method1(self)

b = B()
b.method1()
b.method2()