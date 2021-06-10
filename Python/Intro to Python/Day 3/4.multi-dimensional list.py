
#다차원리스트

a = [1,2,3] #1차원

b = [[1,2,3], [4,5,6]] #2차원

print(b)
print(b[0])
print(b[0][1]) #0번째 줄의 1번째 방

for i in b:
    for j in i:
        print(j, end=',')
    print()

for i in range(0,len(b)):
    for j in range(0, len(b[i])):
        print(b[i][j], end=',')
    print()

#각 값을 10씩 증가시키기
for i in range(0, len(b)):
    for j in range(0, len(b[i])):
        b[i][j] *= 10
print(b)

#요소를 입력받아서 저장
for i in range(0, len(b)):
    for j in range(0, len(b[i])):
        b[i][j]=int(input('num:'))
print(b)

#성적처리 프로그램
#3명의 번호, 국, 영, 수 입력받아 가 학생의 총점, 평균 계산해서 결과 출력
#리스트형태 = [[1번, 국, 영, 수, 총점, 평균], [2번, 국, 영, 수, 총점, 평균], [3번, 국, 영, 수, 총점, 평균]]

score=[[0]*6,[0]*6,[0]*6]

for i in range(0,len(score)):
    snum=0
    for j in range(0,len(score[i])):
        if j == 0:
            score[i][j]=int(input('번호:'))
        elif j == 1:
            score[i][j]=int(input('국어:'))
            snum+=score[i][j]
        elif j == 2:
            score[i][j]=int(input('영어:'))
            snum+= score[i][j]
        elif j == 3:
            score[i][j]=int(input('수학:'))
            snum+= score[i][j]
        elif j == 4:
            score[i][j]=snum
        elif j == 5:
            avg=snum/3
            score[i][j]=avg

print('번호\t국어\t영어\t수학\t총점\t평균')
for i in range(0,len(score)):
    for j in range(0,len(score[i])):
        print(score[i][j],end='\t')
    print()

#두번째 방법
score=[[0]*6,[0]*6,[0]*6]
title=['번호:','국어:','영어:','수학:']

for i in range(0,len(score)):
    score[i][0]=int(input(title[0]))
    for j in range(1,4):
        score[i][j]=int(input(title[j]))
        score[i][4]+=score[i][j]
    score[i][5]=score[i][4]/3

print('번호\t국어\t영어\t수학\t총점\t평균')
for i in range(0,len(score)):
    for j in range(0,len(score[i])):
        print(score[i][j],end='\t')
    print()