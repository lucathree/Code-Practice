import pymysql
from datetime import datetime
import userModel as user
import stationModel as st


class ReservationVo:
    def __init__(self, id=None, station=None, rsvtime=None, user_id=None, status=None):
        self.id = id
        self.station = station
        self.rsvtime = rsvtime
        self.user_id = user_id
        self.status = status

    def __str__(self):
        return '예약번호:' + str(self.id) + ' / 충전소명:' + self.station + ' / 예약시간:' + str(self.rsvtime) + \
               ' / 결과:' + self.status


class ReservationDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='1234', db='chargestation', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, station, rsvtime):
        user_id = 'test' #user.UserService.login_id
        self.connect()
        cur = self.conn.cursor()
        sql = 'insert into reservations(station, rsvtime, user_id) values(%s, %s, %s)'
        vals = (station, rsvtime, user_id)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def get_rsv(self):  # 사용자 예약내역 확인
        reservations = []  # 검색 결과를 담을 리스트
        user_id = 'test' #user.UserService.login_id
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from reservations where user_id = %s'
        vals = (user_id,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                if row[2] < datetime.now():
                    reservations.append(ReservationVo(row[0], row[1], row[2], row[3], '지난예약'))
                else:
                    reservations.append(ReservationVo(row[0], row[1], row[2], row[3], row[4]))
            sql2 = 'update reservations set status = "지난예약" where rsvtime < sysdate()'
            cur.execute(sql2,)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            return reservations
            self.disconnect()

    def cancel_rsv(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'update reservations set status = "예약취소" where reservation_id = %s'
        vals = (id,)
        try:
            cur.execute(sql, vals)  # 커서객체 실행
            self.conn.commit()  # 수정내용 커밋
        except Exception as e:
            print(e)
        finally:
            self.disconnect()


class ReservationService:
    def __init__(self):
        self.dao = ReservationDao()

    def make_rsv(self):
        print('준비 중... 잠시만 기다려주세요')
        sm = st.StationDao()
        df = sm.make_df(' ')
        cpid = input('예약할 충전소 ID:')
        res = df[df['ID'] == cpid]
        try:
            res.iloc[0]
        except Exception:
            print('존재하지 않는 충전소')
        station = res.iloc[0]['충전소명']
        rsvtime = input('예약시간 (yyyy-mm-dd HH:MM)')
        self.dao.insert(station, rsvtime)
        print('예약이 완료되었습니다')

    def check_rsv(self):
        print('예약내역 확인')
        reservations = self.dao.get_rsv()
        for i in reservations:
            print(i)

    def cancel_rsv(self):
        id = input('취소할 예약번호:')
        self.dao.cancel_rsv(id)
        print('예약이 취소되었습니다')

s = ReservationService()
s.make_rsv()
s.check_rsv()
s.cancel_rsv()
