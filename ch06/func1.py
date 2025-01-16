def my_func():
    print('토끼야 안녕!')

my_func()
my_func()

def funca(na):
    print(na)

funca(8)
funca(3)
funca(7)

def funca1(na):
    print(na)
def funca2(na, nb):
    print(na,nb)

funca1(8)
funca2(2,3)

def funca3(a,b,c):
    sum=a+b+c
    print(sum)
funca3(4,4,4)

def funca4(a,b,c):
    sum=a+b+c
    return sum
print(funca4(1,2,3))

def add(a,b):
    c=a+b
    return
result = add(1,2)
print(result)

def myabs(arg):
    if(arg<0):
        result = arg* -1
    else:
        result = arg
    return result

print(myabs(10))
print(myabs(-8))
print(myabs(-2))