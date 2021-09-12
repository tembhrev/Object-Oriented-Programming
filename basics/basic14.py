class Time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def increment(self, inc):
        self.hours += inc
        return self

    def later(self, time2):
        result = 1
        if self.hours > time2.hours:
            result = 1
        elif self.hours < time2.hours:
            result = 0
        elif self.minutes > time2.minutes:
            result = 1
        elif self.minutes < time2.minutes:
            result = 0

        if result == 1:
            return self
        else:
            return time2

    def __str__(self):
        return "["+str(self.hours)+":"+str(self.minutes)+"hrs"+"]"


t1 = Time(12, 4)
t2 = Time(13, 13)
t3 = t1.increment(2)

print(t1, "after 2 hours will be", t3)
t4 = t1.later(t2)

print("The later of times", t1, "and", t2, "is:", t4)











        
    
