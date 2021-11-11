#다형성 구현 -> 한 코드가 다양한 형태로 실행되는 것
class Car:
    def __init__(self):
        name = ''

    def horn(self):
        print('자동차 빵빵')


class Firetruck(Car):
    def __init__(self):
        super().__init__()
        self.name = '소방차'

    def horn(self):
        print('불꺼~~~')


class Ambulance(Car):
    def __init__(self):
        super().__init__()
        self.name = '구급차'

    def horn(self):
        print('삐뽀삐뽀')


class Popo(Car):
    def __init__(self):
        super().__init__()
        self.name = '경찰차'

    def horn(self):
        print('잡았다 요놈!')


def main():
    obj = None
    print('자동차를 선택하시오')
    s = input('1.소방차 2.구급차 3.경찰차')
    if s == '1':
        obj = Firetruck()
    elif s == '2':
        obj = Ambulance()
    elif s == '3':
        obj = Popo()
    else:
        obj = Firetruck()

    print(obj.name)
    obj.horn()

main()