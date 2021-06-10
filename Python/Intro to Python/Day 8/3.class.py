#객체지향프로그래밍
class Card:  # Card라는 이름의 타입을 정의함. 이 타입의 변수는 카드 1개의 정보를 담을 수 있다.
    '''
    def __init__(self):  # 첫번째 파라미터는 현재 객체의 참조값을 받는다. 이름은 self가 아니어도 됨 (그러나 대체적으로 self를 사용함)
        self.number = ''       # 멤버변수 표현은 앞에 'self.변수이름' 형태로 표현한다. 카드번호
        self.owner = ''            # 카드명의자
        self.pwd = ''         # 비밀번호
        self.comp = ''          # 카드회사
    '''
    def __init__(self, number, owner, pwd, comp):
        self.number = number
        self.owner = owner
        self.pwd = pwd
        self.comp = comp

    def printCard(self):
        print('number:', self.number)
        print('owner:', self.owner)
        print('pwd:', self.pwd)
        print('comp:', self.comp)

def main():
    x = 10      # 일반변수 정의: 변수이름 = 값
    """
    # 객체(클래스로 만든 변수). 값을 할당하기 전 먼저 생성자 호출을 해야 함
    c1 = Card()
    c1.number = '1234-5678-9010-1112'  # '.' 은 멤버접근 연산자
    c1.owner = '아무개'
    c1.pwd = '1111'
    c1.comp = '신한'

    c1.printCard()

    c2 = Card()
    c2.number = '9876-5432-1098-7654'
    c2.owner = '홍길동'
    c2.pwd = '2222'
    c2.comp = '국민'
    """
    c3 = Card('1111-2222-3333-4444', '김철수', '3333', '현대')
    c3.printCard()

    c4 = Card('5555-6666-7777-8888', '홍찰찰', '4444', '우리')
    c4.printCard()

main()