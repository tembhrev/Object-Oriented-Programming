def func(self):
    print("written outside class")

class A_Class(object):
    def method_a(self):
        print("Inside statically bound method a")


instance = A_Class()
instance.method_a()

#Adding method dynamically in class
setattr(A_Class, 'method_b', func)
instance.method_b()
