#파이썬 클래스 특징
#정적멤버변수, 정적메서드
class Test:
    x = 0   # 클래스 변수. 정적 멤버 변수. 정적메모리(static)에 저장. 이 클래스로 만든 모든 객체가 공용으로 사용
    def __init__(self):
        self.y = 0      # 일반 멤버변수. 앞에 self.를 꼭 붙인다. 이 멤버변수는 self객체 소속

    def printXY(self):
        print('x:', Test.x)
        print('y:', self.y)


def main():
    t1 = Test()
    Test.x += 1
    t1.y += 1
    t1.printXY()

    t2 = Test()
    Test.x += 1
    t2.y += 1
    t2.printXY()

    t3 = Test()
    Test.x += 1
    t3.y += 1
    t3.printXY()


main()