# clovers=('클로버1', '클로버2', '클로버3')
# print(clovers[1])

# clovers=('클로버1',)
# print(type(clovers))

# clovers='클로버1', '클로버2', '클로버3'
# print(type(clovers))

# clovers=()
# print(type(clovers))

clovers = (1, '하트2', 3.1415, [1,2])
clovers[3][1] = 5
#clovers[3] = [4,5] 는 안됨
print(clovers)
print(type(clovers))


print('-------------------')
a = (1,2,3)
print(a, "a 데이터 타입:",type(a))
b=list(a)
print(b, 'b 데이터 타입:',type(b))
b[0]=7
print(b)
a=tuple(b)
print(a, "a 데이터 타입:",type(a))
