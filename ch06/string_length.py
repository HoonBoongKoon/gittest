# sta="python example"
# def string_length(stb):
#     result=0
#     for i in stb:
#         result+=1
#     return result
# lena=string_length(sta)
# print(lena)

# print('--------------')

# # def fdiv(a,b):
# #     if b==0:
# #         print('0으로 나눌 수 없습니다')
# #     else:
# #         print(a/b)

# # a,b=map(int,input().split())
# # fdiv(a,b)

# a=int(input())

# def mul(a):
#     result=0
#     for i in range(1,101):
#         if i%a==0:
#             result+=i
#     print(result)

# mul(a)

# for i in range(1,10):
#     for j in range(1,10):
#         print (i,"*",j,"=",i*j)

# def print_hello():
#     print("안녕하세요")

# print_hello()
# for i in range(100):
#     print_hello()

def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet("Alice"))
