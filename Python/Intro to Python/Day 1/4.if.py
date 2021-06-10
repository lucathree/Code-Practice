#조건문 if, else, elif
'''
a=10
b=13

if a>b:
    print('a는 b보다 크다')
if a==b:
    print('a는 b와 같다')
if a<b:
    print('a는 b보다 작다')


#합격,불합격 판단
testscore=int(input('점수를 입력해주세요:'))

if testscore>=60:
    print('합격')
else:
    print('불합격')



#짝수,홀수 구분
num = int(input('숫자를 입력하세요:'))

if num % 2 == 0 :
    print('짝수')
else:
    print('홀수')
'''
#나이,성별을 확인하여 성인 여성일 때만 통과시키기
#방법1
'''
age = int(input('나이:'))

if age >= 20:
    sex = input('성별(여자:f, 남자:m):')
    if sex == 'f' :
        print('입장')
    else:
        print('여성만 입장 가능합니다')
else:
    print('성인만 입장 가능합니다')

#방법2 (논리연산자 and 사용)
sex = input('성별(m또는f):')
age = int(input('나이:'))
if sex == 'f' and age >= 20:
    print('입장')
else:
    print('퇴장')

#elif
menu = int(input('select number:'))
if menu == 1:
    print('game start')
elif menu == 2:
    print('select character')
elif menu == 3:
    print('exercise')
elif menu == 4:
    print('end game')
else:
    print('wrong input')
'''
#점수를(0-100) 입력받아 학점을 출력. A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 60 미만
grade = float(input('학점:'))

if grade < 0 or grade > 100:
    print('잘못된 점수')
elif grade >= 90: # 정확하게는 'grade >= 90 and grade <= 100' 또는 '90<=score<=100' 도 가능
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')