class SplNumber:
    def __init__(self, value = 0, name=""):
        self.number = value
        self.name = name

    def __add__(self, y):
        number = self.number + y
        return SplNumber(number, self.name)

    def __sub__(self, y):
        number = self.number - y
        return SplNumber(number, self.name)

    def __mul__(self, y):
        number = self.number * y
        return SplNumber(number, self.name)

    def __floordiv__(self, y):
        number = self.number // y
        return SplNumber(number, self.name)

    def __mod__(self, y):
        number = self.number % y
        return SplNumber(number, self.name)

    def __str__(self):
        return "|... "+ str(self.number) + ", "+ self.name + " ...|"

#-------main-------
num1 = SplNumber(30, "Spl")
print("Original Number is", num1)
print("-"*40)
num2 = num1 + 5
num3 = num1 - 5
num4 = num1 * 3
num5 = num1 // 5
num6 = num1 % 7

print("Original number + 5 =", num2)
print("Original number - 5 =", num3)
print("Original number * 3 =", num4)
print("Original number / 5 =", num5)
print("Original number % 7 =", num6)