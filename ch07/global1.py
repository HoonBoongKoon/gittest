# b=0
# print(b)
# b=1
# print(b)

# def scope_test():
#     global a
    
#     a=a+3
#     print(f'scope_test() 함수 안의 a 값은 {a}')

# a=0
# print(f'scope_test() 함수 밖의 a 값은 {a}')
# scope_test()
# print(f'scope_test() 함수 후의 a 값은 {a}')

print('--------------------------------')

def scope_test():
    a=0    
    a=a+3
    print(f'scope_test() 함수 안의 a 값은 {a}')

a=0
print(f'scope_test() 함수 밖의 a 값은 {a}')
scope_test()
print(f'scope_test() 함수 후의 a 값은 {a}')