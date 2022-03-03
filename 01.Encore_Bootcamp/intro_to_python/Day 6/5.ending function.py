#return
#return: 함수종료
#return 값: 값을 반환하고 함수 종료

def f1():
    while True:
        menu = input('숫자 입력, 멈추려면 0을 입력하세요')
        print('입력값:',menu)
        if menu=='0':
            return  #함수종료

def f2(name):
    return '당신의 이름은 '+name  #문자열 반환

def f3():
    print('test f3')  #함수에서 반환값이 없으면 자동으로 None이 반환된다

def main():
    res = f1()
    print('f1의 리턴값:',res)
    res = f2('aaa')
    print('f2의 리턴값:',res)
    res = f3()
    print('f3의 리턴값:',res)

main()


