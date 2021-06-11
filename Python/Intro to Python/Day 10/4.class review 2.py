#모니터 재고 관리 프로그램
class Monitor:  # VO
    def __init__(self, model='', price=0, amount=0, size=0):
        self.model = model
        self.price = price
        self.amount = amount
        self.size = size

    def __str__(self):
        return 'model:'+self.model+' / price:'+str(self.price)+' / amount:'+str(self.amount)+' / size:'+str(self.size)

# DAO + Service / 기능 및 저장작업
# 필요한 기능: 등록, 검색, 전체출력

class MonitorService:
    def __init__(self):
        self.monitors = []  # 이 객체의 다수 메서드가 사용하는 값. 멤버 변수는 클래스 안에서 전역으로 사용하는 변수

    def addMonitor(self):
        model = input('model:')
        price = int(input('price:'))
        amount = int(input('amount:'))
        size = int(input('size:'))
        mo = Monitor(model, price, amount, size)  # 방금 입력받은 데이터를 묶어서 Monitor 객체 생성 (Service 안에서 VO 사용)
        return self.monitors.append(mo)

    def getMonitor1(self):
        flag = True
        name = input('search model:')
        for i in self.monitors:
            if i.model == name:
                print(i)
                flag = False
                break
        if flag:
            print("couldn't find model")

    def getMonitor2(self, model):
        for i in self.monitors:
            if i.model == model:
                return i

    def printMonitor(self):
        name = input('search model:')
        mo = self.getMonitor2(name)
        if mo == None:
            print("couldn't find model")
        else:
            print(mo)

    def editMonitor1(self):
        flag = True
        name = input('search model:')
        for i in self.monitors:
            if i.model == name:
                i.price = input('edit price:')
                i.amount = input('edit amount:')
                print('수정완료:',i)
                flag = False
                break
        if flag:
            print("couldn't find model")

    def editMonitor2(self):
        name = input('search model:')
        mo = self.getMonitor2(name)
        if mo == None:
            print("couldn't find model. edit canceled")
        else:
            mo.price = input('edit price:')
            mo.amount = input('edit amount:')
            print('수정완료:', mo)

    def delMonitor(self):
        name = input('search model:')
        mo = self.getMonitor2(name)
        if mo == None:
            print("couldn't find model. delete canceled")
        else:
            self.monitors.remove(mo)

    def printAll(self):
        for i in self.monitors:
            print(i)


# 메뉴 클래스는 메뉴 돌려줄 메서드 하나만 있으면 됨
# 메뉴에서 기능을 선택해서 실행하려면 기능을 제공해주는 서비스 객체 필요. MonitorService를 멤버변수로 생성
class Menu:
    def __init__(self):
        self.service = MonitorService()

    def run(self):
        while True:
            m = int(input('1.모니터등록 2.검색 3.수정 4.삭제 5.전체출력 6.종료'))
            if m == 1:
                self.service.addMonitor()
            elif m == 2:
                self.service.printMonitor()
            elif m == 3:
                self.service.editMonitor2()
            elif m == 4:
                self.service.delMonitor()
            elif m == 5:
                self.service.printAll()
            elif m == 6:
                break


def main():
    m = Menu()
    m.run()

main()