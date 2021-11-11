import pymysql


class MenuSearchVo:
    def __init__(self, product_id=None, store_id=None, store_name=None, menu_type=None, product_name=None, product_price=0, sale_available=0):
        self.product_id = product_id
        self.store_id = store_id
        self.store_name = store_name
        self.menu_type = menu_type
        self.product_name = product_name
        self.product_price = product_price
        self.sale_available = sale_available

    def __str__(self):
        return '상품 id:{}, / 가게 id:{}, / 가게이름:{}, / 가게분류: {}, / 상품이름:{}, / 상품가격:{}, / 판매가능:{}'.format(
            self.product_id, self.store_id, self.store_name, self.menu_type, self.product_name, self.product_price, self.sale_available
        )


class MenuSearchDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234',
                                    db='coupangeats_project', charset='utf8')

    def disconnect(self):
        self.conn.close()

    # 음식 타입으로 검색

    def selectByType(self, menu_type):
        list = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'select p.product_id, p.store_id, s.store_name, s.type, p.product_name, p.product_price, p.sale_available \
              from products p join stores s using (store_id) where s.type=%s'
        vals = (menu_type, )

        try:
            cur.execute(sql, vals)  # 여러 개의 검색결과를 cur 객체에 담음
            for row in cur:
                list.append(MenuSearchVo(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            return list
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 이름 키워드 입력받아 그 키워드를 포함하는 모든 상품 검색
    def selectByName(self, product_name):
        list = []
        self.connect()
        cur = self.conn.cursor()
        product_name = '%' + product_name + '%'
        sql = 'select p.product_id, p.store_id, s.store_name, s.type, p.product_name, p.product_price, p.sale_available \
              from products p join stores s using (store_id) where p.product_name like %s'
        vals = (product_name,)

        try:
            cur.execute(sql, vals)  # 여러 개의 검색결과를 cur 객체에 담음
            for row in cur:
                list.append(MenuSearchVo(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            return list
        except Exception as e:
            print(e)
        finally:
            self.disconnect()


class MenuSearchService:
    def __init__(self):
        self.dao = MenuSearchDao()

    # 음식분류로 검색
    def getByType(self):
        print('음식종류로 검색')
        menu_type = input('음식분류(ex.한식):')
        '''나중에 음식분류 값이 제한되면 입력값이 해당 제한에 걸리지 않는지 체크하는 코드 필요'''
        vo_list = self.dao.selectByType(menu_type)
        self.printList(vo_list)

    # 음식이름으로 검색
    def getByName(self):
        print('음식이름으로 검색')
        product_name = input('음식이름 or 키워드:')
        vo_list = self.dao.selectByName(product_name)
        self.printList(vo_list)

    # 반복되는 기능 메서드화
    def printList(self, vo_list):
        if vo_list == None or len(vo_list) == 0:
            print('검색결과 없음')
        else:
            for i in vo_list:
                print(i)
