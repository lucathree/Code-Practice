import pymysql


class UserVo:
    def __init__(self, id=None, pwd=None, nickname=None):
        self.id = id
        self.pwd = pwd
        self.nickname = nickname

    def __str__(self):
        return 'id:' + self.id + ' / 비밀번호:' + self.pwd + ' / 닉네임:' + self.nickname


class UserDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='1234', db='chargestation', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, vo):
        self.connect()  # db 연결
        cur = self.conn.cursor()  # 사용할 커서 객체 생성
        sql = 'insert into users values(%s, %s, %s)'
        vals = (vo.id, vo.pwd, vo.nickname)
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()

    def select(self, id):
        self.connect()  # db 연결
        cur = self.conn.cursor()  # 사용할 커서 객체 생성
        sql = 'select * from users where user_id=%s'
        vals = (id,)
        cur.execute(sql, vals)

        row = cur.fetchone()
        self.disconnect()
        if row != None:
            vo = UserVo(row[0], row[1], row[2])
            return vo


class UserService:
    login_id = None     # 로그인한 사람의 아이디를 보관할 정적 변수. None이면 로그인 안된 상태

    def __init__(self):
        self.dao = UserDao()

    def join(self):
        print('회원가입')
        id = input('id:')
        pwd = input('pwd:')
        nickname = input('nickname:')
        try:
            self.dao.insert(UserVo(id, pwd, nickname))
        except Exception as e:
            print(e)
        else:
            print('회원가입완료')

    def login(self):
        if UserService.login_id != None:     # 로그인 상태 확인
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
                UserService.login_id = id    # 로그인 성공했으므로 이 변수를 id 값으로 바꿔줌

            else:
                print('패스워드 불일치')

    def logout(self):
        print('로그아웃')
        UserService.login_id = None
