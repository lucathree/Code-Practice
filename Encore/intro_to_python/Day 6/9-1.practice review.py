#이름, 전화, 주소
#members = [[이름, 전화, 주소],[이름, 전화, 주소],[이름, 전화, 주소]]
members = []
titles = ['name', 'tel', 'address']

#등록함수
def addMember():
    m = [0,0,0]
    print('새 멤버 등록')
    for i in range(0, len(m)):
        if i == 0: #이름 입력일 때
            while True:
                m[i] = input(f'{titles[i]}:')
                res = getByName(m[i])
                if res == None:
                    break
                else:
                    print('중복된 이름')
        else: #전화, 주소 입력
            m[i] = input(f'{titles[i]}:')
    members.append(m)

def getByName(name):
    for idx, i in enumerate(members):
        if name==i[0]:
            return idx,i

def printMember():
    print('멤버 검색')
    name = input('검색할 이름:')
    res = getByName(name)
    if res == None:
        print('Name not found')
    else:
        i = res[1]
        cnt = 0
        for j in i:
            print(titles[cnt],j)
            cnt+=1
        print()

def printAll():
    for i in members:
        cnt=0
        for j in i:
            print(f'{titles[cnt]}: {j}', end='  ')
            cnt+=1
        print()

def main():
    addMember()
    addMember()
    addMember()
    printAll()
    printMember()

main()