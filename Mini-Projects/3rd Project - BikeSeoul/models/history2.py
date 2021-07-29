import pymysql, pandas


class History:
    def __init__(self, num=None, member_id=None, rent_station=None, return_station=None, rent_date=None, return_date=None,
                 rent_time=None, return_time=None, distance=None, use_time=None):
        self.num = num
        self.member_id = member_id
        self.rent_station = rent_station
        self.return_station = return_station
        self.rent_date = rent_date
        self.return_date = return_date
        self.rent_time = rent_time
        self.return_time = return_time
        self.distance = distance
        self.use_time = use_time

class MyData:
    def __init__(self, favSt=None, stats=None, workout=None, carbon=None, useTime=None, distance=None):
        self.favStation = favSt
        self.stations = stats  # stStNm + endStNm (count)
        self.workout = workout  # 운동량 계산 공식
        self.carbon = carbon  # 탄소량(kg) 계산공식
        self.useTime = useTime  # endTime - stTime
        self.distance = distance  # history 받아오기


class HistoryDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='bikeseoul', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, hist):
        self.connect()
        cur = self.conn.cursor()
        sql = "insert into history(member_id, rent_station, return_station, rent_date, rent_time, " \
              "return_time, distance) " \
              "values(%s, %s, %s, %s, %s, %s, %s)"
        vals = (hist.member_id, hist.rent_station, hist.return_station, hist.rent_date, hist.return_date,
                hist.rent_time, hist.return_time, hist.distance)
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()

    def selectAll(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select date_format(rent_date, "%%y-%%m-%%d") as rent_date, return_date, rent_station, return_station, ' \
              'date_format(rent_time, "%%H:%%i") as rent_time, date_format(return_time, "%%H:%%i") as return_time, ' \
              'distance from history where member_id=%s order by rent_date desc'
        histories = []
        vals = (id,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                histories.append(History(rent_date=row[0], return_date=row[1], rent_station=row[2], return_station=row[3],
                                         rent_time=row[4], return_time=row[5], distance=row[6]))
        except Exception as e:
            print(e)
        finally:
            self.disconnect()
            return histories

    def selectStations(self):
        data = pandas.read_csv('static/data/station_list.csv', encoding='cp949')
        lst = data['보관소명']
        res = lst.tolist()
        return res

    def getFavSt(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select rent_station, return_station from history where member_id=%s'
        vals = (id,)
        cur.execute(sql, vals)
        stats = []
        fav = []
        for row in cur:
            st = stats(row[0], row[1])
            stats.append(st)
            fav = stats.value_counts()
        self.disconnect()
        return fav[0]

    def getDistance(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select sum(distance) from history where member_id=%s'
        cur.execute(sql, id)
        dis = cur[1]
        self.conn.commit()
        self.disconnect()
        return dis

    def getUseTime(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select sum(return_time - rent_time) from history where member_id=%s'
        cur.execute(sql, id)
        row = cur.fetchone()
        self.disconnect()
        times = []
        if row !=None:
            times = ((str(row))[:-1])
        return times

    def mydata(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from mydata where member_id=%s'
        cur.execute(sql, id)
        row = cur.fetchone()
        self.disconnect()
        if row != None:
            favSt = row[0]
            workout = row[1]
            carbon = row[2]
            useTime = row[3]
            distance = row[3]
            datas = mydata(favSt, workout, carbon, useTime, distance)
            return datas

    def getworkout(self,weight,distance):   #
        self.connect()
        cur = self.conn.cursor()
        if (weight != None) and (distance != None):
            workout = distance * weight * 5.94 / 15
        elif (weight == None) and (distance != None):
            workout = distance * 65 * 5.94 / 15
        else:
            workout = '운동량을 계산할 수 없습니다. 몸무게와 이동한 거리를 입력하세요.'
        self.disconnect()
        return workout



class HistoryService:
    def __init__(self):
        self.dao = HistoryDao()

    def writeHistory(self, hist):
        self.dao.insert(hist)

    def getHistory(self, id):
        return self.dao.selectAll(id)

    def getStationList(self):
        return self.dao.selectStations()

    def getMydata(self,id):
        return self.dao.mydata(id)

