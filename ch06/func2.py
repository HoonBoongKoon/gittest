def aaa():
    print('aaa')
def bbb():
    aaa()
    print('bbb')
def ccc():
    bbb()
    print('ccc')

ccc()

print('-------------------')

def fadd(pa, pb):
    pc = pa + pb
    return pc

na=10
nb=20
nc=fadd(na,nb)
print(na,'+',nb,'결과값은',nc,'이다')


print('-------------------')


