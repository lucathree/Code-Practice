def f1():
    print('f1()')
    print('a:',a)
    #print('b:',b)  #b는 f1() 호출한 뒤에 정의하기 때문에 f1()함수에서 안보임
    #print('c:',c)  #c는 f1() 호출한 뒤에 정의하기 때문에 f1()함수에서 안보임

def f2():
    print('f2()')
    print('a:',a)
    print('b:',b)
    #print('c:',c)  #c는 f2() 호출한 뒤에 정의하기 때문에 f2()함수에서 안보임

def f3():
    print('f3()')
    print('a:',a)
    print('b:',b)
    print('c:',c)

a=10  #전역변수

f1()

b=20  #전역변수

f2()

c=30  #전역변수

f3()