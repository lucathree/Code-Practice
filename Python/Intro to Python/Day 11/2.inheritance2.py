class Parent:
    def __init__(self):
        self.a = 10
        print('Parent 생성자')

    def method1(self):
        print('메서드1')

class Child(Parent):
    def __init__(self):
        super().__init__()
        print('child 생성자')
        self.b = 20  #멤버변수는 a, b 2개

    def method2(self):  #메서드 method1, method2 2개
        print('메서드2')

class Child2(Parent):
    def __init__(self):
        super().__init__()
        print('child2 생성자')
        self.c = 20
        self.d = 40  # 멤버변수는 a, c, d 3개

    def method3(self):  # 메서드 mehthod1, method3 2개
        print('메서드3')

def main():
    c1 = Child()
    print('c1.a:', c1.a)
    print('c1.b:', c1.b)

    c1.method1()
    c1.method2()

    c2 = Child2()
    print('c2.a:', c2.a)
    print('c2.c:', c2.c)
    print('c2.d:', c2.d)

    c2.method1()
    c2.method3()


main()