class Car:
    def __init__(self, pnum, pspeed):
        self.num = pnum
        self.speed = pspeed
    def fprint(self):
        print(self.num)
        print(self.speed)

new_car = Car(2023,90)
new_car.fprint()
    