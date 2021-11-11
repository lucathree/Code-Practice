import pymysql

class Member:
    def __init__(self, id=None, pwd=None, name=None, email=None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email

    def __str__(self):
        return f'{self.id} / {self.pwd} / {self.name} / {self.email}'


class MemberDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, mem):
        self.connect()
        cur = self.conn.cursor()
        sql = "insert into members values(%s, %s, %s, %s)"
        vals = (mem.id, mem.pwd, mem.name, mem.email)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def select(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = "select * from members where id=%s"
        vals = (id,)
        cur.execute(sql, vals)
        row = cur.fetchone()
        self.disconnect()
        if row != None:
            mem = Member(row[0], row[1], row[2], row[3])
            return mem

    def selectAll(self):
        self.connect()
        cur = self.conn.cursor()
        sql = "select * from members"
        mems = []
        try:
            cur.execute(sql)
            for row in cur:
                mems.append(vo.Member(row[0], row[1], row[2], row[3]))
        except Exception as e:
            print(e)
        finally:
            self.disconnect()
            return mems

    def update(self, mem):
        self.connect()
        cur = self.conn.cursor()
        sql = "update members set pwd=%s, name=%s, email=%s where id=%s"
        vals = (mem.pwd, mem.name, mem.email, mem.id)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def delete(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = "delete from members where id=%s"
        vals = (id,)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()


class MemberService:
    def __init__(self):
        self.dao = MemberDao()

    def addMem(self, mem):
        self.dao.insert(mem)

    def getMem(self, id):
        return self.dao.select(id)

    def getMemAll(self):
        return self.dao.selectAll()

    def editMem(self, mem):
        self.dao.update(mem)

    def delMem(self, id):
        self.dao.delete(id)