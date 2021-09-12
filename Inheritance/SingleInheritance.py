class Car(object):
    def __init__(self, clr, seats):
        self.colour = clr
        self.seatingCapacity = seats
        print("Car instance created")

    def accelerate(self, time, direction):
        print("Inside accelerate method")

    def turn(self, direction):
        print("Inside turn method")

    def applyBrakes(self, pressure):
        print("Inside applyBrakes method")

    def __str__(self):
        return self.colour+"coloured Car with"+str(self.seatingCapacity)+"seats"

class RacingCar(Car):
    def __init__(self, clr, seats, tr, spd):
        Car.__init__(self, clr, seats)
        self.turnRadius = tr
        self.avgSpeed = spd
        print("RacingCar instance created.")

    def __str__(self):
        string = self.colour + "RacingCar with" + str(self.turnRadius)+"\"turn radius & speed"+ str(self.avgSpeed)+"rpm"
        return string

#--------main segment------------
mycar = Car("Blue", 5)
rcar = RacingCar("Red", 2, 6, 190)
print(mycar)
print(rcar)
print(isinstance(rcar, Car))
print(issubclass(RacingCar, Car))
