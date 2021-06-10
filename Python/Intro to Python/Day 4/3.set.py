#셋(set) = 집합

#셋 생성
s = {1, 2, 3}
print(s)
print(type(s))

s = {}  #딕셔너리도 중괄호를 사용하여 표현하기 때문에 이렇게 빈 셋을 만들려고 할 경우 셋이 아닌 딕셔너리가 된다.
print(type(s))

s = set()  #셋 함수를 이용해서 만들자
print(type(s))

#셋은 요소의 순서가 없기 때문에 인덱스도 없다. (s[1] 사용불가)
s = {3,5,1,3,2,3,5}  #중복을 허용하지 않기 때문에 중복된 값은 저장되지 않는다
for i in s:
    print(i)

s = {'aaa', 1, False}   #요소들은 다른 타입을 가질 수 있음
print(s)
#s = {1, 2, [3,4,5]}     #그러나 안에 있는 요소들은 변경이 되면 안되기 때문에 리스트를 요소로 가질 수는 없음 (에러 발생)

#셋에 요소 추가
s.add('bbb')    #add함수로는 한꺼번에 여러개 추가 불가
print(s)
a = [5,6,7]     #리스트를 넣는게 아니라 상수를 값으로 추가
s.update(a)     #요소 여러개 추가 시에는 update 사용.
print(s)

#요소 삭제
s.remove('aaa')     #없는 요소 삭제시 에러
print(s)
s.discard(1)   #없는 요소 삭제시 무시
print(s)

x = s.pop()     #값을 맨 앞부터 추출하여 셋으로부터 삭제
print(x, '가 삭제됨')
print(s)

s.clear() #모든 요소 삭제
print(s)

###############################
#합집합(union)
s1 = {1,2,3}
s2 = {3,4,5}

s3 = s1|s2
print(s3)

s4 = s1.union(s2) #s1과 s2의 유니온
print(s4)

#교집합(intersection)
s3 = s1 & s2
print(s3)

s4 = s1.intersection(s2)
print(s4)

#차집합(difference)
s3 = s1 - s2
print(s3)
s4 = s2 - s1
print(s4)

s5 = s1.difference(s2)
print(s5)
s6 = s2.difference(s1)
print(s6)