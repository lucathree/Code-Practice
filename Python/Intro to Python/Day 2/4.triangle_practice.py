'''
1. 1~100 소수 출력
2. 크기 입력받아 삼각형 출력
*
**
***
****
3. 크기 입력받아 삼각형 출력
    *
   **
  ***
 ****
*****
4. 크기 입력받아 삼각형 출력
  *
 ***
*****
5. 크기 입력받아 삼각형 출력
  *
 ***
*****
 ***
  *


1. 1~100 소수출력 while 사용
소수(약수가 1과 자신밖에 없는 수)를 찾으려면 약수 중에서 1을 제외하고 num보다 작은 수가 있으면 안된다
'''
# while문 사용
num=2
while num<=100:
    i=2
    while i<=num:
        if num%i == 0:
            if i < num:
                break
            else:
                print(num, end=' ')
        i+=1
    num+=1
print()
# for문 사용
for num in range(2,101):
    for i in range(2,num+1):
        if num%i == 0:
            if i < num:
                break
            else:
                print(num, end=' ')
print()

'''
2. 크기 입력받아 삼각형 출력
*
**
***
****
'''
size=int(input('첫번째 삼각형 크기:'))
for i in range(1,size+1):
    for j in range(0,i):
        print('*',end='')
    print()
print()

'''
3. 크기 입력받아 삼각형 출력
    *
   **
  ***
 ****
*****
'''
size=int(input('두번째 삼각형 크기:'))
for i in range(1,size+1):
    for space in range(i,size):
        print(' ',end='')
    for star in range(0,i):
        print('*',end='')
    print()
print()

'''
4. 크기 입력받아 삼각형 출력
  *
 ***
*****
'''

size=int(input('세번째 삼각형 크기:'))
for i in range(1,size+1):
    for space in range(i,size):
        print(' ',end='')
    for star in range(1,i*2):
        print('*',end='')
    print()
print()

'''
5. 크기 입력받아 삼각형 출력
  *
 ***
*****
 ***
  *
'''
size=int(input('마름모 크기:'))
for i in range(1,size+1):
    for space in range(i,size):
        print(' ',end='')
    for star in range(1,i*2):
        print('*',end='')
    print()
for i in range(size-1,0,-1):
    for space in range(i, size):
        print(' ', end='')
    for star in range(1, i * 2):
        print('*', end='')
    print()