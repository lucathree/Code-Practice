#성적처리 프로그램
#번호, 이름, 국어, 영어, 수학, 총점, 평균
#번호는 자동할당, 나머지 이름,국,영,수만 입력. 총 세사람
#딕셔너리 안에 딕셔너리를 포함

datas={}                                #번호를 키로 가지는 딕셔너리
num=1
titles = ['번호', '이름', '국어', '영어', '수학', '총점', '평균']

for i in range(0,3):
    s={}                                #각 항목을 키로 가지는 딕셔너리 속의 딕셔너리, 루프를 돌 때마다 초기화
    total=0                             #총점을 구하기 위한 변수
    for j in range(1,5):                #이름,국,영,수 4개를 입력받기 위해 레인지를 (1,5)로 설정
        val = input(titles[j])          #각 항목 명을 프린트한 후 값을 입력받는다
        if j!=1:                        #이름을 제외시키기 위해
            val = int(val)              #입력받은 값을 str에서 int로 변환
            total += val                #루프가 돌 때마다 점수 합산
        s[titles[j]]=val                #딕셔너리s에 titles[j]의 값을 키로 가지는 값 val 입력
    s[titles[j+1]]=total                #딕셔너리s에 '총점'(titles[j+1], j는 현재 4)을 키로 가지는 값으로 total 입력
    s[titles[j+2]]=total/3              #딕셔너리s에 '평균'을 키로 가지는 값으로 평균(total/3) 입력
    datas[num]=s                        #딕셔너리datas에 num을 키로 가지는 값으로 딕셔너리s를 입력
    num+=1                              #키가 될 번호를 루프가 돌때마다 1씩 올림
print(datas)

#성적처리 결과 출력시키기
for i in range(0,7):
    print(titles[i], end='\t')          # 리스트 titles에서 i번째 값을 출력하도록 반복
print()

for i in datas:                         #딕셔너리 datas의 키를(1, 2, 3) 변수 i의 값으로 반복해서 호출
    print(i,end='\t')                   #'번호' 값을 출력, end='\t' 로 다음에 오는 출력 내용이 오른쪽으로 이어지도록 함
    for j in s:                         #딕셔너리 s의 키를('이름', '국어', '영어', '수학', '총점', '평균') 변수 j의 값으로 반복해서 호출
        print(datas[i][j],end='\t')     # 딕셔너리 datas의 i번 줄, j번 방 값을 출력. (예, datas[1]['이름'] 은 datas 안에 있는 또 다른 딕셔너리 s에서 '이름'을 키로 가지고 있는 값이 됨)
    print()                             #루프가 한번 끝나면 출력 결과 줄바꿈

"""
#########강사님 출력 방법#########
for i in titles:
    print(i, end='\t')
print()

nums = datas.keys()
for i in nums:
    dic = datas[i]
    for key in titles:
        if key=='번호':
            print(i, end='\t')
        else:
            print(dic[key], end='\t')
    print()
"""