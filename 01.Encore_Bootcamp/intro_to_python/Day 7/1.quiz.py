#1. 이름이 printName이고 파라미터로 문자열 하나를 받아서 간단히 받은 파라미터 값을 출력하는 함수를 정의하고 호출. 함수 리턴값 없음
#2. 파라미터로 숫자 3개를 받아서 이중 가장 큰 값을 반환하는 함수. 이름은 maxNum 함수 정의 및 호출
#3. 파라미터로 리스트 하나를 받아서 리스트에 담긴 숫자 모두의 합을 구하여 반환하는 함수를 정의 및 호출. 함수 이름은 sumNum
#4. 파라미터로 문자열 하나 숫자 하나를 받는 이름이 f1인 함수 정의. 호출시 파라미터의 순서가 바뀌어도 동작되도록 정의 및 호출하시오. 동작은 파라미터 값 출력, 리턴값은 없음.
#5. 위 f1 함수 파라미터의 기본값을 설정하시오. 문자열 파라미터의 기본값은 'aaa'. 숫자 파라미터의 기본값은 0.

#1
def printName(word):
    print(word)

printName('hello')

#2
def maxNum(a,b,c):
    max = a
    if a < b:
        max = b
        if b < c:
            max = c
    elif a < c:
        max = c
    return max

maxNum(144,3,25)

#3
def sumNum(list):
    sum = 0
    for i in list:
        sum += i
    return sum

sumNum([10,20,30,5,15,3])

'''
#4 & 5
def f1(word, num):
    word = 'aaa'
    num = 0
    if typeCheck(word) == 'str':
        text = word
        number = num
    elif typeCheck(word) == 'num':
        number = word
        text = num
    print(f'문자:{text}, 숫자:{number}')

def typeCheck(var):
    res = str(type(var))
    if res == "<class 'str'>":
        res2 = 'str'
    else:
        res2 = 'num'
    return res2
'''
#4
def f1(s,n):
    print('s:',s)
    print('n:',n)
f1(n=10, s='asdf')

#5
def f1(s='aaa', n=0):
    print('s:', s)
    print('n:', n)

f1() #기본값을 지정한 파라미터는 호출시 값 할당을 생략가능

#파라미터의 기본값이 지정된것과 지정됮 ㅣ않은것을 섞어서 쓸때 순서가 중요. 기본값 없는 파라미터가 먼저 정의되어야 함
def f1(c, a=1, b=2):
    print(a, b, c)

f1(1)
f1(1,2)