import pymysql


class MyData:
    def __init__(self, favSt=None, stats=None, workout=None, carbon=None, useTime=None, distance=None):
        self.favStation = favSt
        self.stations = stats      # stStNm + endStNm (count)
        self.workout = workout      # 운동량 계산 공식
        self.carbon = carbon         # 탄소량(kg) 계산공식
        self.useTime = useTime      # endTime - stTime
        self.distance = distance     # history 받아오기


class MyDataDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='1234', db='bikeseoul', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, mydata):
        self.connect()
        cur = self.conn.cursor()
        sql = "insert into mydata(favSt,workout,carbon, useTime, distance) values(%s, %s, %s, %s, %s)"   #변수가 들어갈 위치에 %s와 같은 포맷문자 지정
        vals = (mydata.favSt, mydata.workout, mydata.carbon, mydata.useTime, mydata.distance)
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()

    def selectAll(self):
        self.connect()
        cur = self.conn.cursor()
        sql = "select * from mydata"
        cur.execute(sql)
        datas = []
        for row in cur:
            d = mydata(row[0], row[1], row[2], row[3], row[4])
            datas.append(d)
        self.disconnect()
        return datas


    def getworkout(self,weight,distance):
        self.connect()
        cur = self.conn.cursor()
        if (weight != None) and (distance != None):
            workout = distance * weight * 5.94 / 15
        elif (weight == None) and (distance != None):
            workout = distance * 65 * 5.94 / 15
        else:
            print('운동량을 계산할 수 없습니다. 몸무게와 이동한 거리를 입력하세요.')
        self.disconnect()
        return workout


    def carbon(self, distance):
        self.connect()
        cur = self.conn.cursor()

        if distance != None:
            carbon = distance * 0.232
        else:
            print('탄소량을 계산할 수 없습니다. 이동한 거리를 입력하세요.')
        self.disconnect()
        return carbon

    def stats(self):
        self.connect()



    def useTime(self, time):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from board where writer=%s order by num desc'
        vals = (writer,)
        cur.execute(sql, vals)
        boards = []
        for row in cur:
            boards.append(Board(row[0], row[1], row[2], row[3], row[4]))
        self.disconnect()
        return boards

    def stations(self, stats):
        self.connect()
        cur = self.conn.cursor()
        stats = []
        stats.append(hist.stStNm)
        stats.append(hist.endStNm)
        count()
        sql = 'select * from stStNm, endStNm order by num desc'
        vals = (stats,)
        cur.execute(sql, vals)

        self.disconnect()
        return stats


class MyDataService:
    def __init__(self):
        self.dao = MyDataDao()

    def addData(self, mydata):  # db저장
        self.dao.insert(mydata)

    def getAll(self):   #전체검색기능
        datas = self.dao.selectAll()
        return datas