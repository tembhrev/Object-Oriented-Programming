class Greeting:
    def __init__(self, name):
        self.name = name
        print("Object constructed")

    def __del__(self):
        print("Destructor started")

    def SayHello(self):
        print("Hello", self.name)

x1 = Greeting("Vikas")
x2 = x1
x2.SayHello()
del x1
del x2
        
