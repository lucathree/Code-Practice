import pymysql
import member.memModel as mem


class BoardVo:
    def __init__(self, num=None, writer=None, w_date=None, title=None, content=None):
        self.num = num
        self.writer = writer
        self.w_date = w_date
        self.title = title
        self.content = content

    def __str__(self):  #객체 설명. 원래는 클래스풀네임 & 참조값을 표시. 예) <member.memModel.MemVo object at 0x0000023C5B995850>
        return 'num:'+str(self.num)+' / writer:'+self.writer+' / w_date:'+str(self.w_date)+' / title:'+self.title+\
               ' / content:'+self.content


class BoardDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='boardproject', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, vo):
        self.connect()
        cur = self.conn.cursor()
        sql = 'insert into board(writer, w_date, title, content) values(%s, now(), %s, %s)'
        vals = (vo.writer, vo.title, vo.content)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectAll(self):
        boards = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from board'
        try:
            cur.execute(sql)
            for row in cur:
                boards.append(BoardVo(row[0], row[1], row[2], row[3], row[4]))
            return boards
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectByNum(self, num):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from board where num=%s'
        vals = (num,)
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()
            if row != None:
                return BoardVo(row[0], row[1], row[2], row[3], row[4])
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectByWriter(self, writer):
        boards = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from board where writer=%s'
        vals = (writer,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                boards.append(BoardVo(row[0], row[1], row[2], row[3], row[4]))
            return boards
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectByTitle(self, title):
        boards = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from board where title like %s'
        t = '%'+title+'%'
        vals = (t,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                boards.append(BoardVo(row[0], row[1], row[2], row[3], row[4]))
            return boards
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectByContent(self, content):
        boards = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from board where content like %s'
        c = '%'+content+'%'
        vals = (c,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                boards.append(BoardVo(row[0], row[1], row[2], row[3], row[4]))
            return boards
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def editBoard(self, vo):
        self.connect()
        cur = self.conn.cursor()
        sql = 'update board set title=%s, content=%s where num=%s'
        vals = (vo.title, vo.content, vo.num)
        try:
            line = cur.execute(sql, vals)
            self.conn.commit()
            return line
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def delBoard(self, num):
        self.connect()
        cur = self.conn.cursor()
        sql = 'delete from board where num=%s'
        vals = (num,)
        try:
            line = cur.execute(sql, vals)
            self.conn.commit()
            return line
        except Exception as e:
            print(e)
        finally:
            self.disconnect()


class BoardService:
    def __init__(self):
        self.dao = BoardDao()

    def addBoard(self):
        print('글작성')
        title = input('title:')
        content = input('content:')
        self.dao.insert(BoardVo(writer=mem.MemService.login_id, title=title, content=content))

    def getAll(self):
        print('글목록 확인')
        boards = self.dao.selectAll()
        for i in boards:
            print(i)

    def getByNum(self):
        print('글 번호로 검색')
        num = int(input('글번호:'))
        vo = self.dao.selectByNum(num)
        if vo == None:
            print('없는 글번호')
        else:
            print(vo)

    def printList(self, vo_list):
        if vo_list == None or len(vo_list) == 0:
            print('검색결과 없음')
        else:
            for i in vo_list:
                print(i)

    def getByWriter(self):
        print('글 작성자로 검색')
        writer = input('작성자:')
        vo_list = self.dao.selectByWriter(writer)
        self.printList(vo_list)

    def getByTitle(self):
        print('글 제목으로 검색')
        title = input('제목:')
        vo_list = self.dao.selectByTitle(title)
        self.printList(vo_list)

    def getByContent(self):
        print('글 내용으로 검색')
        content = input('내용:')
        vo_list = self.dao.selectByContent(content)
        self.printList(vo_list)

    def editBoard(self):
        print('글 수정')
        num = int(input('수정할 글 번호:'))
        vo = self.dao.selectByNum(num)
        if vo == None:
            print('없는 글번호')
        else:
            if mem.MemService.login_id == vo.writer:
                title = input('new title:')
                content = input('new content:')
                line = self.dao.editBoard(BoardVo(num=num, title=title, content=content))
                print(line, '줄이 수정됨')
            else:
                print('남의 글은 수정할 수 없음')

    def delBoard(self):
        print('글 삭제')
        num = int(input('삭제할 글 번호:'))
        vo = self.dao.selectByNum(num)
        if vo == None:
            print('없는 글번호')
        else:
            if mem.MemService.login_id == vo.writer:
                line = self.dao.delBoard(num)
                print(line, '삭제완료')
            else:
                print('남의 글은 삭제할 수 없음')