class Person(object):
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def __str__(self):
        string = self.name + " is "+str(self.age) + "years old"
        return string

class Student(Person):
    def __init__(self, n, a, s):
        # Person.__init__(self, n, a)
        super(Student, self).__init__(n,a)
        self.school = s
    
    def __str__(self):
        string = self.name+ " is "+str(self.age)+"years ild and attends "+self.school
        return string

p = Person("Nisha", 57)
print(p)
s = Student("Barry", 12, 'Sun Rays School')
print(s)

