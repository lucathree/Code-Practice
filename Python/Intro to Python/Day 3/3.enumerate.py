#enumerate - '열거하다'
#enumerate(): 반복자. 리스트에서 요소를 하나씩 순서대로 추출하는 것을 반복
#반복적으로 방번호와 요소를 추출해서 반환
a = [9,8,7,6,5]
for i in a:
    print(i)

for idx, i in enumerate(a):
    print(idx,' ',i)

#출력모양
#a[0]=9
#a[1]=8

for idx,i in enumerate(a):
    print('a[',idx,']=',i, sep='')

b = enumerate([10,20,30,40,50])
for idx, i in b:
    print(idx, i)