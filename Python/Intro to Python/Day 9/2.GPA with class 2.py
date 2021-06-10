"""
# 방법 1
class Student:
    def __init__(self, name='', num=0, score=[]):
        self.name = name
        self.num = num
        self.score = score  # 국,영,수,총점,평균이 담길 리스트

    def calc(self):
        for i in range(0, 3):
            self.score[3] += self.score[i]

        self.score[4] = self.score[3]/3

    def printInfo(self):
        print(self.name, end='\t')
        print(self.num, end='\t')
        for i in self.score:
            print(i, end='\t')
        print()

def main():
    s1 = Student('aaa', 1, [67, 87, 89, 0, 0])  # 객체 생성, 메모리 할당, 메모리 초기화
    s1.calc()
    s1.printInfo()

main()
"""


# 방법 2
class Score:  # 점수와 관련된 정보만 담는 클래스
    def __init__(self, kor, eng, math):  # 멤버변수는 점수와 관련된 국,영,수,총,평
        self.kor = kor
        self.eng = eng
        self.math = math
        # 총점&평균 계산
        self.total = self.kor + self.eng + self.math
        self.avg = self.total/3

    def printScore(self):
        print(self.kor, end='\t')
        print(self.eng, end='\t')
        print(self.math, end='\t')
        print(self.total, end='\t')
        print(self.avg, end='\t')
        print()

class Student:  # Score를 포함한 학생의 정보를 담는 클래스. "포함관계"
    def __init__(self, name, num, score):
        self.name = name
        self.num = num
        self.score = score  # Score 객체, 포함관계

    def printMember(self):
        print(self.name, end='\t')
        print(self.num, end='\t')
        self.score.printScore()

def main():
    sc1 = Score(76, 54, 87)
    s1 = Student('aaa', 1, sc1)
    s1.printMember()

    s2 = Student('bbb', 2, Score(57, 98, 86))
    s2.printMember()

main()