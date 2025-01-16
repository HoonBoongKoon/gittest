for num in [0,1,2]:
    print(num)

characters = ['앨리스', '도도새', '3월토끼']
for char in characters:
    print(char)

print("--------------")
characters = ['앨리스', '도도새', '3월토끼']
for char in characters:
    pass

print("--------------")
for letter in '체셔고양이':
    # print(letter)
    pass

print("--------------")
nums=[0,1,2]
for num in nums:
    print(num)
print(nums)

print("--------------")
nums=[0,1,2]
for num in nums:
    print(num)
    print(nums)

print("--------------")

print(range(3))
print(list(range(3)))
print(list(range(0,3)))
print(list(range(0,9,2)))

for num in range(3):
    print(num)

print("--------------")
for num in range(0,3):
    print(num)
print("--------------")
for num in range(0,9,2):
    print(num)
print("--------------")
for num in range(0,13,3):
    print(num)
print("--------------")
for num in range(0,13,-1):
    print(num) # 출력 안됨.
print("--------------")
for num in range(13,0,-1):
    print(num)
print("--------------")
print(type(range(3)))
print("--------------")

result=0
for i in range(1,6):
    result+=i
print(result)