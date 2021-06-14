class Member:
    def __init__(self, id='', pwd='', email=''):
        self.__id = id
        self.__pwd = pwd
        self.__email = email

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def __str__(self):  # object 클래스로부터 상속받은 메서드 재정의
        return 'id:'+self.__id+' / pwd:'+self.__pwd+' / email:'+self.__email


def main():
    m1 = Member('aaa', '111', 'aaa@email.com')
    m2 = Member('bbb', '222', 'bbb@email.com')
    m3 = Member('ccc', '333', 'ccc@email.com')

    print(m1)  # 우회접근이기 때문에 id, pwd, email 출력 가능
    print(m2)
    print(m3)

    # print('m2.a:', m2.__id)  # 에러 발생
    print('m2.a:', m2.getId())

    m1.__id = 'abc'  # 밖에서는 프라이빗 멤버인 __id가 안보이기 때문에 __id라는 멤버를 새로 생성함
    print(m1)  # 그러나 출력을 해보면 프라이빗 멤버인 __id의 값이 바뀌지 않고 유지되어 출력됨

    m1.setId('abc')  # 클래스 내에서 메소드를 설정해놔야 프라이빗 멤버의 값을 우회하여 변경 가능
    print(m1)



main()