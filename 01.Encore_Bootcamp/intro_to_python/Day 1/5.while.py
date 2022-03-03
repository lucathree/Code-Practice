'''
# 5부터 1까지 출력하기
a=5
while a>0:
    print(a)
    a-=1

print('loop end')

# 1부터 10까지 출력하기
a=1
while a<=10:
    print(a)
    a+=1

print('출력 끝')
'''

# 1부터 100까지의 합을 구하기 (결과값: 5050)
print('1.1부터 100까지의 합')
a=1
sum=0
while a<=100:
    sum+=a
    a+=1
print(sum)

# 1부터 100까지 짝수만 출력하기
print('2.1부터 100까지 짝수만 출력')
b=1
while b<=100:
    if b%2==0:
        print(b,'',end='')
    b+=1

# 구구단 단수를 입력받아 한 단 출력
print('\n3.입력된 값의 구구단 출력')
c=1
num = int(input('구구단 단수를 입력하세요:'))
while c<=9:
    print(num,"*",c,"=",num*c)
    c+=1

# 약수 구하기
print('4.입력된 값의 약수 출력')
d=1
num2 = int(input('숫자를 입력하세요:'))
while d<=num2:
    if num2%d==0:
        print(d)
    d+=1