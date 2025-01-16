candy0='딸기맛'
candy1='레몬맛'
candy2='수박맛'
candy3='박하맛'
candy4='우유맛'

candies=['딸기맛','레몬맛','수박맛','박하맛', '우유맛']
print(candies)

a=[candy0,candy1,candy2]
print(a)

candy0='바나나맛'
print(a)

ca = [10, 11, 21]
print(ca[0], end=",")
print(ca[1], end=",")
print(ca[2])

print(type(ca))
print(type(ca[1]))

print("----------------")
lista = [1, "python", 3.9, "프로그래밍"]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print("----------------")
candies = []
print(candies)
candies.append(candy0)
candies.append(candy1)
candies.append(candy2)
candies.append(candy3)
print(candies)

print("----------------")
clovers=['클로버1', '클로버2', '클로버3']
print(clovers[2])
print(clovers)
del clovers[2]
print(clovers)
print(clovers[1])

print("----------------")
clovers.insert(0,'클로버0')
print(clovers)

clovers.extend(['클로버3', '클로버4'])
print(clovers)