class Student:


    def __init__(self, rno, name, mks):
        self.rollNo = rno
        self.name = name
        self.marks = mks
        self.grade = ''
        print("defined in module", Student.__module__)
        



#------main--------
stud1 = Student(12, "Nitin", 68.5)
print("from the main of", Student.__module__)


