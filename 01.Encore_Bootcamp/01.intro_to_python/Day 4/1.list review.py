#1. a라는 이름의 리스트를 생성, 숫자 1,2,3,4,5로 초기화해서 생성하시오
a = []
for i in range(1,6):
    a.append(i)

#2. a의 요소를 하나씩 출력
for i in a:
    print(i, end=' ')
print()

#3. a의 인덱스가 2인 요소의 값을 13으로 변경하시오
a[2] = 13

#4. a의 요소중 짝수만 출력
for i in a:
    if i%2 == 0:
        print(i, end=' ')
print()

#5. a의 인덱스가 2인 요소를 삭제하시오
del a[2]

#6. 이름이 b인 2줄 3칸 리스트를 생성. 모두 0으로 초기화해서 생성
b = [[0]*3,[0]*3]
# b = [[0]*3]*2   이렇게 만들면 참조값이 복사가 되어서 내부 요소 값까지 복사되는 문제가 발생함
print(b)

#7. 0번줄의 2번방 요소를 10으로 변경
b[0][2] = 10

#8.b의 요소를 0번 줄은 [1,2,3], 1번 줄은 [4,5,6]으로 변경
for i in range(0,len(b)):
    for j in range(0,len(b[i])):
            b[i][j] = j+1+(i*3)

#9. b의 모든 요소 출력
for i in b:
    for j in i:
        print(j, end=' ')