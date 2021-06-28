import pymysql

# type없음
import project1.memModel as mem  # 같은폴더 내, '폴더명.파일이름'


class ProductVo:
    def __init__(self, product_id=None, store_id=None, product_name=None, product_price=0, sale_available=0):
        self.product_id = product_id
        self.store_id = store_id
        self.product_name = product_name
        self.product_price = product_price
        self.sale_available = sale_available

    def __str__(self):
        return '상품 id:{}, / 가게 id:{}, / 상품 이름:{}, / 상품 가격:{}, / 판매가능여부:{}'.format(
            self.product_id, self.store_id, self.product_name, self.product_price, self.sale_available
        )


class ProductDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234',
                                    db='coupangeats_project', charset='utf8')

    def disconnect(self):
        self.conn.close()

    # 상품 입력
    def insertProd(self, vo):
        self.connect()
        cur = self.conn.cursor()
        sql = 'insert into products(store_id, product_name, product_price, sale_available) \
            values(%s, %s, %s, %s)'
        vals = (vo.store_id, vo.product_name,
                vo.product_price, vo.sale_available)

        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    '''접속한 아이디가 보유한 가게가 맞는지 확인하는 절차(1)'''

    # 가게id를 받아 해당하는 가게정보 레코드를 반환하는 함수(이거도 태현님 코드에 있을듯)
    def selectByStoreID(self, store_id):
        self.connect()
        cur = self.conn.cursor()
        sql = "select manager_id from stores where store_id=%s"
        vals = (store_id,)
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()    # 고유한 가게id는 하나의 레코드만 나올 것이기 때문에 '1줄'씩 읽어도 좋다.(fetchone)
            if row != None:  # 검색결과가 있으면
                return row[0]  # row = [manager_id] 이므로 manager_id 값만 반환해준다.
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    '''입력한 상품 id에 해당하는 상품이 속한 가게가 자신의 가게의 것인지 확인하는 절차(2)'''

    # product_id => ProductVo.store_id => selectByStoreID(self, store_id) => manager_id
    def selectByProdID(self, product_id):
        self.connect()
        cur = self.conn.cursor()
        sql = "select * from products where product_id=%s"
        vals = (product_id,)
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()
            if row != None:  # 검색결과가 있으면
                # row[1] = store_id
                return ProductVo(row[0], row[1], row[2], row[3], row[4])
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 상품id를 받아 그 상품 수정(이름, 가격정보)

    def updateProd(self, product_id, new_product_name, new_product_price, new_sale_available):
        self.connect()
        cur = self.conn.cursor()
        sql = "update products set product_name=%s, product_price=%s, sale_available=%s where product_id = %s"
        vals = (new_product_name, new_product_price,
                new_sale_available, product_id)
        try:
            line = cur.execute(sql, vals)
            self.conn.commit()
            return line  # 변경 된 line 수를 반환.
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 상품id를 받아 그 상품 삭제

    def deleteProd(self, product_id):
        self.connect()
        cur = self.conn.cursor()
        sql = "delete from products where product_id=%s"
        vals = (product_id,)
        try:
            # execute: sql문을 적용(쓰기)하고 그 적용된 줄 수를 반환하는 함수
            line = cur.execute(sql, vals)
            self.conn.commit()
            # 삭제된 줄 수를 반환(선택사항, 어차피 product_id는 고유하므로 1개의 레코드만 삭제될 것)
            return line
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 상품 모두 출력을 위한 모든목록 선택

    def checkAll(self):
        stores = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from products \
            where store_id = any (select store_id from stores  where manager_id = %s)'
        vals = (mem.MemService.login_id,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                stores.append(
                    ProductVo(row[0], row[1], row[2], row[3], row[4]))
            return stores
        except Exception as e:
            print(e)
        finally:
            self.disconnect()


class ProductService:
    def __init__(self):
        self.dao = ProductDao()

    # 상품추가하기
    def addProduct(self):
        print('음식메뉴추가')
        store_id = input('메뉴를 추가하고 싶은 가게id 입력:')
        manager_id = self.dao.selectByStoreID(store_id)

        if mem.MemService.login_id != manager_id:
            print('당신이 보유한 가게가 아닙니다.')
        else:
            product_name = input('추가하고 싶은 음식이름:')
            product_price = int(input('그 음식의 가격:'))
            while True:
                sale_available = int(input('음식판매가능여부설정(판매가능:1, 판매불가능:0):'))
                if sale_available == 0 or sale_available == 1:  # 0과 1만 입력 가능하므로, 다른 입력값 받으면 다시 입력받도록 함
                    break
                else:
                    print('0또는 1만 입력 가능합니다. 다시 입력하세요.')

            self.dao.insertProd(ProductVo(store_id=store_id, product_name=product_name,
                                          product_price=product_price, sale_available=sale_available))
            print('상품이 정상적으로 추가되었습니다.')

    # 상품정보변경(상품이름, 가격, 판매가능여부 변경)

    def editProduct(self):
        print('상품수정')
        product_id = int(input('수정하고 싶은 상품id'))
        '''입력한 그 상품이 자신의 가게의 것인지 확인하는 절차(2)'''
        vo = self.dao.selectByProdID(product_id)    # ProductVo type
        manager_id = self.dao.selectByStoreID(vo.store_id)
        if mem.MemService.login_id != manager_id:
            print('당신이 보유한 가게의 상품이 아닙니다.')
        else:
            new_product_name = input('new product_name:')
            new_product_price = int(input('new product_price:'))
            while True:
                new_sale_available = int(input('음식판매가능여부변경(판매가능:1, 판매불가능:0):'))
                if new_sale_available == 0 or new_sale_available == 1:  # 0과 1만 입력 가능하므로, 다른 입력값 받으면 다시 입력받도록 함
                    break
                else:
                    print('0또는 1만 입력 가능합니다. 다시 입력하세요.')

            line = self.dao.updateProd(
                product_id, new_product_name, new_product_price, new_sale_available)
            print(line, "개의 메뉴정보가 성공적으로 수정되었습니다.")

    # 상품삭제

    def delProduct(self):
        print('상품삭제')
        product_id = int(input('삭제할 상품id:'))
        '''입력한 그 상품이 자신의 가게의 것인지 확인하는 절차(2)'''
        vo = self.dao.selectByProdID(product_id)  # ProductVo type
        manager_id = self.dao.selectByStoreID(vo.store_id)
        if mem.MemService.login_id != manager_id:
            print('당신이 보유한 가게의 상품이 아닙니다.')
        else:
            line = self.dao.deleteProd(product_id)
            print(line, "개이 메뉴정보가 성공적으로 삭제되었습니다.")

    # 상품확인 출력
    def printAll(self):
        print('내 모든 가게 및 메뉴 확인')
        products = self.dao.checkAll()
        for pro in products:
            print(pro)
