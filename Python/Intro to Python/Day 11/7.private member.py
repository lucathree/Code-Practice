#접근제어: 클래스의 멤버변수나 메서드를 외부에서 접근하는 것을 허용할지 말지 지정

class Test:
    def __init__(self):
        self.__a = 10  # private 멤버
        self.b = 20  # public 멤버

    def setData(self, a, b):
        self.__a = a
        self.b = b

    def printData(self):
        print('a:', self.__a)
        print('b:', self.b)

    def setA(self, a):  # setter - 클래스 밖에서 private member에 값을 설정하는 메서드
        self.__a = a

    def getA(self, a):  # getter - 클래스 밖으로 private 멤버 값을 반환하여 외부에서도 읽을 수 있게하는 메서드
        return self.__a


class main():
    t1 = Test()
    t1.printData()
    t1.setData(3, 4)
    t1.printData()

    t1.__a = 100  # t1 객체에 멤버변수 __a를 추가 (에러없이 작동 됨)
    t1.setA(100)
    t1.b = 200

    # print('t1.a:', t1.__a)  # 프라이빗 멤버를 밖에서 읽을 수 없기 때문에 에러 발생
    print('t1.a:', t1.getA())  #__a의 값을 읽음
    print('t1.b:', t1.b)

main()