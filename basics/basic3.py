class Student():
    num_of_students = 0
    class_teacher = "Mrs. David"
    def __init__(self, rno, name, mks):
        self.rollno = rno
        self.name = name
        self.marks = mks
        self.grade = ''
        Student.num_of_students += 1

    def calcGrade(self):
        if self.marks >= 80:
            self.grade = "A+"
        elif self.marks >= 70:
            self.grade = "A"
        elif self.marks >= 60:
            self.grade = "B"
        elif self.marks >= 50:
            self.grade =  "C"
        elif self.marks >= 40:
            self.grade =  "D"
        else: 
            self.grade = "E"

stud1 = Student(12, "Nitin", 68.5)
stud2 = Student(14, "Joseph", 80.25)
stud3 = Student(16, "Zain", 59.5)
stud4 = Student(18, "Nimrat", 47.5)


stud1.calcGrade()
print("Grade of rollnumber {} - {} is  : {}".format(stud1.rollno, stud1.name, stud1.grade))
stud2.calcGrade()
print("Grade of rollnumber {} - {} is  : {}".format(stud2.rollno, stud2.name, stud2.grade))
stud3.calcGrade()
print("Grade of rollnumber {} - {} is  : {}".format(stud3.rollno, stud3.name, stud3.grade))
stud4.calcGrade()
print("Grade of rollnumber {} - {} is  : {}".format(stud4.rollno, stud4.name, stud4.grade))
