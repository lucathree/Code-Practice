import os

def checkDir():
    if os.path.isdir('memo'):
        print('memo 디렉토리를 확인했습니다.')
    else:
        print('memo 디렉토리가 생성되었습니다.')
        os.mkdir('memo')
    os.chdir('memo')

def selectFile():
    flist = os.listdir('memo')
    print(----메모 리스트----)
    for i in range(0, len(flist))
        print

def textInput(file):
    print("----내용을 작성하세요 (멈추려면 '/stop' 입력)----")
    while True:
        s = input()
        if s == '/stop':
            break
        else:
            file.write(s+'\n')
    print('내용작성이 완료되었습니다.')

def writeMemo():
    print('=====메모쓰기=====')
    name = input('파일명을 입력하세요:')+'.txt'
    if os.path.isfile(name):
        print('같은 이름의 파일이 확인되었습니다.')
        sel = input('옵션을 선택하세요. 1.이어쓰기 2.덮어쓰기')
        if sel == '1':
            with open(name, 'a', encoding='utf-8') as f:
                textInput(f)
        elif sel == '2':
            with open(name, 'w', encoding='utf-8') as f:
                textInput(f)
        else:
            print('잘못된 선택입니다.')
    else:
        with open(name, 'w', encoding='utf-8') as f:
            textInput(f)

def readMemo():
    print('=====메모읽기=====')
    name = input('파일명을 입력하세요:') + '.txt'
    if os.path.isfile(name):
        print(f'({name})')
        with open(name, 'r', encoding='utf-8') as f:
            print(f.read())
    else:
        print('파일을 찾을 수 없습니다.')

def delMemo():
    print('=====메모삭제=====')
    name = input('파일명을 입력하세요:') + '.txt'
    if os.path.isfile(name):
        os.remove(name)
        print(name,'파일이 삭제되었습니다.')
    else:
        print('파일을 찾을 수 없습니다.')

def main():
    print('=====메모를 시작합니다=====')
    checkDir()
    while True:
        func = [writeMemo, readMemo, delMemo]
        menu = int(input("기능을 선택하세요: 1-쓰기 2-읽기 3-삭제 4-종료"))
        if 1 <= menu <=3:
            func[menu-1]()
        elif menu == 4:
            print('메모를 종료합니다.')
            break
        else:
            print('잘못된 선택입니다.')

main()