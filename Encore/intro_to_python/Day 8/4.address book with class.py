"""
주소록
클래스명: Member
멤버변수: id, pwd, name, email
기능: 멤버변수 출력
"""
class Member:
    def __init__(self, id, pwd, name='홍길동', email='default@mail.com'):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email

    def printMember(self):
        print('id:', self.id)
        print('password:', self.pwd)
        print('name:', self.name)
        print('email:', self.email,'\n')


def main():
    m1 = Member('lucathree', '1111', '이창민', 'clee0627@gmail.com')
    m1.printMember()

    m2 = Member(pwd='2222', name='홍찰찰', id='beatdrops01', email='gogo@hanmail.net')
    m2.printMember()

    m3 = Member('okie', '3333')
    m3.printMember()

    m4 = m3
    m4.name = '가나다'
    m4.email = 'abc@email.com'
    m4.printMember()
    m3.printMember()

main()