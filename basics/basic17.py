#Adding a method dynamically using MethodType function of types module
from types import MethodType

class Person(object):
    def __init__(self, name):
        self.name = name
def play(self):
    print("{} is playing".format(self.name))

Person.method_a = play
p = Person("Ranjan")
# p.method_a = MethodType(play,p)
p.method_a()
p1 = Person("Vikas")
p1.method_a()