class Student:
    def __init__(self, rno, name, mks):
        self.rollNo  = rno
        self.name = name
        self.marks = mks
        print("I am inside class {} of {}".format(Student.__name__, __name__))

stud1 = Student(12, "Nitin", 78.5)
print("from main of {}".format(Student.__name__))
print("I am in {}".format(__name__))
