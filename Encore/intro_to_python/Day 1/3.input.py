#print(): 출력
#input(): 키보드 입력

#input()로 받은 값을 name에 저장
'''
name = input('이름을 입력하시오')
age = input('나이를 입력하시오')

print('name:', name)
print('age:', age)
#print('10년 뒤 나이:', age+10) <- 이렇게 입력하면 age를 str으로 불러오기 때문에('12') 연산이 되지 않고 에러가 난다
print('10년 뒤 나이:', int(age)+10)
'''
#숫자 2개를 입력받아 더하기, 빼기, 곱하기, 나누기 결과 출력하기


a = input('첫번째 숫자를 입력하세요')
b = input('두번째 숫자를 입력하세요')

print('더하기: a + b =', int(a)+int(b))
print('뺴기: a - b =', int(a)-int(b))
print('곱하기: a * b =', int(a)*int(b))
print('나누기: a / b =', int(a)/int(b))


a = int(input('첫번째 숫자를 입력하세요'))
b = int(input('두번째 숫자를 입력하세요'))

print('더하기: a + b =', a+b)
print('뺴기: a - b =', a-b)
print('곱하기: a * b =', a*b)
print('나누기: a / b =', a/b)
