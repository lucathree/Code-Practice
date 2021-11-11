import pymysql
import project1.memModel as mem
import project1.productModel as p

'''주요 수정사항
1. StoreVo는 궁극적으로는 stores table의 모든 컬럼값을 담을 수 있도록 설정해야, 나중에 정보를 출력할 때 모든 정보를 출력할 수 있어 적절합니다.
그래서 아래처럼 store_id와 avg_score 변수를 추가했고, 이후에 원하는 값들만 빼서 활용하면 됩니다.

2. sql문에서 table명이 전부 달랐습니다. 예를 들어 가게정보를 담은 테이블 이름은 store가 아닌 store's'였습니다.
디테일한 부분 신경 써주시면 좋을 거 같습니다.

3. 가게 말고 '상품 출력'의 경우 product 테이블의 값을 가져와야 하므로, 다른 파일에 있는 ProductVo(productModel.py에서 정의됨)을 import하여 사용했습니다.
'''


class StoreVo:
    def __init__(self, store_id=None, manager_id=None, store_name=None, type=None, location=None, deleveryfee=None, avg_score=None):
        self.store_id = store_id
        self.manager_id = manager_id
        self.store_name = store_name
        self.type = type
        self.location = location
        self.deleveryfee = deleveryfee
        self.avg_score = avg_score

    def __str__(self):
        return ('가게 id:' + str(self.store_id) + ' / 회원 id:' + self.manager_id + ' / 가게이름:' + self.store_name + ' / 가게분류:' + self.type +
                ' / 배송지역:' + self.location + ' / 배달비:' + str(self.deleveryfee) + ' / 평점:' + str(self.avg_score))


class StoreDao:                     # (수정) 클래스명은 관행적으로 대문자로 시작합니다.
    def __init__(self):
        self.conn = None
        # self.memser = mem.MemService()
        # self.sto_id = StoreVo()

    def connect(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='1234', db='Coupangeats_project', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, vo):
        self.connect()
        cur = self.conn.cursor()
        # (수정) 테이블명
        sql = 'insert into stores(manager_id, store_name, type, location, deleveryfee) values( %s, %s, %s ,%s , %s )'
        # (수정) 파라미터로 받아온 vo객체의 변수들을 sql문에 대입하기 위해 튜플을 정의해야 합니다.
        vals = (vo.manager_id, vo.store_name,
                vo.type, vo.location, vo.deleveryfee)
        try:
            cur.execute(sql, vals)  # (수정) 위의 sql에 vals 튜플의 값들을 대입해서 실행합니다.
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def select(self, id):
        self.connect()
        cur = self.conn.cursor()
        # (수정) 테이블명 (store -> stores), 포맷문자 변경(%d -> %s)
        sql = 'select * from stores where store_id=%s'
        vals = (id,)
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()
            if row != None:
                # (수정) 마지막에 콤마를 붙일 필요가 없습니다.(이건 튜플이 아니고, 새로 정의한 StoreVo 타입의 객체입니다.)
                vo = StoreVo(row[0], row[1], row[2], row[3], row[4])
                return vo
        except Exception as e:
            print(e)
        finally:
            self.disconnect()
            # print(vo)     (삭제) 이미 위에서 return 했으므로 아랫줄인 이 코드는 작동이 되지 않습니다.
    '''
    def check(self,id):
        pass
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from stores where Manager_id=%s'
        vals = (id,)
        if self.member.login_id == self.sto_id.manager_id:
            pass
    '''

    def delete(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'delete from stores where store_id = %s'
        vals = (id,)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 자신이 보유 중인 가게들의 모든 상품들을 확인
    def selectAllProducts(self, member_id):     # (수정) 입력 파라미터가 로그인 된 멤버id 입니다.
        list = []                       # (추가) 상품 목록을 담을 리스트를 만듭니다.
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from products as p \
            join stores as s \
            on p.store_id=s.store_id \
            where s.manager_id = %s'            # (수정) 로그인 된 아이디 = 매니저 id인(즉, 자신이 보유한) 모든 가게들의 상품정보 전부를 선택하는 sql문
        vals = (member_id,)
        try:
            cur.execute(sql, vals)
            # 검색결과가 여러줄이므로 fetchone을 쓸 필요가 없다.
            for row in cur:
                # 검색한 테이블이 products 테이블이므로 이에 맞는 VO 객체를 가져옴
                list.append(p.ProductVo(
                    row[0], row[1], row[2], row[3], row[4]))
            return list                           # 반환값은 검색결과 전체인 리스트가 되어야 한다.
            # print(vo)
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 점포 전체 선택

    def selectAll(self):
        stores = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from stores'
        try:
            cur.execute(sql)
            for row in cur:
                stores.append(
                    StoreVo(row[0], row[1], row[2],
                            row[3], row[4], row[5], row[6])
                )
            return stores
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectMyStores(self, member_id):
        list = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from stores where manager_id=%s'
        vals = (member_id,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                # stores 테이블에 있는 7개의 값을 모두 보여주어야 하므로
                list.append(
                    StoreVo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            return list
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def checkStore(self, member_id):
        list = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from stores where manager_id=%s'
        vals = (member_id,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                list.append(row[0])  # stores 테이블에 있는 7개의 값을 모두 보여주어야 하므로
            return list
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def getPwd(self, store_id):  # (수정) 가게의 pwd가 아닌, 가게 주인 계정의 pwd를 반환하는 메서드이므로 이름을 변경
        self.connect()
        cur = self.conn.cursor()
        sql = 'SELECT member_id, store_id, pwd ' \
              'from members m ' \
              'join stores s ' \
              'on m.member_id = s.manager_id ' \
              'where store_id = %s'
        vals = (store_id,)
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()
            if row != None:
                # print(row[2])
                return row[2]
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 점포 이름 받아서 선택
    def selectByStoreName(self, store_name):
        stores = []
        self.connect()
        cur = self.conn.cursor()

        store_name = "%{}%".format(store_name)
        sql = 'select * from stores where store_name like %s'
        vals = (store_name,)
        try:
            cur.execute(sql, vals)

            # row = cur.fetchone()
            # if row != None:  # 검색결과가 있으면
            for row in cur:
                stores.append(
                    StoreVo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                return stores
        except Exception as e:
            print(e)
        finally:
            self.disconnect()


class StoreService:                 # (수정) 클래스명은 관행적으로 대문자로 시작합니다.
    def __init__(self):
        self.dao = StoreDao()
        # self.memser = mem.MemService() 아래에서 그냥 그대로 mem.MemService.login_id를 사용하므로 굳이 멤버변수를 만들 필요는 없습니다.
        # self.sto_id = StoreVo()

    # (수정) 로그인된 id를 manager_id로 자동으로 대입되도록 바꿨습니다.
    def addStore(self):
        print('신규 점포를 등록합니다')
        member_id = mem.MemService.login_id
        name = input('점포이름:')
        type = input('판매음식종류:')
        location = input('점포위치:')
        deleveryfee = input('배달비:')
        self.dao.insert(StoreVo(manager_id=member_id, store_name=name,
                        type=type, location=location, deleveryfee=deleveryfee))
        print('점포등록완료')

    def delStore(self):
        print('점포등록 취소')
        store_id = int(input('삭제할 점포ID:'))
        a = self.dao.checkStore(mem.MemService.login_id)

        if store_id not in a:
            print('회원님이 보유한 점포가 아닙니다.')
        else:
            pwd = int(input('본인확인절차: 비밀번호를 입력해주세요:'))
            real_pwd = self.dao.getPwd(store_id)
            if pwd == real_pwd:
                self.dao.delete(store_id)
                print('해당 점포가 삭제되었습니다.')
            else:
                print('비밀번호를 틀리셨습니다.')

    def printMyStore(self):
        print('내 가게 목록')
        store_list = self.dao.selectMyStores(mem.MemService.login_id)
        if store_list == None:
            print('등록된 점포 없음')
        else:
            for i in store_list:
                print(i)

        print('내 상품 목록')
        product_list = self.dao.selectAllProducts(mem.MemService.login_id)
        if product_list == None:
            print('등록된 상품 없음')
        else:
            for i in product_list:
                print(i)

    # 점포명으로 검색
    def getByStore(self):
        print('‘점포명으로 검색’')
        store_name = input('점포명:')
        vo_list = self.dao.selectByStoreName(store_name)
        self.printList(vo_list)
        # print(vo_list)

    # 점포 전체 출력

    def getStores(self):
        print('점포 전체 목록')
        stores = self.dao.selectAll()
        for s in stores:
            print(s)

    # 출력 기능
    def printList(self, vo_list):
        if vo_list == None or len(vo_list) == 0:
            print('검색 결과 없음')
        else:
            for s in vo_list:
                print(s)
