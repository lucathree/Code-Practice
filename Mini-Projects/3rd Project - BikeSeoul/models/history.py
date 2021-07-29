import pymysql, pandas


class History:
    def __init__(self, num=None, member_id=None, rent_station=None, return_station=None, rent_date=None,
                 rent_time=None, return_time=None, distance=None):
        self.num = num
        self.member_id = member_id
        self.rent_station = rent_station
        self.return_station = return_station
        self.rent_date = rent_date
        self.rent_time = rent_time
        self.return_time = return_time
        self.distance = distance


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
        vals = (hist.member_id, hist.rent_station, hist.return_station, hist.rent_date,
                hist.rent_time, hist.return_time, hist.distance)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectAll(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select date_format(rent_date, "%%y-%%m-%%d") as rent_date, rent_station, return_station, ' \
              'date_format(rent_time, "%%H:%%i") as rent_time, date_format(return_time, "%%H:%%i") as return_time, ' \
              'distance from history where member_id=%s order by rent_date desc'
        histories = []
        vals = (id,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                histories.append(History(rent_date=row[0], rent_station=row[1], return_station=row[2],
                                         rent_time=row[3], return_time=row[4], distance=row[5]))
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

    ############ 여기부터 이용통계 관련

    def calcUseTime(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select sum(time_to_sec(timediff(return_time, rent_time))/60) from history where member_id=%s'
        cur.execute(sql, id)
        row = cur.fetchone()
        self.disconnect()
        if row !=None:
            return round(row[0])


    def selectUserStations(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select rent_station, return_station from history where member_id=%s'
        vals = (id,)
        cur.execute(sql, vals)
        stats = []
        for row in cur:
            stats.append(row[0])
            stats.append(row[1])
        self.disconnect()
        return stats

    def calcFavStn(self, id):
        stations = self.selectUserStations(id)
        count_list=[]
        for i in stations:
            count_list.append(stations.count(i))
        return stations[count_list.index(max(count_list))]

    def calcDistance(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select sum(distance) from history where member_id=%s'
        cur.execute(sql, id)
        dis = cur.fetchone()
        self.disconnect()
        return dis[0]

    def calcCarbon(self, id):
        distance = self.calcDistance(id)
        carbon = (distance * 0.001) * 0.232
        return round(carbon, 2)

    def calcWorkout(self, id):
        distance = self.calcDistance(id)
        kcal = (distance * 0.001) * 65 * (5.94/15)
        return round(kcal, 2)

    def selectCount(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select count(*) from history where member_id=%s'
        cur.execute(sql, id)
        res = cur.fetchone()
        self.disconnect()
        return res[0]

class HistoryService:
    def __init__(self):
        self.dao = HistoryDao()

    def writeHistory(self, hist):
        self.dao.insert(hist)

    def getHistory(self, id):
        return self.dao.selectAll(id)

    def getStationList(self):
        return self.dao.selectStations()

    def getTotalHours(self, id):
        time = self.dao.calcUseTime(id)
        hour = time // 60
        min = time % 60
        return str(hour) + '시간 ' + str(min) + '분'

    def getFavStn(self, id):
        return self.dao.calcFavStn(id)

    def getTotalCarbon(self, id):
        return self.dao.calcCarbon(id)

    def getTotalWorkout(self, id):
        return self.dao.calcWorkout(id)

    def getCount(self, id):
        return self.dao.selectCount(id)

    def getDistance(self, id):
        return self.dao.calcDistance(id)

    def getHoursByMin(self, id):
        return self.dao.calcUseTime(id)