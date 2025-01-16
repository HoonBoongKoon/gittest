# a=int(input("숫자 입력: "))

# b= a+20

# if b>255:
#     print(255)
# else:
#     print(b)

# a=int(input("숫자 입력:"))
# b = a-20
# if b<0:
#     print(0)
# elif b>255:
#     print(255)
# else:
#     print(b)

# a= input("현재 시간: ")
# time, minute = a.split(":")
# if minute=="00":
#     print('정각입니다.')
# else:
#     print('정각이 아닙니다.') 

score = int(input("성적: "))
if score>80:
    print("grade is A")
elif score>60:
    print("grade is B")
elif score>40:
    print("grade is C")
elif score>20:
    print("grade is D")
elif score>0:
    print("grade is E")