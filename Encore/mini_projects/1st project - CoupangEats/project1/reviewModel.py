import pymysql

import project1.memModel as mem
import project1.ordercheckModel as order


class ReviewVo:
    def __init__(self, review_id=None, order_id=None, score=None, content=None, store_name=None, reviewer=None):
        self.review_id = review_id
        self.order_id = order_id
        self.score = score
        self.content = content
        self.store_name = store_name
        self.reviewer = reviewer

    def __str__(self):
        return f'가게이름:{self.store_name} / 주문번호:{self.order_id} / 주문자:{self.reviewer} / 점수:{self.score} / 한줄평:{self.content}'


class ReviewDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234',
                                    db='coupangeats_project', charset='utf8')

    def disconnect(self):
        self.conn.close()

    # 리뷰 등록
    def insert(self, vo):
        self.connect()
        cur = self.conn.cursor()
        sql = 'insert into reviews(review_id, order_id, score, content) \
            values(%s, %s, %s, %s)'
        vals = (vo.review_id, vo.order_id, vo.score, vo.content)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 리뷰 전체 선택
    def selectAllReview(self):
        reviews = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'SELECT store_name, r.order_id, member_id, score, content ' \
              'from reviews r join orders o on r.order_id = o.order_id ' \
              'join stores s on o.store_id = s.store_id'
        try:
            cur.execute(sql)
            for row in cur:
                reviews.append(
                    ReviewVo(store_name=row[0], order_id=row[1],
                             reviewer=row[2], score=row[3], content=row[4])
                )
            return reviews
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

        # 내 리뷰 선택
    def selectMyReview(self):
        reviews = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'SELECT store_name, r.order_id, member_id, score, content ' \
              'from reviews r join orders o on r.order_id = o.order_id ' \
              'join stores s on o.store_id = s.store_id ' \
            'where member_id=%s'
        vals = (mem.MemService.login_id,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                reviews.append(
                    ReviewVo(store_name=row[0], order_id=row[1],
                             reviewer=row[2], score=row[3], content=row[4])
                )
            return reviews
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 주문번호 받아서 리뷰 선택

    def selectReview(self, order_id):
        reviews = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'SELECT store_name, r.order_id, member_id, score, content ' \
              'from reviews r join orders o on r.order_id = o.order_id ' \
              'join stores s on o.store_id = s.store_id ' \
              'where r.order_id=%s'
        vals = (order_id,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                reviews.append(
                    ReviewVo(store_name=row[0], order_id=row[1],
                             reviewer=row[2], score=row[3], content=row[4])
                )
            return reviews
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 해당 order_id 데이터 있는지 확인,로긴아이디랑 주문접수된거 맞는지
    # sql문에서 전부 조건 걸어줌
    # order_id가 자동설정 되는건가?
    def selectByOrderId(self, order_id):
        orders = []
        self.connect()
        cur = self.conn.cursor()

        sql = 'select * from orders where order_id = %s and reception_status=1 and member_id=%s'
        vals = (order_id, mem.MemService.login_id)
        try:
            cur.execute(sql, vals)
            for row in cur:
                orders.append(
                    order.OrdersVo(row[0], row[1], row[2],
                                   row[3], row[4], row[5], row[6])
                )
                return orders
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    #### 아래는 평균리뷰점수 등록을 위해 추가된 내용입니다. 작성자: 이창민 ####
    # 주문ID로 리뷰 등록할 점포ID 반환
    def getStoreId(self, order_id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select store_id from orders where order_id = %s'
        vals = (order_id,)
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()
            if row != None:
                store_id = row[0]
                return store_id
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 점포ID로 해당 가게의 평균 리뷰점수 반환
    def getAvgScore(self, store_id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select store_id, avg(score) ' \
              'from reviews r ' \
              'join orders o ' \
              'using (order_id) ' \
              'where store_id = %s'
        vals = (store_id,)
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()
            if row != None:
                avg_score = row[1]
                return avg_score
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 반환된 평균 리뷰점수를 해당 점포에 업데이트
    def addAvgScore(self, avg_score, store_id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'update stores set avg_score = %s where store_id = %s'
        vals = (avg_score, store_id)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 리뷰 달 수 있는 주문 출력 reception_status=1 인 주문 출력
    def selectReception(self, member_id):
        orders = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from orders where reception_status=1 and member_id=%s'
        vals = (member_id,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                orders.append(
                    order.OrdersVo(row[0], row[1], row[2],
                                   row[3], row[4], row[5], row[6])
                )
                return orders
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    # 중복체크를 위한 리뷰테이블에 있는 주문 id 출력
    def selectOrderId(self):
        ids = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'select order_id from reviews '
        try:
            cur.execute(sql)
            for row in cur:
                ids.append(row[0])
            return ids
        except Exception as e:
            print(e)
        finally:
            self.disconnect()


class ReviewService:
    def __init__(self):
        self.dao = ReviewDao()

    # 8. 리뷰평점등록
    def addReview(self):
        print('리뷰 및 평점 등록')
        # 리뷰 달수 있는 주문 출력
        order_list = self.dao.selectReception(mem.MemService.login_id)
        if order_list == None or len(order_list) == 0:
            print('리뷰할수 있는 주문이 없습니다')
        else:
            print('접수된 주문 목록')
            for order in order_list:
                print(order)
            id_list = self.dao.selectOrderId()
            # 해당 order_id 데이터 있는지 확인
            order_id = int(input('리뷰 등록하고 싶은 주문 아이디 입력:'))
            # 중복체크
            if order_id in id_list:
                print('이미 리뷰가 있습니다')
            else:
                vo_list = self.dao.selectByOrderId(order_id)
                if vo_list == None or len(vo_list) == 0:
                    print('고객님이 리뷰를 작성할 수 있는 주문이 아닙니다')
                else:
                    # 특정 상품 id, 가게id 입력??
                    content = input('리뷰 등록:')
                    score = int(input('평점 등록 (1~5점 중 선택):'))
                    # 평점 1~5
                    if score >= 1 and score <= 5:
                        self.dao.insert(ReviewVo(order_id=order_id,
                                        score=score, content=content))
                        print('리뷰 등록 완료')
                        # 입력된 order_id로 검색해서 평균리뷰점수 넣을 store_id 반환
                        store_id = self.dao.getStoreId(order_id)
                        avg_score = self.dao.getAvgScore(
                            store_id)  # 점포의 평균리뷰점수 반환
                        self.dao.addAvgScore(avg_score, store_id)  # 평균리뷰점수 입력
                    else:
                        print('잘못된 입력입니다. 리뷰를 다시 등록해주세요.')

    # 9.2 리뷰 확인하기 리뷰 번호 받아서
    def printReviewByOrder(self):
        order_id = int(input('리뷰를 확인할 주문번호 입력:'))
        reviews = self.dao.selectReview(order_id)
        if reviews == None or len(reviews) == 0:
            print('검색결과 없음')
        else:
            for review in reviews:
                print(review)

    # 9.1 모든 리뷰

    def printAllReview(self):
        print('리뷰 목록')
        reviews = self.dao.selectAllReview()
        for review in reviews:
            print(review)

    # 9.3 내 리뷰 확인하기
    def printMyReview(self):
        print('내 리뷰 보기')
        reviews = self.dao.selectMyReview()
        for review in reviews:
            print(review)

    # 리뷰 선택지

    def printReview(self):
        while True:
            m = input('1.리뷰전체보기 2.주문별 리뷰보기 3.내 리뷰 보기 4.나가기')
            if m == '1':
                self.printAllReview()
            elif m == '2':
                self.printReviewByOrder()
            elif m == '3':
                self.printMyReview()
            elif m == '4':
                break
            else:
                continue

    def insertScore(self):
        pass


"""
테스트코드
r = ReviewService()
m = mem.MemService()

m.login()
r.addReview()
r.printReview()
"""
