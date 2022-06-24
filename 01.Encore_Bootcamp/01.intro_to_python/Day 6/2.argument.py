#인자 = argument
#요구인자 = ?
'''
def f1(name, tel, age):
    print('name:',name)
    print('tel:',tel)
    print('10년 후 age:', age+10)

def main():
    n = 'aaa'
    t = '1234'
    a = 12
    f1(n,t,a)
    #f1(a,n,t) 값을 순서대로 넣어주지 않고 뒤죽박죽 넣으면 에러가 발생한다

    #하지만 키워드인자를 사용하면 순서가 뒤바뀌어도 문제없다
    f1(tel=t, age=a, name=n)
    f1(n, t)

main()


def f1(name, tel, age=5):   #인자값을 미리 지정
    print('name:',name)
    print('tel:',tel)
    print('10년 후 age:', age+10)

def main():
    n = 'aaa'
    t = '1234'
    f1(n,t) #age 값이 미리 지정되어 있기 때문에 두개의 인자만 제공해도 에러가 발생하지 않는다

main()
'''

#가변인자
def f1(*x): #가변인자, 튜플로 받아옴
    print('함수시작')
    for i in x:
        print(i)
    print('함수끝')

def add(*nums):
    s = 0
    for i in nums:
        s+=i
    return s

def main():
    f1('aaa','bbb')
    f1('ccc','ddd','eee','fff')

    s = add(1,2,3)
    print('add(1,2,3):',s)
    s = add(1,2,3,4,5)
    print('add(1,2,3,4,5):',s)

main()