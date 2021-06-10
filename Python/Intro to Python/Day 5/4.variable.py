#지역변수(지역구): 함수 내에서 선언. 그 함수 내에서만 사용가능
#전역변수(전국구): 함수 밖에 선언. 이 파일 내에서 모든 함수에서 사용가능
num=10  #전역변수
def f1():
    num=20  #변수이름은 전역변수와 같아도 함수 안에서 선언되면 지역변수
    print('f1:',num)

def f2():
    x=5   #지역변수
    print('f2 x:',x)
    print('f2 num:',num)

def f3():
    global num  #전역변수로 지정
    num=20      #전역변수 값 변경
    print('f3:', num)

def main():
    print('main num:', num)  #전역변수 호출
    #print('main x:',x)     다른 함수의 지역변수 사용불가
    f1()
    f2()
    print('main num:',num)   #전역변수 호출. f1함수가 실행되었어도 f1함수의 num은 지역변수로 f1 안에서만 호출됨
    f3()
    print('main num:', num)

main()


#자, 이제 피카츄 게임을 함수를 써서 만들어보자!