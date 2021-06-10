a,b,c = 1,2,3
print(a)
print(b)
print(c)

#튜플 생성
t1 = (1,2,3)
for i in t1:
    print(i, end=' ')
print()

for i in range(0, len(t1)):
    print(t1[i], end=' ')
print()

t2 = ('asd', 12, True, [3,4,5])
print(t2)

#빈 튜플 생성
t3 = ()
print(type(t3))

t4 = (1)        #끝에 콤마를 넣어주지 않으면 int로 인식한다
print(type(t4))

t5 = (1,)       #끝에 콤마를 넣어야 튜플 생성
print(type(t5))

#다차원 튜플
s1 = ((1,2,3), [4,5])
for i in range(0, 2):
    for j in range(0, len(s1[i])):
        print('s1[',i,'][',j,']=',s1[i][j], sep='')

for i in s1:
    print(type(i))
    for j in i:
        print(j, end=' ')
    print()

#요소 수정,삭제 불가
t1 = (1,2,3,4,[5,6,7])
#t1[0] = 10      #에러 발생. 생성할 때에만 대입연산자 사용이 가능하고 생성 이후에는 불가
print(t1)
t1[4][0] = 50       #튜플 안의 리스트는 값을 바꿀 수 있음
print(t1)
t1[4].append(8)     #튜플 안의 리스트에 값을 추가하는 것도 가능
print(t1)
del t1[4][1]        #튜플 안의 리스트는 값 삭제도 가능
print(t1)