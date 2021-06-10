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
'''

i=1
while i<=100:
    print(i, end='\t') #'\t'는 공백
    if i%10==0:     #10단위로 줄바꿈을 하기위한 태그
        print()     #안에 내용이 없는 print()는 공백줄바꿈이라고 보면 됨
    i+=1

'''
#짝수 구하기 출력방법 수정
print('2.1부터 100까지 짝수만 출력')
b=1
while b<=100:
    if b%2==0:
        print(b,end='\t')
        if b%20==0:
            print()
    b+=1
'''
#짝수 구하기 다른 방법
print('# 1부터 100까지 짝수만 출력')
b=2
while b<=100:
    print(b, end='\t')
    b+=2
print()

# 구구단을 9단까지 모두 출력하기
print('# 구구단 출력')
num=2
c=1
while num<=9:
    print('구구단',num,'단')
    while c<=9:
        print(num,"*",c,"=",num*c)
        c+=1
    print()
    num+=1
    c=1

#이중루프를 사용하여 아래 형태로 #출력하기

####
####

row=2
while row>0:
    sharp=4
    while sharp>0: #down counting
        print('#',end='')
        sharp-=1
    print()
    row-=1

# 점수 입력 받을 때 올바른 점수를 입력할 때까지 점수 받기 (조건에 의한 반복)
score = int(input('score(0-100):'))
while score>100 or score<0:
    score = int(input('wrong input!\nscore(0-100):'))

if score >= 60:
    print('합격')
else:
    print('불합격')
