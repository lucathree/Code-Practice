"""
#클래스 Person 정의 - 이름, 나이 저장. 기능 출력
#객체 2개 생성

class Person:
    def __init__(self):  # 생성자는 아무때나 호출 못하고 생성할 때 한 번만 호출됨
        self.name = ''
        self.age = 0

    def setData(self, name='홍길동', age=5):  # 언제든 값을 수정할 수 있도록 세팅하면
        self.name = name
        self.age = age

    def printData(self):
        print('name:', self.name, '\t', 'age:', self.age)


def main():
    s1 = Person()  # 생성자 호출은 클래스명() -> 객체가 사용할 메모리를 할당받아서 그 참조값을 반환
    s1.setData('홍찰찰', 27)  # 반환받은 참조값을 변수 s1에 저장한 상태. s1.멤버변수, s1.메서드() 사용가능

    s2 = Person()
    s2.name = '김뱡뱡'
    s2.age = 34

    s3 = Person()
    s3.setData()

    s4 = Person()

    s1.printData()
    s2.printData()
    s3.printData()
    s4.printData()

    people = []

    for i in range(0, 3):
        people.append(Person())  #이렇게 하면 굳이 people[i] = Person() 이라고 매번 정의하지 않아도 people[i] 의 값으로 객체가 들어가진다.

main()
"""


# 숫자 리스트를 다루는 클래스
class Number:
    def __init__(self, arr):
        self.arr = arr  # 멤버 변수는 클래스 내에서 전역변수. 클래스 안의 모든 메서드가 사용 가능

    def listSum(self):
        s = 0
        for i in self.arr:
            s += i
        return s

    def listAvg(self):
        s = self.listSum()
        return s / len(self.arr)


def main():
    n1 = Number([1, 2, 3, 4, 5])
    print(n1.listSum())
    print(n1.listAvg())


main()
