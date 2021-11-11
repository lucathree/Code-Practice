'''
b=[1,2,3,4,5]

print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])

for i in [1,2,3,4,5]:
    print(i)

for i in b:
    print(i)

for i in 'hello world':
    print(i)

for i in range(0,5): #list 구성 [0,1,2,3,4]
    print(i)

for i in range(1,10,2): #[1,3,5,7,9], range(시작값, 끝값, 간격]
    print(i)
'''

#1. 1-10 출력 for, range 사용
for i in range(1,11):
    print(i)

#2. 1-10 사이 짝수 출력
for i in range(2,11,2):
    print(i)
#또는
for i in range(1,11):
    if i%2==0:
        print(i, end=', ')
print()
#3. 1-100까지 합
sum=0
for i in range(1,101):
    sum+=i
print(sum)

#4. 구구단 3단
for i in range(1,10):
    dan=3
    print(dan,'*',i,'=',dan*i)

#이중 for문

for j in range (0,2):
    for i in range(0,3):
        print('#',end='')
    print()

#구구단 전체 출력

for j in range(2,10):
    for i in range(1,10):
        print(j,'*',i,'=',j*i)
    print()

#break와 continue
for i in range(1,11): #1~10
    if i%2 == 0: #짝수일 경우
        continue
    print(i)          #제어문은 짝수를 대상으로 하고 있지만 결과적으로는 홀수를 프린트한다
