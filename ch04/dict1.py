my_dict1={}
print(my_dict1)

my_dict2={0:1, 1:-2}
print(my_dict2)
my_dict2[3]=9.99
print(my_dict2)
my_dict2[10]=7.77
print(my_dict2)

my_dict3={'이름':'홍길동', '성별': '남자', '나이':567, '만나이':566}
print(my_dict3)
print(my_dict3['이름'])
print(my_dict3['성별'])
print(my_dict3['나이'])
print(my_dict3.get('만나이'))

print(my_dict3.get('주소')) # 에러안남
print(my_dict3['주소'])     # 에러 남
