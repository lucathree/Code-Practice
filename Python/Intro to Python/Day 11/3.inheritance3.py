#학사관리 프로그램
class Person:
    def __init__(self):
        self.number = 0  #번호
        self.name = ''  #이름
        self.type = ''  #타입(교직원, 교수, 학생)
        self.dept = ''  #학과

    def printInfo(self):
        print('number:', self.number)
        print('name:', self.name)
        print('type:', self.type)
        print('dept:', self.dept)


class Student(Person):
    def __init__(self, number, name, dept):
        super().__init__()
        self.number = number
        self.name = name
        self.dept = dept
        self.type = '학생'
        self.subject = []

    def subReg(self, sub):  #수강신청 메서드
        self.subject.append(sub)

    def printSub(self):
        print('수강과목')
        for i in self.subject:
            print(i)

class Professor(Person):
    def __init__(self, number, name, dept):
        super().__init__()
        self.number = number
        self.name = name
        self.dept = dept
        self.type = '교수'
        self.course = []

    def addCourse(self, course):  # 담당과목 추가 메서드
        self.course.append(course)

    def printCourse(self):
        print('담당과목')
        for i in self.course:
            print(i)

class Faculty(Person):
    def __init__(self, number, name, dept):
        super().__init__()
        self.number = number
        self.name = name
        self.dept = dept
        self.type = '교직원'
        self.job = ''

    def setJob(self, job):
        self.job = job

    def printJob(self):
        print('담당업무:',self.job)

def main():
    s1 = Student(1, 'aaa', '컴퓨터공학')
    s1.subReg('전산학개론')
    s1.subReg('컴퓨터비전')
    s1.printInfo()
    s1.printSub()

    p1 = Professor(2, 'bbb', '전자공학')
    p1.addCourse('컴공개론')
    p1.addCourse('C언어')
    p1.printInfo()
    p1.printCourse()

    f1 = Faculty(3, 'ccc', '입학처')
    f1.setJob('학생등록관리')
    f1.printInfo()
    f1.printJob()

main()