"""
# 메서드에서 멤버변수를 정의한 예
class Test:
    def setData(self, a, b):  # 메서드에서 멤버변수 정의
        self.a = a
        self.b = b

    def printData(self):
        print('a:', self.a)
        print('b:', self.b)

def main():
    m1 = Test()
    m1.setData(1,2)
    m1.printData()

    m2 = Test()
    m2.printData()  #멤버변수 값이 정의되지 않은 채로 메서드 사용

main()

# 에러 발생. 호출 순서에 따라 멤버변수 정의 여부가 바뀔 수 있기 때문에 가급적이면 메서드에서 멤버변수를 정의하지 않는다
"""


#모니터 재고 관리 프로그램
class Monitor:
    #생성자. 객체를 초기화하는 함수. 멤버변수 정의 및 초기와. self = 현재 객체 참조값. 모든 메서드는 첫번쨰 파라미터가 self다
    #멤버변수: 객체 소속의 변수. self 변수
    def __init__(self, model='', price=0, amount=0, size=0):
        self.model = model
        self.price = price
        self.amount = amount
        self.size = size

    def printMonitor(self):
        print('model:', self.model)
        print('price:', self.price)
        print('amount:', self.amount)
        print('size', self.size)

    #메서드 오버라이딩(overriding) => 상속받은 메서드를 수정해서 사용용
    def __str__(self):  # 객체 설명 메서드로, object로부터 상속 받음
        return 'model:'+self.model+' / price:'+str(self.price)+' / amount:'+str(self.amount)+' / size:'+str(self.size)

def main():
    '''
    m1 = Monitor('s2440', 1500, 5, 27)  # 객체 생성
    m1.printMonitor()
    print(m1)  # 객체 이름을 출력하면 그 객체의 __str__()을 호출하여 이 함수의 반환값을 출력함. __str__ :
    print(id(m1))  # id(): 객체의 참조값을 십진수로 반환 ( __str__이 반환하는 값은 16진수)

    m2 = Monitor('s2455', 2500, 5, 30)
    m2.printMonitor()
    print(m2)
    print(id(m1))

    m3 = Monitor('s3440', 4500, 8, 30)
    m3.printMonitor()
    print(m3)
    print(id(m1))

    m4 = m3
    print(m4)
    print('m4의 참조값:', id(m4))
    '''

    #이름 없이 객체를 생성하여 생성한 객체를 리스트에 추가
    monitors = []
    monitors.append(Monitor('s2440', 1500, 5, 27))
    monitors.append(Monitor('s2455', 2500, 5, 30))
    monitors.append(Monitor('s3440', 4500, 8, 30))

    #세 객체의 정보 출력
    for i in range(0, 3):
        monitors[i].printMonitor()

    for i in monitors:
        i.printMonitor()

    #현재 __str__이 바뀌어 있어서 이대로해도 출력 가능
    for i in monitors:
        print(i)



main()