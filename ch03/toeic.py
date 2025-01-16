# 900 이상 : 상위권
# 600 이상 : 상위권
# 300 이상 : 상위권

tscore=700
if tscore>=900:
    print('토익점수는', tscore, '상위권')
elif tscore>=600:
    print('토익점수는', tscore, '중상위권')
elif tscore>=300:
    print('토익점수는', tscore, '중위권')
else:
    print('토익점수는', tscore, '하위권')
print('if문 종료')