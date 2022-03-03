class Product:
    def __init__(self, id=0, name='', price=0, amount=0):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return 'id:'+str(self.id)+' / name:'+self.name+' / price:'+str(self.price)+' / amount:'+str(self.amount)


class StoreDao:
    def __init__(self):
        self.prods = []

    def create(self, p):
        return self.prods.append(p)

    def read(self, id):
        for i in self.prods:
            if i.id == id:
                return i

    def readAll(self):
        return self.prods

    def delete(self, p):
        return self.prods.remove(p)


class StorageService:
    def __init__(self):
        self.dao = StoreDao()

    def addProd(self):
        id = Menu.cnt
        name = input('제품명:')
        price = int(input('가격:'))
        amount = int(input('수량:'))
        p = Product(id, name, price, amount)
        return self.dao.create(p)

    def searchProd(self):
        id = int(input('검색할 제품번호:'))
        p = self.dao.read(id)
        if p == None:
            print("제품을 찾을 수 없습니다.")
        else:
            print(p)

    def editProd(self):
        id = int(input('수정할 제품번호:'))
        p = self.dao.read(id)
        if p == None:
            print("제품을 찾을 수 없습니다.")
        else:
            p.price = int(input('수정할 가격:'))
            p.amount = int(input('수정할 수량:'))
            print('수정완료:', p)

    def delProd(self):
        id = int(input('삭제할 제품번호:'))
        p = self.dao.read(id)
        if p == None:
            print("제품을 찾을 수 없습니다.")
        else:
            self.dao.delete(p)

    def printAll(self):
        list = self.dao.readAll()
        for i in list:
            print(i)



class Menu:
    cnt = 0
    def __init__(self):
        self.service = StorageService()

    def run(self):
        while True:
            s = int(input('1.등록 2.검색 3.수정 4.삭제 5.전체출력 6.종료'))
            if s == 1:
                Menu.cnt += 1
                self.service.addProd()
            elif s == 2:
                self.service.searchProd()
            elif s == 3:
                self.service.editProd()
            elif s == 4:
                self.service.delProd()
            elif s == 5:
                self.service.printAll()
            elif s == 6:
                break


def main():
    m = Menu()
    m.run()


main()


