class Bag:
    def __init__(self):
        self.data=[]
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
    
prada = Bag()
prada.add('손수건')
prada.addtwice('카드')
print(prada.data)

gucci = Bag()
gucci.addtwice('립밤')
print(gucci.data)