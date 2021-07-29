import pymysql


class Member:
    def __init__(self, id=None, password=None, name=None, gender=None, age=None):
        self.id = id
        self.password = password
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'{self.id} / {self.password} / {self.name} / {self.gender} / {self.age}'


class MemberDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='bikeseoul', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, mem):
        self.connect()
        cur = self.conn.cursor()
        sql = "insert into member values(%s, %s, %s, %s, %s)"
        vals = (mem.id, mem.password, mem.name, mem.gender, mem.age)
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
        sql = "select * from member where id=%s"
        vals = (id,)
        cur.execute(sql, vals)
        row = cur.fetchone()
        self.disconnect()
        if row != None:
            mem = Member(row[0], row[1], row[2], row[3], row[4])
            return mem

    def update(self, mem):
        self.connect()
        cur = self.conn.cursor()
        sql = "update member set password=%s, name=%s, gender=%s, age=%s where id=%s"
        vals = (mem.password, mem.name, mem.gender, mem.age, mem.id)
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
        sql = "delete from member where id=%s"
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