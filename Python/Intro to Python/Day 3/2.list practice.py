'''
index 함수를 사용하지 않고 탐색
리스트에 10개 숫자 입력받아서 저장

1. 최대값, 최소값 출력
2. 찾고싶은 값 입력받아서 그 값의 위치 출력. 없으면 없다고 출력
'''

a = [0]*10
for i in range(0,10):
    a[i] = int(input('숫자:'))
'''
maximum = a[0]
minimum = a[0]
for i in range(0,10):
    if maximum < a[i]:
        maximum = a[i]
    if minimum > a[i]:
        minimum = a[i]
print('최대값:',maximum,'/ 최소값:',minimum)

find = int(input('찾고싶은 값:'))
found = False
for i in range(0,10):
    if a[i] == find:
        location = i
        found = True
if found == True:
    print(location)
else:
    print('값이 없습니다.')




#참고사항
d = [2,4,6,8,10]
for idx, i in enumerate(d): # for 문에 변수를 두 개를 설정할 수 있고, enumerate() 함수를 사용하면 인덱스와 값을 같이 추출해준다
    print(idx,' ',i)

# 강사님 풀이
a = []
for i in range(0,10):
    a.append(int(input('num:')))

max = a[0] #초기 기준값
min = a[0] #초기 기준값
max_idx = -1
min_idx = -1

for idx, i in enumerate(a):
    if max < i:
        max=i
        max_idx=idx
    if min > i:
        min=i
        min_idx=idx
print('max:',max,'/ max위치:',max_idx)
print('min:',min,'/ max위치:',min_idx)

#순차 탐색
s_num = int(input('검색할 숫자:'))
flag = True #찾았나 표시, 못 찾았을 때 True
for idx, i in enumerate(a):
    if s_num == i:
        print(idx,'번에 위치')
        flag = False
        break
if flag:
    print('not found')
'''
#enumerate를 안 쓰는 방법
max = a[0]
for i in a:  #range를 쓰지 않고 in a 라고 해도 된다
    if max<i:
        max = i
print(max)

min = a[0]
for i in a:
    if min>i:
        min = i
print(min)

search = int(input('찾고싶은 값:'))
found = True
for i in range(0, len(a)):
    if a[i] == search:
        print('idx =',i)
        found = False
        break
if found:   #True 일 때는 그냥 if ____: 라고 해도 된다
    print('값이 없습니다.')