#주석: 프로그램 실행에 영향을 주지 않는다
#으로 변수를 정의

"""
이것은
여러 줄 주석을 주고 싶을 때
작은따옴표나 큰따옴표 세 개로 표시
"""

name = 'aaa'
age = 12
height = 170.4
bool_val = True

print('str_val:', name, ', type', type(name))
print('int_val:', age, ', type', type(age))
print('float_val:', height, ', type', type(height))
print('bool_val:', bool_val, ', type', type(bool_val))


#print 함수 사용 시 줄바꿈 & 이어쓰기
print('hello \nworld')
print('hello ', end='')
print('python')
