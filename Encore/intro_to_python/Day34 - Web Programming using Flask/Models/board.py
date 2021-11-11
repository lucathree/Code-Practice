import pymysql

class Board:
    def __init__(self, num=None, writer=None, w_date=None, title=None, content=None):
        self.num = num
        self.writer = writer
        self.w_date = w_date
        self.title = title
        self.content = content


class BoardDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', database='encore', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, board):
        self.connect()
        cur = self.conn.cursor()
        sql = "insert into board(writer, w_date, title, content) values(%s, now(), %s, %s)"
        vals = (board.writer, board.title, board.content)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectAll(self):
        self.connect()
        cur = self.conn.cursor()
        sql = "select * from board"
        cur.execute(sql)
        rows = []
        for row in cur:
            rows.append(Board(row[0], row[1], row[2], row[3], row[4]))
        self.disconnect()
        return rows

    def selectByNum(self, num):
        self.connect()
        cur = self.conn.cursor()
        sql = "select * from board where num=%s"
        vals = (num,)
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()
            bo = Board(row[0], row[1], row[2], row[3], row[4])
        except Exception as e:
            print(e)
        finally:
            self.disconnect()
            return bo

    def selectByWriter(self, writer):
        self.connect()
        cur = self.conn.cursor()
        sql = "select * from board where writer=%s"
        vals = (writer,)
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()
            bo = Board(row[0], row[1], row[2], row[3], row[4])
        except Exception as e:
            print(e)
        finally:
            self.disconnect()
            return bo

    def update(self, board):
        self.connect()
        cur = self.conn.cursor()
        sql = "update board set title=%s, content=%s where num=%s"
        vals = (board.title, board.content, board.num)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def delete(self, num):
        self.connect()
        cur = self.conn.cursor()
        sql = "delete from board where num=%s"
        vals = (num,)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()


class BoardService:
    def __init__(self):
        self.dao = BoardDao()

    def addBoard(self, board):
        self.dao.insert(board)

    def getAll(self):
        return self.dao.selectAll()

    def getByNum(self, num):
        return self.dao.selectByNum(num)

    def editContent(self, board):
        self.dao.update(board)

    def delByNum(self, num):
        self.dao.delete(num)

