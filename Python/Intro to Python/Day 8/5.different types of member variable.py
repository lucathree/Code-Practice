class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def printPoint(self):
        print('좌표:(', self.x, ',', self.y, ')')


class Test:
    def __init__(self):
        self.num = 0
        self.s = ''
        self.arr = []
        self.point = None

    def printData(self):
        print(f'num:{self.num}')
        print(f's:{self.s}')
        print(f'arr:{self.arr}')
        self.point.printPoint()


def main():
    t1 = Test()
    t1.num = 10
    t1.s = 'hello class'
    t1.arr.append(1)
    t1.arr.append(2)
    t1.arr.append(3)
    t1.point = Point(3, 4)
    print(t1.point.x)
    print(t1.point.y)
    t1.point.x = 20
    t1.point.y = 30
    print(t1.point)
    t1.printData()


main()