d1 = {'name':'aaa', 'age':12, 'flag':True}
print(d1)
print(type(d1))

d2 = {1:'aaa', 2:'bbb', 3:'ccc'}
print(d2)
print(type(d2))

#딕셔너리 요소 접근 방법
print(d1['name'])
print(d1['age'])
print(d1['flag'])

print(d2[1])
print(d2[2])
print(d2[3])

#요소추가
d1['tel'] = 1234
print(d1)

d1['name'] = 'bbb'  #이미 있는 키로 값을 할당하면 값이 수정됨 (에러X)
print(d1)

#전체 항목 불러오기
items = d1.items()
print(items)
for i in items:     #딕셔너리 값들을 튜플로 변환해서 i로 호출. 이때 items는 튜플의 집합. type은 dict_items
    print(i)
print(type(items))

for idx, i in enumerate(items):     #딕셔너리 값들도 인덱스 존재, 불
    print(idx,' ',i)

#요소삭제
del d1['name']      #'name'키로 등록되어 있는 요소를 삭제
print(d1)

#딕셔너리 관련 함수
d1['name'] = 'aaa'
print(d1.get('name'))       #get(키): 키로 검색된 값을 반환

keys = d1.keys()        #딕셔너리의 키값들만 모아서 호출
print(keys)
vals = d1.values()      #딕셔너리의 값들만 모아서 호출
print(vals)

for k in keys:
    val = d1[k]
    print(k,':',val)

for i in d1:
    print(i)

d1.clear()      #딕셔너리 초기화
print(d1)