import os

def init(path)
    if not os.path.isdir(path):
        os.mkdir(path)

def selectFile(path):
    flist = os.listdir(path)
    print('메모 파일 목록')
    for i in range(0, len(flist)):
        print(i,','+flist[i])
    while True:
        idx = int(input('선택할 파일의 번호를 입력하시오'))
        if 0 <= idx <= len(flist)-1:
            break
    return flist[idx]

def readFile(path):
    fname = selectFile(path)
    if fname == None:
        return
    print('선택한 파일명:',fname)
    f = open(path+fname, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    print(f'==={fname} 내용===')
    print(content)

def nameCheck(path, fname):
    flist = os.listdir(path)
    mode = 'w'
    if fname in flist:
        x = int(input('1.덮어쓰기 2.이어쓰기'))
        if x == 2:
            mode = 'a'

        


def main():
    memo_path = 'memo'
    init(memo_path)
    readFile(memo_path)

main()