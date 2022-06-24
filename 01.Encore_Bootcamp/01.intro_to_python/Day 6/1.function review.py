'''
#함수의 파라미터로 immutable한 값 전달의 예
#immutable(값 변경 안되는 요소, 상수). int, str, float, bool, tuple
def f1(num, name):
    print('f1에서 변경전')
    print('num:',num)
    print('name:',name)
    num = 123
    name = 'asf'
    print('f1에서 변경후')
    print('num:',num)
    print('name:',name)

def main():
    num = 10
    name = 'aaa'
    print('main에서 변경전')
    print('num:',num)
    print('name:',name)
    f1(num,name)
    print('main에서 변경후')
    print('num:',num)
    print('name:',name)

main()
'''

#함수의 파라미터로 mutable한 값 전달의 예
#mutable: 변경되는 값, 리스트, 셋, 딕셔너리
def f1(arr):
    print('f1안에서 변경전:',arr)
    arr[0]=100
    print('f1안에서 변경후:',arr)

def main():
    x = [1,2,3,4,5]
    print('main 변경전:',x)
    f1(x)                   #x의 참조값을 f1함수에 전달. 
    print('main 변경후:',x)

main()
