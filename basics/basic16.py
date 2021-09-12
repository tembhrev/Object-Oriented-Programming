#Setting attribute for method dynamically
class Person(object):
    pass

def play():
    print("i' m playing!")

p = Person()
p.play = play
p.play()
