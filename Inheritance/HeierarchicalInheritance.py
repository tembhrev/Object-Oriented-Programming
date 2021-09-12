class Animal(object):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name, " says ", self.sound())

class Cow(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def sound(self):
        return "moo"

class Horse(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def sound(self):
        return "neigh"

class Sheep(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def sound(self):
        return "baaaaa"

#---main----
s = Horse("Chetak")
s.speak()
c = Cow("Rambha")
c.speak()
Sheep("Mithi").speak()