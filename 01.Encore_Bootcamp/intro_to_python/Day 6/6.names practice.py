#emails = []
#이메일을 등록하고 검색하는 함수 (몇번 방에 있는지)

emails = []
def addEmail(email):  #등록하는 함수. 중복허용 안됨, 이름 입력받아 리스트 추가
    overlap = False
    for i in emails:
        if i == email:
            overlap = True
            break
    if overlap == False:
        emails.append(email)
    else:
        print('중복된 이메일입니다.')

def searchEmail(s_email):  #파라미터로 검색할 이메일을 받아서 emails 리스트에서 검색하여 있으면 인덱스 제공, 없으면 아무값도 반환안함
    res = emails.index(s_email)
    if res == None:
        return
    else:
        return res

def main():
    while True:
        email = input('이메일을 입력하세요. 종료하려면 0')
        if email == '0':
            break
        else:
            addEmail(email)
    while True:
        s = input('검색할 이메일을 입력하세요. 종료하려면 0')
        if s == '0':
            break
        else:
            res = searchEmail(s)
            if res == None:
                print('이메일이 없습니다')
            else:
                print('이메일 위치:', res,'/',emails[res])

main()
'''

#강사님 작성코드

emails=[]

def addEmail():
    while True:
        email = input('등록할 이메일:')
        res = searchEmail(email)
        if res == None:
            break
        else:
            print('중복된 이메일, 다시 입력하세요')
    emails.append(email)
    
def searchEmail(s_email):
    for idx, i in enumerate(emails):
        if i == s_email:
            return idx
        
def printEmail():
    email = input('검색할 이메일을 입력:')
    idx = searchEmail(email)
    if idx == None:
        print('없는 이메일')
    else:
        print(idx,'번째 방에 있음 /',emails[idx])
        
def printAll():
    print('등록된 이메일')
    for i in emails:
        print(i)

def main():
    while True:
        menu = input('1.등록 2.검색 3.전체출력 4.종료')
        if menu=='1':
            addEmail()
        elif menu=='2':
            printEmail()
        elif menu=='3':
            printAll()
        elif menu=='4':
            break

main()
'''