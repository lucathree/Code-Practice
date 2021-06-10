def hello():        #파라미터 없음
    print('hello')  #리턴값 없음

hello()

#더하기 함수
def add(a,b):
    c = a+b
    return c    #계산한 결과를 되돌려줌. c는 함수 안에서만 사용가능, 함수 밖에서는 c를 호출해도 나오지 않는다.
result = add(1,2)
print(result)

def add2(a,b):
    return a+b
print(add2(2,3))

#파라미터로 단수를 받아 구구단 한단 출력 함수. 반환값 없음
def gugudan(x):
    print(f'<{x}단>')
    for i in range(1,10):
        print(x,'*',i,'=',x*i)

for i in range(2,10):
    gugudan(i)

#계산기: +,-,*,/ 따로따로 만들기. 2개의 숫자와 1개의 연산자 키보드 입력받아서 출력

def remove(a,b):
    c = a-b
    return c

def multiply(a,b):
    c = a*b
    return c

def divide(a,b):
    if b!=0:            #나누는 값이 0이면 에러가 발생하기 때문에 조건입력
        return a/b        #b에 0을 넣어서 반환된 값이 없을 때 실제로는 None이 반환됨

def calculator():
    a = int(input('숫자1:'))
    x = input('원하는 계산:')
    b = int(input('숫자2:'))
    result = None
    if x == '+':
        result = add(a,b)
    elif x == '-':
        result = remove(a,b)
    elif x == '*':
        result = multiply(a,b)
    elif x == '/':
        result = divide(a,b)

    if result == None:
        print('잘못된 입력')
    else:
        print(f'{a} {x} {b} = {result}')

calculator()


#파라미터로 숫자를 받아서 그 숫자의 약수를 출력하는 함수, 리턴값 없음

def divisor(x):
    for i in range(1,x+1):
        if x%i == 0:
            print(i, end=' ')
    print()

x = int(input('약수를 구할 수:'))
divisor(x)


#값을 리스트로 저장하는 약수 함수
def divisor2(x):
    res=[]
    for i in range(1, x+1):
        if x % i == 0:
            res.append(i)
    return res

def print_div(data):
    print(data[len(data)-1],'의 약수:', end='')
    for i in data:
        print(i, end=' ')
    print()

x = int(input('num:'))
d = divisor2(x)
print_div(d)
