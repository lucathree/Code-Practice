class Product:
    def __init__(self, id=0, name='', price=0, amount=0):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return 'id:' + str(self.id) + ' / name:' + self.name + ' / price:' + str(self.price) + ' / amount:' + str(self.amount)


def main():
    prods = []
    for i in range(0, 5):
        id = int(input('제품번호:'))
        name = input('제품명:')
        price = int(input('가격:'))
        amount = int(input('수량:'))
        prods.append(Product(id, name, price, amount))
    for i in prods:
        print(i)


main()


