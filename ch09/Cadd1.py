class Cadd:
    def fadd(self, a,b):
        self.x = a
        self.y = b
        self.ha = self.x + self.y
obj = Cadd()
obj.fadd(10,20)
print(obj.x, obj.y, obj.ha)

obj1 = Cadd()
obj1.fadd(30,40)
print(obj1.x, obj1.y, obj1.ha)