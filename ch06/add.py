# def fadd(pa, pb):
#     pc = pa + pb
#     return pc
# def fsub(pa,pb):
#     pc = pa - pb
#     return pc
# def fmul(pa,pb):
#     pc = pb * pa
#     return pc
# def fdiv(pa,pb):
#     pc = pa / pb
#     return pc

# nadd=fadd(100,3)
# nsub=fsub(100,3)
# nmul=fmul(100,3)
# ndiv=fdiv(100,3)

# print (nadd, nsub, nmul, ndiv)

# print(na,'+',nb,'결과값은',nc,'이다')

print('----------------')

def fadd(pa, pb):
    pc = pa + pb
    return pc
def fsub(pa,pb):
    pc = pa - pb
    return pc
def fmul(pa,pb):
    pc = pb * pa
    return pc
def fdiv(pa,pb):
    pc = pa / pb
    return pc

na,nb=map(int,input().split())

nadd=fadd(na,nb)
nsub=fsub(na,nb)
nmul=fmul(na,nb)
ndiv=fdiv(na,nb)

print (nadd, nsub, nmul, ndiv)