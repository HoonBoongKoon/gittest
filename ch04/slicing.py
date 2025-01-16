# print(week[시작인덱스:끝인덱스+1])
week = ['월', '화', '수', '목', '금', '토', '일']
# print(week)
print(week[0:3])
# 월요일부터 수요일까지
print(week[3:7])
print('--------')
# print(week[5:2])
# print(week[4:3])

# print(week[-1])
# print(week[-2])
# print(week[-3])
# print(week[-1:-4]) # []

print(week[:7]) # 0부터 
print(week[3:])
print(week[:])
print(week[-4:-1]) # 이건 됨. 왼쪽에서 오른쪽으로 읽는 건 다 된다

#사용자로부터 입력 받은 시간이 정각인지 다음과 같이 판별하기
#split()으로 푸는법
a= input("현재 시간: ")
time, minute = a.split(":")
if minute=="00":
    print('정각입니다.')
else:
    print('정각이 아닙니다.')

#slicing으로 해결하는 법
a= input("현재 시간: ")
if a[3:5]=='00':
    print('정각입니다.')
else:
    print('정각이 아닙니다.')