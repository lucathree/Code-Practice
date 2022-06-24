'''
PocketMon => 부모클래스. 상속이 목적인 클래스
hp
exp = 0
lv = 1

밥먹기: 밥먹음.
잠자기
운동하기
놀기
레벨업
상태출력

피카추(PocketMon) / 꼬부기(PocketMon) / 파이리(PocketMon)

생성자에서 hp는 캐릭터 적합하게 할당

재정의
밥먹기
잠자기
운동하기
놀기
레벨업
상태출력
'''
#상속과 다형성
class PocketMon: #상속이 목적이고 이 클래스로 객체생성 안할거임
    def __init__(self):
        self.name = ''
        self.hp = 0
        #모든 캐릭터의 시작값 동일
        self.exp = 0
        self.lv = 1

    #상속하기 위한 메서드이므로 간단히 출력문만 작성하였음. 실제 동작은 하위클래스에서 각 캐릭터에 맞게 구현
    def 밥먹기(self):
        print(self.name, ' 밥먹는다')#피카추:hp5증가, 꼬부기:hp8증가

    def 잠자기(self):
        print(self.name, ' 잠잔다')

    def 운동하기(self):
        print(self.name, ' 운동한다')

    def 놀기(self):
        print(self.name, ' 논다')

    def 레벨체크(self):
        print(self.name, ' 레벨체크')

    #모든 캐릭터가 동일하게 동작하므로 부모 클래스에 구현한것을 하위에서 그대로 사용
    def 상태정보(self):
        print(self.name, ' 상태정보 출력')
        print('hp:', self.hp)
        print('exp:', self.exp)
        print('lv:', self.lv)

class Picachu(PocketMon):
    def __init__(self):
        super().__init__()
        self.name = '피카추'
        self.hp = 30 #이 캐릭터의 hp초기값 할당

    def 밥먹기(self):
        super().밥먹기() #부모 클래스의 밥먹기()호출
        self.hp+=5

    def 잠자기(self):
        super().잠자기()
        self.hp += 10

    def 운동하기(self):
        super().운동하기()
        self.hp -= 10
        flag = self.hp>0 #살았나 확인한 값 flag에 할당
        if flag:
            self.exp += 8
            self.레벨체크()
        return flag #살았나 확인한 값

    def 놀기(self):
        super().놀기()
        self.hp -= 5
        flag = self.hp > 0
        if flag:
            self.exp += 3
            self.레벨체크()
        return flag

    def 레벨체크(self):
        if self.exp>=20: #exp 20마다 레벨 1 증가
            self.lv += 1
            print(self.name, '레벨 1증가')
            self.exp -= 20

    def 전기공격(self):
        print('백만볼트~~~')

class Gobook(PocketMon):
    def __init__(self):
        super().__init__()
        self.name = '꼬부기'
        self.hp = 20

    def 밥먹기(self):
        super().밥먹기()
        self.hp+=3

    def 잠자기(self):
        super().잠자기()
        self.hp += 5

    def 운동하기(self):
        super().운동하기()
        self.hp -= 8
        flag = self.hp>0
        if flag:
            self.exp += 5
            self.레벨체크()
        return flag

    def 놀기(self):
        super().놀기()
        self.hp -= 5
        flag = self.hp > 0
        if flag:
            self.exp += 3
            self.레벨체크()
        return flag

    def 레벨체크(self):
        if self.exp>=15:
            self.lv += 1
            print(self.name, '레벨 1증가')
            self.exp -= 15

    def 물대포(self):
        print('물대포')

class Piry(PocketMon):
    def __init__(self):
        super().__init__()
        self.name = '파이리'
        self.hp = 15

    def 밥먹기(self):
        super().밥먹기()
        self.hp+=15

    def 잠자기(self):
        super().잠자기()
        self.hp += 20

    def 운동하기(self):
        super().운동하기()
        self.hp -= 20
        flag = self.hp>0
        if flag:
            self.exp += 15
            self.레벨체크()
        return flag

    def 놀기(self):
        super().놀기()
        self.hp -= 15
        flag = self.hp > 0
        if flag:
            self.exp += 10
            self.레벨체크()
        return flag

    def 레벨체크(self):
        if self.exp>=30:
            self.lv += 1
            print(self.name, '레벨 1증가')
            self.exp -= 30

    def 불대포(self):
        print('불대포')

class Menu:
    def __init__(self, ch):
        self.ch = ch

    def run(self):
        flag = True
        while flag:
            m = input('1.밥먹기 2.잠자기 3.운동하기 4.놀기 5.상태확인 6.종료 7.특기공격')
            if m=='1':
                self.ch.밥먹기()
            elif m=='2':
                self.ch.잠자기()
            elif m=='3':
                flag = self.ch.운동하기()
            elif m=='4':
                flag = self.ch.놀기()
            elif m=='5':
                self.ch.상태정보()
            elif m=='6':
                flag = False
            elif m=='7':
                # isinstance(obj, class name) obj 객체가 class name으로 만들어진 객체냐? True/False반환
                if isinstance(self.ch, Picachu):
                    self.ch.전기공격()
                elif isinstance(self.ch, Gobook):
                    self.ch.물대포()
                elif isinstance(self.ch, Piry):
                    self.ch.불대포()

        if m=='4' or m=='3':
            print('캐릭터 사망')

        print('게임종료')

def main():
    print('포켓몬 게임 시작')
    m = input('캐릭터 선택\n1.피카추(기본) 2.꼬부기 3.파이리')
    ch = None
    if m=='2':
        ch = Gobook()
    elif m=='3':
        ch = Piry()
    else:
        ch = Picachu()

    ch.상태정보()
    mm = Menu(ch)
    mm.run()

main()