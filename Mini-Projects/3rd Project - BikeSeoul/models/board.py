import pymysql


class Board:
    def __init__(self, num=None, writer=None, title=None, content=None, w_date=None):
        self.num = num
        self.writer = writer
        self.title = title
        self.content = content
        self.w_date = w_date


class Reply:
    def __init__(self, num=None, reply_writer=None, board_num=None, content=None, w_date=None):
        self.num = num
        self.reply_writer = reply_writer
        self.board_num = board_num
        self.content = content
        self.w_date = w_date


class BoardDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', database='bikeseoul', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, board):
        self.connect()
        cur = self.conn.cursor()
        sql = "insert into board(writer, title, content, w_date) values(%s, %s, %s, now())"
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
        sql = "select * from board order by num desc"
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
            b = Board(row[0], row[1], row[2], row[3], row[4])
        except Exception as e:
            print(e)
        finally:
            self.disconnect()
            return b

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


class ReplyDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', database='bikeseoul', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, reply):
        self.connect()
        cur = self.conn.cursor()
        sql = "insert into reply(reply_writer, board_num, content, w_date) values(%s, %s, %s, now())"
        vals = (reply.reply_writer, reply.board_num, reply.content)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectByBoardNum(self, board_num):
        self.connect()
        cur = self.conn.cursor()
        sql = "select * from reply where board_num=%s"
        vals = (board_num,)
        cur.execute(sql, vals)
        rows = []
        for row in cur:
            rows.append(Reply(row[0], row[1], row[2], row[3], row[4]))
        self.disconnect()
        return rows

    def selectByWriter(self, reply_writer):
        self.connect()
        cur = self.conn.cursor()
        sql = "select * from reply where reply_writer=%s"
        vals = (reply_writer,)
        cur.execute(sql, vals)
        rows = []
        for row in cur:
            rows.append(Reply(row[0], row[1], row[2], row[3], row[4]))
        self.disconnect()
        return rows

    def delete(self, num):
        self.connect()
        cur = self.conn.cursor()
        sql = "delete from reply where num=%s"
        vals = (num,)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()


class ReplyService:
    def __init__(self):
        self.dao = ReplyDao()

    def addReply(self, reply):
        self.dao.insert(reply)

    def getBoardReply(self, board_num):
        return self.dao.selectByBoardNum(board_num)

    def getMyReply(self, id):
        return self.dao.selectByWriter(id)

    def delByNum(self, num):
        self.dao.delete(num)

