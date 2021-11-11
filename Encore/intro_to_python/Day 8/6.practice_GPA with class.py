"""
#나의 작업물

class Student:
    def __init__(self):
        self.name = ''
        self.num = 0
        self.kor = 0
        self.eng = 0
        self.math = 0
        self.total = 0
        self.avg = 0

    def totalScore(self):
        return self.kor + self.eng + self.math

    def avgScore(self):
        sum = self.totalScore()
        return sum / 3

    def printData(self):
        print(f'{self.num}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}')


s = []


def enterData(i):
    s.append([])
    s[i] = Student()
    s[i].num = i + 1
    s[i].name = input('이름:')
    s[i].kor = int(input('국어 점수:'))
    s[i].eng = int(input('영어 점수:'))
    s[i].math = int(input('수학 점수:'))
    s[i].total = s[i].totalScore()
    s[i].avg = s[i].avgScore()


def repeat():
    while True:
        choice = input('학생 정보를 계속해서 입력하시겠습니까? y/n')
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print('잘못된 입력입니다')


def main():
    i = 0
    flag = True
    while flag is True:
        enterData(i)
        flag = repeat()
        i += 1
    print('\n======성적 처리 결과======')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균')
    for j in range(0, i):
        s[j].printData()


main()

"""

#강사님의 작업 결과

class Student:
    def __init__(self):
        self.name = ''
        self.num = 0
        self.kor = 0
        self.eng = 0
        self.math = 0
        self.total = 0
        self.avg = 0

    def setData(self, name, num, kor, eng, math):
        self.name = name
        self.num = num
        self.kor = kor
        self.eng = eng
        self.math = math

    def calc(self):  # 합계 구하는 것과 평균 구하는 것을 굳이 별도의 함수로 지정할 필요없이 하나로 합쳐서 해도된다!
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3

    def printData(self):
        print('name:', self.name)
        print('num:', self.num)
        print('kor:', self.kor)
        print('eng:', self.eng)
        print('math:', self.math)
        print('total:', self.total)
        print('avg:', self.avg)

def main():
    #클래스 타입의 변수는 먼저 생성해야 사용가능
    s1 = Student()  #객체 생성
    s1.name = 'aaa'
    s1.num = 1
    s1.kor = 45
    s1.eng = 56
    s1.math = 67
    s1.calc()
    s1.printData()

    s2 = Student()
    s2.setData('bbb', 2, 87, 67, 65)
    s2.calc()
    s2.printData()
