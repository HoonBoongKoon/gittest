def personA(width, height=10):
    print(width, height)
# def personA():
#     print('no data')
def personB(width=4, height=3):
    print(width, height)

def personC(width, height=2, depth=1):
    print(width, height, depth)

personA(10,20)
personA(10)
personB()
personC(4,5)