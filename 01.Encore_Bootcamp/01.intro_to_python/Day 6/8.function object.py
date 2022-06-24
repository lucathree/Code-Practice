#함수객체(function object)

'''
#함수를 변수에 담음
def f1(name):
    print(name,'hello')

def main():
    #obj => 함수 객체
    obj = f1    #함수이름에는 함수 참조값이 있다
    obj('aaa')

main()


#핸들러로 활용하는 경우
def onEvent(f):
    print('이벤트 등록')
    f()  #함수 객체로 함수 대신 호출

def handler():
    print('3의 배수')

def main():
    for i in range(1,100):
        print(i)
        if i%3==0:
            onEvent(handler)

main()
'''

#룩업테이블(리스트)
def 밥먹기():
    print('피카츄 밥먹음')

def 놀기():
    print('피카츄 놀음')

def 잠자기():
    print('피카츄 잠')

def 운동하기():
    print('피카츄 운동함')

def main():
    funcs = [밥먹기, 놀기, 잠자기, 운동하기]
    menu = int(input('1.밥 2.놀 3.잠 4.운동'))
    funcs[menu-1]()

main()