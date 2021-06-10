#####오늘의 과제#####
'''
함수를 이용하여 주소록 만들기(이메일 연습과 비슷)
한 사람의 정보 = (이름, 전화번호, 주소)

**기능**
1. 등록(이름중복안됨)
2. 검색(이름으로) → 정보출력. 없으면 없다고 알림
3. 수정(이름으로) → 전화, 주소 수정
4. 삭제(이름으로)
5. 전체출력
6. 종료
'''

#정보를 담을 최초 딕셔너리. 정보는 {‘이름’:[전화번호, 주소]} 형태로 관리
info = {}

#정보등록 기능
def enterInfo():
    while True:
        name = input('등록할 이름:')
        res = info.get(name)    #name을 키로 갖는 값 검색
        if res == None:         #name을 키로 갖는 값이 없을 때,
            info[name] = []     #새로운 키를 추가하고 그 값으로 빈 리스트를 생성
            break
        else:
            print('이미 등록된 이름입니다.')
    tel = input('전화번호:')
    address = input('주소:')
    info[name] = [tel, address]
    print(f'정보가 등록되었습니다: {name} / {tel} / {address}')

#이름검색함수. 검색, 수정, 삭제 기능에 반복해서 사용되어 별도 함수 지정.
def searchInfo(s_name):
    res = info.get(s_name)
    if res == None:
        print('검색결과가 없습니다.')
    else:
        return res

#정보검색 기능
def printInfo():
    name = input('검색할 이름:')
    res = searchInfo(name)
    if res != None:
        print(f'이름:{name} 전화번호:{res[0]} 주소:{res[1]}')

#정보수정 기능
def editInfo():
    name = input('정보를 수정할 이름:')
    res = searchInfo(name)
    if res != None:
        tel = input('새 전화번호:')
        address = input('새 주소:')
        info[name] = [tel, address]
        print(f'정보가 수정되었습니다: {name} / {tel} / {address}')

#정보삭제 기능
def delInfo():
    name = input('정보를 삭제할 이름:')
    res = searchInfo(name)
    if res != None:
        del info[name]
        print('정보가 삭제되었습니다.')

#전체출력
def showAll():
    print('이름 \t전화번호 \t주소')
    for i in info:
        print(i,info[i][0],info[i][1], sep='\t')

#메인메뉴
def main():
    while True:
        menu = input('1.등록 2.검색 3.수정 4.삭제 5.전체출력 6.종료')
        if menu == '1':
            enterInfo()
        elif menu == '2':
            printInfo()
        elif menu == '3':
            editInfo()
        elif menu == '4':
            delInfo()
        elif menu == '5':
            showAll()
        elif menu == '6':
            print('종료합니다.')
            break
        else:
            print('잘못된 입력입니다.')

main()