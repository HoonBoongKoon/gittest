class Cexm:
    def fsam(self):
        print("멤버함수(메소드)")
    def fsbm(self, pa):
        self.x = pa
        print('멤버번수 x는', self.x)


ca=Cexm()
ca.fsam()
ca.fsbm(10)
print(ca.x)