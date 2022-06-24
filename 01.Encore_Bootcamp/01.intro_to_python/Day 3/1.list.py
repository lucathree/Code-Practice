a = [1,2,3]  #list of int
b = ['sdf', 'qwer', 'dfg'] #list of str
c = [12.24, 34.45, 3.14] #list of float
d = [True, True, False] #list of bool

#a[3]=10 => 에러, 범위 밖의 인덱스
a.append(4) #방을 확장하고 값 저장
print(a)

#빈 리스트 생성
e = []
f = list() #리스트 함수로 생성

e.append('라인')
e.append('하루')
print(e)

#하나의 리스트에 다양한 타입의 값을 담을 수 있다. (권장하지는 않지만)
f.append('098')
f.append(34)
f.append(12.23)
print(f)

#리스트 요소 접근
for i in range(0,3): #i=인덱스(방번호)
    print(a[i])

for i in a:
    print(i)

for i in range(0, len(b)): #len(): 요소의 길이를 가져오는 함수. 여기서 len(b)=3
    print(b[i], end=' ')
print()

#숫자 10개를 입력받아서 리스트에 저장한 뒤 출력하라
g=list()
for i in range(0,10):
    g.append(int(input('숫자를 입력하세요:')))
print(g)

#또는
data=[0]*10 #리스트를 0으로 초기화한 방 10칸 생성
for i in range(0, len(data)):
    data[i] = int(input('숫자:')) #리스트의 값은 바꿀 수 있다
print(data)

#5명 학생의 점수를 입력받아 총점과 평균을 출력하라
score=list()
sum1=0
for i in range(0,5):
    score.append(int(input('점수를 입력:')))
    sum1+=score[i]
avg1=sum1/len(score)
print('총점:',sum1,'/ 평균:',avg1)

#사실 총합을 구해주는 함수가 존재함
s = sum(score)
print('sum 합:',s)


#변수와 마찬가지로 리스트도 요소를 변경(수정,삭제) 할 수 있다.
a = [1,2,3,4,5]
print(a)

a[2]=30 #요소 수정, 값 재할당
print(a)

del a[2] #삭제명령, 값을 삭제하고 초기화 시키는 것이 아니라 방 자체를 삭제시킨다
print(a)

del a[1:3] #범위로 삭제 (1~2)
print(a)

a.remove(1) #값을 찾아서 삭제, 없는 값일 경우 에러
print(a)

b = [2,7,4,5,3]
print(b.index(7)) #7이 위치한 인덱스를 출력
list.sort(b)  #리스트 정렬
print(b)
