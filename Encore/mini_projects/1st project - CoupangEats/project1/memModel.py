import pymysql


class MemVo:
    def __init__(self, id=None, pwd=None, name=None, tel=None, email=None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.tel = tel
        self.email = email

    def __str__(self):
        return 'id:' + self.id + ' / 비밀번호:' + str(self.pwd) +\
               ' / 회원이름:' + self.name + ' / 전화번호:' + self.tel + ' / email:' + self.email


class MemDao:
    def __init__(self):
        self.conn = None

        # db 연결함수

    def connect(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='1234', db='coupangeats_project', charset='utf8')

        # db 연결 종료함수

    def disconnect(self):
        self.conn.close()

    def insert(self, vo):
        self.connect()  # db 연결
        cur = self.conn.cursor()  # 사용할 커서 객체 생성

        # 변수가 들어갈 위치를 지정 / 포맷문자(%s:문자열, %d:정수, %f:실수)
        sql = 'insert into members values(%s, %s, %s, %s, %s)'
        # 튜플로 위의 변수포맷문자에 들어갈 변수들을 순서대로 매칭시켜주어야 함
        vals = (vo.id, vo.pwd, vo.name, vo.tel, vo.email)
        cur.execute(sql, vals)

        self.conn.commit()
        self.disconnect()

    def select(self, id):
        self.connect()  # db 연결
        cur = self.conn.cursor()  # 사용할 커서 객체 생성

        sql = 'select * from members where member_id=%s'
        # 값 1개짜리 튜플을 설정 (execute 함수는 (str, tuple(list,dict))) 을 parameter로 받는다.)
        vals = (id,)
        cur.execute(sql, vals)

        row = cur.fetchone()        # cur 객체에서 검색된 한 줄 fetch
        self.disconnect()           # 미리 db를 닫음
        if row != None:             # fetchone에서 검색된 결과가 있으면
            # 그 한 줄의 id, pwd, name, tel, email 컬럼값으로 vo객체를 생성
            vo = MemVo(row[0], row[1], row[2], row[3], row[4])
            return vo               # 객체 vo를 반환

    def update(self, id, new_pwd, new_name, new_tel, new_email):  # 비밀번호, 이름, 전화번호, 이메일 변경
        self.connect()
        cur = self.conn.cursor()
        sql = 'update members set pwd=%s, name=%s, tel=%s, email=%s where member_id = %s'
        vals = (new_pwd, new_name, new_tel, new_email, id)
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()

    def delete(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'delete from members where member_id = %s'
        vals = (id,)
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()


class MemService:
    login_id = None     # 로그인한 사람의 아이디를 보관할 정적 변수. None이면 로그인 안된 상태

    def __init__(self):
        self.dao = MemDao()

    def join(self):
        print('회원가입')
        id = input('id:')
        pwd = input('pwd:')
        name = input('name:')
        tel = input('tel:')
        email = input('email:')
        try:
            # db에 id, pwd, name, tel, email 저장
            self.dao.insert(MemVo(id, pwd, name, tel, email))
        except Exception as e:
            print(e)
        else:
            print('회원가입완료')

    def login(self):
        print('로그인')
        if MemService.login_id != None:     # 로그인 상태 확인
            print('이미 로그인 중')
            return                          # 이미 로그인이 되어 있다면 메서드를 빠져나감

        id = input('id:')
        pwd = int(input('pwd:'))               # id, pwd 입력받음
        vo = self.dao.select(id)
        if vo == None:                      # 검색결과가 없는 경우
            print('없는 아이디')
        else:
            if pwd == vo.pwd:               # db의 패스워드와 입력한 패스워드가 일치하는 경우
                print('로그인 성공')
                MemService.login_id = id    # 로그인 성공했으므로 이 변수를 id 값으로 바꿔줌

            else:
                print('패스워드 불일치')

    def logout(self):
        print('로그아웃')

        MemService.login_id = None

    def printMyInfo(self):
        print('내정보확인')

        if MemService.login_id == None:  # 로그인 상태 확인
            print('로그인을 먼저 하시오')
            return

        vo = self.dao.select(MemService.login_id)
        print(vo)

    def editMyInfo(self):  # MemService.login_id로 새 pwd, 이름, 전화번호, 이메일 입력받아 수정
        print('내정보수정')
        if MemService.login_id == None:  # 로그인 상태 확인
            print('로그인을 먼저 하시오')
            return

        new_pwd = input('새 비밀번호:')
        new_name = input('변경할 이름:')
        new_tel = input('새 전화번호:')
        new_email = input('새 이메일:')
        self.dao.update(MemService.login_id, new_pwd,
                        new_name, new_tel, new_email)

    def delMyInfo(self):  # MemService.login_id로 삭제
        print('회원탈퇴')
        if MemService.login_id == None:  # 로그인 상태 확인
            print('로그인을 먼저 하시오')
            return
        else:
            vo = self.dao.select(MemService.login_id)
            pwd = int(input('당신의 비밀번호를 한번 더 입력하시오:'))
            if pwd == vo.pwd:               # db의 패스워드와 입력한 패스워드가 일치하는 경우
                self.dao.delete(MemService.login_id)
                print('삭제에 성공했습니다.')
                MemService.login_id = None  # 로그아웃 처리(아이디를 삭제했으므로)
            else:
                print('패스워드 불일치. 삭제 불가능')
