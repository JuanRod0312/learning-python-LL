#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class vehicle ():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle
    def drive(self,speed):
        self.mode = "driving"
        self.speed = speed
    def parking(self, spot):
        self.mode = "Parked"
        self.spot = spot

class Car(vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)

    def parking(self, spot):
        super().parking(spot)
        print("My car is parked at", self.spot, "In the parking garage")

class motorcycle(vehicle):
    def __init__(self,enginetype,sidecar):
        super().__init__("Motorcycle")
        if(sidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "Motorcycle at", self.speed)

car1 = Car("gas")
car2 = Car("electric")
mc1 = motorcycle("gas", True)

print (car1.enginetype)

car1.drive(40)
mc1.drive(30)
car1.parking(72)


        
        
        
