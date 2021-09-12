class Student:
    """
        stores details of student
        Attributes:
        rollno: roll number of student
        marks: marks of student out of 500
    """


    def __init__(self, rno, mks):
        self.rollno = rno
        self.marks = mks
        self.percentage = 0

    def calcPerc(self):
        self.percentage = self.marks/500 * 100

stud1 = Student(12, 478.5)
print("class student's base class :", Student.__bases__)
print("--Documentation string is--")
print(Student.__doc__)