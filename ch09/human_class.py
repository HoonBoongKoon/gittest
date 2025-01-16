class Human:
    def __init__(self, age, name):
        self.age=age
        self.name=name
    def intro(self):
        print(str(self.age), '살', end=" ")
        print(self.name + "입니다")

kim = Human(23,'송주훈')
kim.intro()