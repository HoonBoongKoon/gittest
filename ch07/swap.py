def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

na=10
nb=20
na,nb=swap(na,nb)
print(na, nb)


global a