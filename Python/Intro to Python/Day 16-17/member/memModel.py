import pymysql


class MemVo:
    def __init__(self, id=None, pwd=None, name=None, email=None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email

    def __str__(self):
        return 'id:' + self.id + ' / pwd:' + self.pwd + ' / name:' + self.name + ' / email:' + self.email


class MemDao:  # members 테이블과 관련된 db 작업만 구현
    def __init__(self):
        self.conn = None  #커넥션 객체를 담을 멤버 변수

    # db연결함수. db 사용 전 로그인하는 작업을 수행
    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='boardproject', charset='utf8')

    # db에 담는 모든 함수
    def disconnect(self):
        self.conn.close()

    #def insert(self, id, pwd, name, email)
    def insert(self, vo):  #members 테이블에 한 줄 추가, 회원가입 정보를 저장
        self.connect()  # db 연결
        cur = self.conn.cursor()  # 사용할 커서 객체 생성
        #insert into member values(vo.id, vo.pwd, vo.name, vo.email)
        sql = "insert into members values(%s, %s, %s, %s)"
        vals = (vo.id, vo.pwd, vo.name, vo.email)
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()

    def select(self, id):
        self.connect()  # db 연결
        cur = self.conn.cursor()  # 사용할 커서 객체 생성
        sql = "select * from members where id=%s"
        vals = (id,) # 반드시 튜플을 사용해야하기 때문에 값이 하나라도 뒤에 ,를 붙여준다
        cur.execute(sql, vals)  # 쿼리 실행, 검색 결과가 cur에 저장
        row = cur.fetchone()  # cur 객체에서 검색된 한 줄 fetch, 검색 결과 없으면 None 반환
        self.disconnect()  # db를 미리 닫음
        if row != None:  # 검색된 결과가 있으면
            vo = MemVo(row[0], row[1], row[2], row[3])
            return vo

    def update(self, id, new_pwd):
        self.connect()  # db 연결
        cur = self.conn.cursor()  # 사용할 커서 객체 생성
        sql = "update members set pwd=%s where id=%s" # 변수가 들어갈 위치에 %s와 같은 포맷문자 지정
        vals = (new_pwd, id)
        cur.execute(sql, vals)  # 쿼리 실행, 검색 결과가 cur에 저장
        self.conn.commit()
        self.disconnect()

    def delete(self, id):
        self.connect()  # db 연결
        cur = self.conn.cursor()  # 사용할 커서 객체 생성
        sql = "delete from members where id=%s"  # 변수가 들어갈 위치에 %s와 같은 포맷문자 지정
        vals = (id,)
        cur.execute(sql, vals)  # 쿼리 실행, 검색 결과가 cur에 저장
        self.conn.commit()
        self.disconnect()


class MemService:  #제공할 기능 구현

    login_id = None  #로그인한 사람의 id보관. None이면 로그인이 안된 상태

    def __init__(self):
        self.dao = MemDao()

    def join(self):
        print('회원가입')
        id = input('id:')
        pwd = input('pwd:')
        name = input('name:')
        email = input('email:')
        try:
            self.dao.insert(MemVo(id, pwd, name, email))  #db에 id, pwd, name, email 저장
        except Exception as e:
            print(e)
        else:
            print('회원가입완료')

    def login(self):
        print('로그인')
        if MemService.login_id != None:
            print('이미 로그인 되어있습니다.')
            return
        id = input('id:')
        pwd = input('pwd:')
        vo = self.dao.select(id)
        if vo == None:
            print('없는 아이디')
        else:
            if pwd == vo.pwd:
                print('로그인 성공')
                MemService.login_id = id
            else:
                print('비밀번호가 틀렸습니다')

    def logout(self):
        print('로그아웃')
        if MemService.login_id == None:
            print('로그인부터 해주세요')
            return
        MemService.login_id = None

    def printMyInfo(self):
        print('내정보확인')
        if MemService.login_id == None:
            print('로그인부터 해주세요')
            return
        vo = self.dao.select(MemService.login_id)
        print(vo)

    def editMyInfo(self):
        print('내정보수정')
        if MemService.login_id == None:
            print('로그인부터 해주세요')
            return
        new_pwd = input('새 비밀번호:')
        self.dao.update(MemService.login_id, new_pwd)
        print('정보수정완료')

    def delMyInfo(self):
        print('회원탈퇴')
        if MemService.login_id == None:
            print('로그인부터 해주세요')
            return
        self.dao.delete(MemService.login_id)
        print('회원탈퇴완료')
        MemService.login_id = None
