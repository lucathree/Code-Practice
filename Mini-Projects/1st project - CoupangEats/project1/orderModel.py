import pymysql


import project1.memModel as mem


class OrdersVo:  # 주문 vo
    def __init__(self, order_id=None, member_id=None, store_id=None, total_price=None, order_time=None,
                 destination=None, reception_status=0):
        self.order_id = order_id
        self.member_id = member_id
        self.store_id = store_id
        self.total_price = total_price
        self.order_time = order_time
        self.destination = destination
        self.reception_status = reception_status

    def __str__(self):  # 객체 설명. 클래스풀네임. 참조값
        return '주문 id:' + str(self.order_id) + '/ 회원 id:' + str(self.member_id) + ' / 가게 id:' + str(
            self.store_id) + ' / 주문 총액:' + str(self.total_price) + \
            ' / 주문 시간:' + self.order_time + '/배송지:' + \
            self.destination + '/ 주문 확인 유무:'+self.reception_status


class OrderDetailsVo:  # 주문 상세vo
    def __init__(self, orderdetail_id=None, order_id=None, product_id=None, count=None, orderdetail_price=None):
        self.orderdetail_id = orderdetail_id
        self.order_id = order_id
        self.product_id = product_id
        self.count = count
        self.orderdetail_price = orderdetail_price


class OrdersDao:
    def __init__(self):
        self.conn = None  # 커넥션 객체 담을 멤버 변수
        self.order_id = 0

    # db연결함수. db 사용전 로그인하는 작업을 수행
    def connect(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='1234', db='coupangeats_project', charset='utf8')

    # db 닫는 함수
    def disconnect(self):
        self.conn.close()

    # 공통 Inert 문장
    def insert(self, tableName, dictVal):
        if(isinstance(dictVal, dict)):  # 매개변수의 타입 확인 dictionary
            self.connect()
            self.conn.begin()
            try:
                with self.conn.cursor() as insert_cursor:
                    sqlcmd = (
                        f"INSERT INTO {tableName} ({', '.join(dictVal.keys())}) "
                        f"VALUES (%({')s, %('.join(dictVal.keys())})s)")
                    insert_cursor.execute(sqlcmd, dictVal)
                self.conn.commit()
                self.disconnect()
                return insert_cursor.lastrowid  # 마지막 아이디를 반환
            except:
                self.conn.rollback()
                print('\a추가를 실패하였습니다. 값이나 테이블을 확인해주세요')
                raise  # 오류 내보냄

    # 공통 Delete 문장
    def delete(self, tableName, dictVal):
        if(isinstance(dictVal, dict)):
            condition = ['1=1']  # 조건 설정
            for key in dictVal.keys():  # 차후에 Type을 비교하여 데이터를 넣는 문장 생성 예정
                tempVal = ''
                if (isinstance(dictVal[key], int)):
                    tempVal += key + ' = ' + str(dictVal[key])
                else:
                    tempVal += key + ' = \'' + dictVal[key] + '\''
                condition.append(tempVal)
            self.connect()
            self.conn.begin()  # 시작
            try:
                with self.conn.cursor() as delete_cursor:
                    sqlcmd = (
                        f"DELETE FROM {tableName} "
                        f"WHERE  {' AND '.join(condition) }")
                    delete_cursor.execute(sqlcmd, dictVal)
                    self.conn.commit()
                    self.disconnect()
                    return delete_cursor.rowcount
            except:
                self.conn.rollback()
                print('\a삭제를 실패하였습니다. 값이나 테이블을 확인해주세요')
                raise

    # 공통 Select 문장
    def selectAll(self, tableName, dictVal):
        if (isinstance(dictVal, dict)):
            condition = ['1 = 1']
            for key in dictVal.keys():  # 차후에 Type을 비교하여 데이터를 넣는 문장 생성 예정
                tempVal = ''
                if (isinstance(dictVal[key], int)):
                    tempVal += key + ' = ' + str(dictVal[key])
                else:
                    tempVal += key + ' = \'' + dictVal[key] + '\''
                condition.append(tempVal)

            self.connect()
            try:
                rtnList = []  # 배열 전달
                with self.conn.cursor(pymysql.cursors.DictCursor) as select_cursor:
                    sqlcmd = (
                        f"SELECT * FROM {tableName} "
                        f"WHERE  {' AND '.join(condition)}")
                    select_cursor.execute(sqlcmd, dictVal)

                    for row in select_cursor:
                        rtnList.append(row)

                    self.disconnect()
                    return rtnList
            except:
                self.conn.rollback()
                print('\a조회를 실패하였습니다. 값이나 테이블을 확인해주세요')
                raise

    # 공통 Select 문장
    def select(self, tableName, dictVal):
        if(isinstance(dictVal, dict)):
            condition = ['1 = 1']
            for key in dictVal.keys():  # 차후에 Type을 비교하여 데이터를 넣는 문장 생성 예정
                tempVal = ''
                if(isinstance(dictVal[key], int)):
                    tempVal += key + ' = ' + str(dictVal[key])
                else:
                    tempVal += key + ' = \'' + dictVal[key] + '\''
                condition.append(tempVal)

            self.connect()
            try:
                with self.conn.cursor(pymysql.cursors.DictCursor) as select_cursor:
                    sqlcmd = (
                        f"SELECT * FROM {tableName} "
                        f"WHERE  {' AND '.join(condition)}")

                    select_cursor.execute(sqlcmd, dictVal)
                    # 각각의 id를 만족하는 것은 한줄 만 나올것 이다.
                    row = select_cursor.fetchone()
                    self.disconnect()
                    return row
            except:
                self.conn.rollback()
                print('\a조회를 실패하였습니다. 값이나 테이블을 확인해주세요')
                raise

    # 공통 update
    def update(self, tableName, changeStatus, whereVal):
        if(isinstance(changeStatus, dict) and isinstance(whereVal, dict)):
            changeCondition = []
            for key in changeStatus.keys():  # 차후에 Type을 비교하여 데이터를 넣는 문장 생성 예정
                tempVal = ''
                if (isinstance(changeStatus[key], int)):
                    tempVal += key + ' = ' + str(changeStatus[key])
                else:
                    tempVal += key + ' = \'' + changeStatus[key] + '\''
                changeCondition.append(tempVal)

            whereCondition = ['1 = 1']
            for key in whereVal.keys():  # 차후에 Type을 비교하여 데이터를 넣는 문장 생성 예정
                tempVal = ''
                if (isinstance(whereVal[key], int)):
                    tempVal += key + ' = ' + str(whereVal[key])
                else:
                    tempVal += key + ' = \'' + whereVal[key] + '\''
                whereCondition.append(tempVal)

            self.connect()
            self.conn.begin()  # 시작
            try:
                with self.conn.cursor() as update_cursor:
                    sqlcmd = (
                        f"UPDATE {tableName} SET "
                        f"{' , '.join(changeCondition)}"
                        f" WHERE {' AND '.join(whereCondition)}"
                    )
                    update_cursor.execute(sqlcmd)
                    self.conn.commit()
                    self.disconnect()
                    return update_cursor.rowcount
            except:
                self.conn.rollback()
                print('\a갱신을 실패하였습니다. 값이나 테이블을 확인해주세요')
                raise

    # order_details 전체 합계 (공통으로 가능하나 현재는 구현 안할예정임)
    def calTotalPrice(self, order_id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select sum(orderdetail_price * count) AS total_cnt from order_details where order_id=%s'
        vals = (order_id,)
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()
            if row != None:
                return row[0]
        except Exception as a:
            print(a)
        finally:
            self.disconnect()

    # 작성자 :송하늘
    # 가. 6 주문확인할때 상세하게 출력 sql문 약간 변경
    # 파라메터로 현재 로그인한 회원의 member_id= mem.memService.login_id 로 가져옴
    def showAllDetailByMember(self, member_id):
        self.connect()
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as select_cursor:
                rtnList = []  # 배열 전달
                sqlcmd = (
                    f"SELECT d.orderdetail_id AS \"주문상세번호\", d.order_id AS \"주문번호\", d.product_id AS \"상품번호\", p.product_name AS \"상품명\", d.count, d.orderdetail_price  AS \"상품가격\" "
                    f"FROM order_details d "
                    f"INNER JOIN products p "
                    f"ON p.product_id= d.product_id "
                    f"JOIN orders o "
                    f"ON o.order_id = d.order_id "
                    f"WHERE o.member_id='{member_id}'")

                select_cursor.execute(sqlcmd)
                for row in select_cursor:
                    rtnList.append(row)
                self.disconnect()
                return rtnList
        except:
            self.conn.rollback()
            print('\a조회를 실패하였습니다. 값이나 테이블을 확인해주세요')
            raise


class OrderService:
    def __init__(self):
        self.dao = OrdersDao()

    # 주문 접수
    def addOrder(self):
        store_id = int(input('점포 아이디를 입력'))

        store = self.dao.select('stores', {'store_id': store_id})

        if(store != None):
            destination = input('배송지역:')
            if destination != store['location']:  # 입력한 배송지와 그 가게의 위치가 다르면
                print('배송이 불가능한 지역입니다.')
            else:
                order_id = self.dao.insert('orders', {'member_id': mem.MemService.login_id  # m.MemService.login_id 가 없으므로 테스트로 aaa 로 사용
                                                      , 'store_id': store_id, 'destination': destination})

                flag = True
                while flag:
                    print('상세주문 작성 페이지 입니다.')
                    product_id = int(input('상품 아이디를 입력'))
                    product = self.dao.select(
                        'products', {'product_id': product_id, 'store_id': store_id, 'sale_available': 1
                                     })
                    if product == None:
                        print('이 가게에선 그 음식을 팔지 않습니다. 다시 입력하세요.')
                        break

                    else:
                        count = int(input('몇개를 사시겠습니까? :'))

                        orderDetails_id = self.dao.insert('order_details', {
                                                          'order_id': order_id, 'product_id': product_id, 'count': count, 'orderdetail_price': product['product_price']})

                        self.dao.update('orders', {
                                        'total_price': product['product_price'] * count}, {'order_id': order_id})

                        # vo 객체 삽입 차후 연동을 위함
                        OrderDetailsVo(order_id=order_id, product_id=product_id,
                                       count=count, orderdetail_price=product['product_price'] * count)

                    checkOrderStatus = input('추가 주문을 하시겠습니까?Y/N(기본값):')
                    if checkOrderStatus.upper() == 'Y':
                        flag = True
                    else:
                        flag = False

                print('===========================================================총 주문내역============================================================================')

                detail_list = self.dao.selectAll(
                    'order_details', {'order_id': order_id})
                # 세부 주문을 전혀 하지 않은 경우(=order_id에 해당하는 주문디테일이 없음)
                if detail_list == None or len(detail_list) == 0:
                    print('주문 내역이 없습니다. 주문을 취소합니다.')
                    # insert했었던 미완성주문 레코드를 삭제
                    self.dao.delete('orders', {'order_id': order_id})
                else:  # 세부 주문을 했다면, 그 내역 출력
                    for column in ['주문상세번호', '주문번호', '상품번호', '개수', '주문상세가격']:
                        print('%19s' % column, end='\t')
                    print()
                    for dict in detail_list:
                        for column in dict.keys():
                            print('%20s' % dict[column], end='\t')
                        print()

                total_price = self.dao.calTotalPrice(order_id)
                print('구매한 물품의 전체 총액의 합은 : ' + str(total_price))

    # 내 주문내역 확인(전체출력)
    def getAllMyOrder(self):
        print('내 주문내역 확인')
        # m.MemService.login_id 가 없으므로 테스트로 aaa 로 사용
        order_list = self.dao.selectAll(
            'orders', {'member_id': mem.MemService.login_id})
        if order_list == None or len(order_list) == 0:
            print('주문 내역이 없습니다.')
        else:
            print('=================================================================================총 주문내역============================================================================')
            for column in ['주문번호', '주문자아이디', '상점번호', '전체가격', '주문시간', '목적지', '주문상태']:
                print('%19s' % column, end='\t')
            print()
            for dict in order_list:
                for column in dict.keys():
                    print('%20s' % dict[column], end='\t')
                print()

    # 내 주문내역 확인(전체출력)
    def cancelMyOrder(self):
        print('취소 가능한 주문 목록')
        # m.MemService.login_id 가 없으므로 테스트로 aaa 로 사용
        no_reception_list = self.dao.selectAll(
            'orders', {'member_id': mem.MemService.login_id, 'reception_status': 0})
        print('=================================================================================총 주문내역============================================================================')
        for column in ['주문번호', '주문자아이디', '상점번호', '전체가격', '주문시간', '목적지', '주문상태']:
            print('%19s' % column, end='\t')
        print()
        for dict in no_reception_list:
            for column in dict.keys():
                print('%20s' % dict[column], end='\t')
            print()

        order_id = int(input('취소하고 싶은 주문 id(order_id):'))
        factor = 0
        for row in no_reception_list:
            id = row['order_id']  # 취소 가능한 주문의 order_id
            if int(id) == order_id:
                factor += 1  # 만약 입력받은 주문id가 취소가능한 주문들의 order_id들 중에 하나와 일치할 경우 factor에 +1

        if factor == 0:  # 입력한 주문id가 취소 가능한 주문들의 order_id 중에 존재하지 않을 때
            print('그 주문은 취소가 불가능한 주문입니다.')
        else:
            print('입력한 주문id에 해당하는 모든 주문과 세부주문내역을 삭제합니다.')
            line_1 = self.dao.delete('order_details', {'order_id': order_id})
            line_2 = self.dao.delete('orders', {'order_id': order_id})
            print(f'{line_2}개의 주문내역과 {line_1}개의 상세주문내역이 성공적으로 삭제되었습니다.')

    # 가. 6 주문확인할때 상세하게 출력
    def getAllMyOrderDetails(self):
        print('내 주문내역 확인')
        # m.MemService.login_id 가 없으므로 테스트로 aaa 로 사용
        order_list = self.dao.showAllDetailByMember(mem.MemService.login_id)
        if order_list == None or len(order_list) == 0:
            print('주문 내역이 없습니다.')
        else:
            print('=============================================================총 주문내역======================================================================')
            for column in order_list[0].keys():
                print('%19s' % column, end='\t')
            print()
            for dict in order_list:
                for column in dict.keys():
                    print('%20s' % dict[column], end='\t')
                print()

# #테스트용 코드
# a = OrderService()

# a.addOrder()
