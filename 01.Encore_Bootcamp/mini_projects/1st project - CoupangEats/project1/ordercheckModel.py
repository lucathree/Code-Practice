import pymysql
import project1.memModel as mem


class OrdersVo:
    def __init__(self, order_id=None, member_id=None, store_id=None, total_price=None, order_time=None, destination=None, reception_status=None):
        self.order_id = order_id
        self.member_id = member_id
        self.store_id = store_id
        self.total_price = total_price
        self.order_time = order_time
        self.destination = destination
        self.reception_status = reception_status

    def __str__(self):
        return "가게ID:"+str(self.store_id)+" / 주문번호:"+str(self.order_id)+" / 주문자:"+self.member_id+" / 주문금액:"\
               + str(self.total_price)+" / 배송지:"+self.destination+" / 주문일시:" + \
            str(self.order_time) + " / 주문상태:"+str(self.reception_status)


class OrderDetailsVo:
    def __init__(self, orderdetail_id=None, order_id=None, product_id=None, product_name=None, count=None, orderdetail_price=None):
        self.orderdetail_id = orderdetail_id
        self.order_id = order_id
        self.product_id = product_id
        self.product_name = product_name
        self.count = count
        self.orderdetail_price = orderdetail_price

    def __str__(self):
        return '상품명:'+self.product_name+' / 주문수량:'+str(self.count) + ' / 상품금액:'+str(self.orderdetail_price)


class OrdercheckDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='1234', db='coupangeats_project', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def selectStoreOrder(self, store_id):  # 점포별 전체 주문 읽기
        orders = []  # 검색 결과를 담을 리스트
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from orders where store_id = %s'  # orders 테이블에서 store_id 로 검색
        vals = (store_id,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                # 검색결과를 order객체로 담아 리스트에 추가
                orders.append(
                    OrdersVo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            return orders  # 리스트 반환
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectOrderByStatus(self, store_id):  # 점포별 미확인 주문 읽기
        orders = []  # 검색 결과 담을 리스트
        self.connect()
        cur = self.conn.cursor()
        # orders 테이블에서 주문상태 값이 0인 주문들을 store_id 로 검색
        sql = 'select * from orders where reception_status = 0 and store_id = %s'
        vals = (store_id,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                # 검색결과를 order객체로 담아 리스트에 추가
                orders.append(
                    OrdersVo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            return orders  # 리스트 반환
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def editOrderStatus(self, order_id):  # 미확인 주문의 상태 수정
        self.connect()
        cur = self.conn.cursor()
        # 주문id가 일치하는 주문의 주문상태를 1로 수정
        sql = 'update orders set reception_status = 1 where order_id = %s'
        vals = (order_id,)
        try:
            cur.execute(sql, vals)  # 커서객체 실행
            self.conn.commit()  # 수정내용 커밋
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectOrderDetail(self, order_id):  # 상세 주문정보 읽기
        details = []  # 상세주문정보를 담을 리스트 생성
        self.connect()
        cur = self.conn.cursor()
        sql = 'select orderdetail_id, order_id, product_id, product_name, count, orderdetail_price ' \
              'from order_details ' \
              'join products ' \
              'using (product_id)' \
              'where order_id = %s'  # order_details 테이블에서 주문번호가 일치하는 상세주문내역 검색
        vals = (order_id,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                # 검색결과를 OrderDetail 객체로 담아 리스트에 추가
                details.append(OrderDetailsVo(
                    row[0], row[1], row[2], row[3], row[4], row[5]))
            return details  # 리스트 반환
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def getStoreId(self):  # 현재 로그인 되어있는 사용자가 보유중인 점포id 반환
        ids = []  # 사용자의 점포id 들을 담을 리스트 생성
        self.connect()
        cur = self.conn.cursor()
        # stores 테이블에서 매니저ID 값이 일치하는 행의 store_id 검색
        sql = 'select store_id from stores where manager_id = %s'
        member_id = mem.MemService.login_id  # 현재 로그인 되어있는 사용자의 id를 변수에 저장
        vals = (member_id,)  # 사용자id 값을 기준으로 쿼리문 변수 매칭
        try:
            cur.execute(sql, vals)
            for row in cur:
                ids.append(row[0])  # 검색 결과를 점포id 리스트에 추가
            return ids  # 리스트 반환
        except Exception as e:
            print(e)
        finally:
            self.disconnect()


class OrdercheckService:
    def __init__(self):
        self.dao = OrdercheckDao()

    def checkOrderStatus(self):  # 미확인된 주문 내역을 확인하고 상태 변경
        print('미확인 주문내역 확인')
        store_id = int(input('주문을 확인할 점포ID:'))  # 미확인 주문내역을 확인할 점포의 id 입력
        ids = self.dao.getStoreId()  # 로그인 되어있는 사용자가 등록한 점포id 리스트 가져오기
        if ids == None or len(ids) == 0:  # 리스트가 비어있을 경우
            print('보유중인 점포가 없습니다.')
        elif store_id in ids:  # 입력한 점포id가 리스트 안에 있는 경우
            list = self.dao.selectOrderByStatus(store_id)  # 미확인 주문 내역 가져오기
            if list == []:  # 주문내역이 없을 경우
                print('미확인 주문내역이 없습니다')
            else:
                # 주문내역이 있을 경우 하나씩 출력 후 사용자가 처리방법 선택  [ordervo1, ordervo2, ...]
                for i in list:
                    print(i)
                    vo_list = self.dao.selectOrderDetail(i.order_id)
                    for j in vo_list:
                        print(j)
                    change = input('1.주문접수 2.다음주문 3.나가기')
                    if change == '1':
                        self.dao.editOrderStatus(i.order_id)  # 주문내역을 접수상태로 변경
                        print('주문접수완료')
                    elif change == '2':
                        print('주문을 미확인 상태로 유지합니다.')
                    elif change == '3':
                        print('주문확인을 마칩니다.')
                        break
                    else:
                        print('잘못된 입력, 주문을 접수하지 않습니다.')
                    if i == list[-1]:
                        print('모든 주문을 확인했습니다.')
        else:
            print('회원님이 보유중인 점포ID가 아닙니다.')

    def checkAllOrder(self):
        print('전체 주문내역 확인')
        store_id = int(input('주문을 확인할 점포ID:'))
        ids = self.dao.getStoreId()
        if ids == None or len(ids) == 0:
            print('보유중인 점포가 없습니다.')
        elif store_id in ids:
            list = self.dao.selectStoreOrder(store_id)
            if list == []:
                print('주문내역이 없습니다.')
            else:
                print("----전체주문내역::주문상태 0=미확인, 1=접수완료----")
                for i in list:
                    print(i)
        else:
            print('회원님이 보유중인 점포ID가 아닙니다.')

    def checkOrderDetail(self):
        print('상세 주문내역 확인')
        order_id = int(input('상세내역을 확인할 주문번호:'))
        vo_list = self.dao.selectOrderDetail(order_id)
        if vo_list == None or len(vo_list) == 0:
            print('검색결과 없음')
        else:
            print(f'----주문ID {order_id}번 상세주문정보----')
            for i in vo_list:
                print(i)
