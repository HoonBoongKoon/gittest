# def fmax(sua,sub,suc):
#     max=sua
#     if max<sub:
#         max=sub
#     elif max<suc:
#         max=suc
#     return max
# print(fmax(10,5,7))

# def print_lower_price(price =0):
#     discount = price * 0.9
#     return(discount)
# price = int(input("현재가 입력하세요.: "))
# p = print_lower_price(price)
# print(p)

# def make_list(_str):
#     return list(_str)
# print(make_list('asdf'))

'''
def make_list(str):
    result=[]
    for i in str:
        result.append(i)
    return result
print(make_list("abcd"))
'''

def pickup_even(str):
    result=[]
    for i in str:
        if (int(i))%2==0:
            result.append(i)
    return result
nums=[2,3,4,1,2,3,4,6,3]
print(pickup_even(nums))

dic = {'애플': 'apple.com', '파이썬': 'python.org', '구글': 'google.com'}

print(dic.keys())
print(dic.values())
print(dic.items())

for key in dic.keys():
    print(key)
