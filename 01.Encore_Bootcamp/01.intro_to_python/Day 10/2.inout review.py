import sys
import os

def stdTest():
    msg = sys.stdin.readline()  # 표준입력(키보드)로 한 줄 읽기
    sys.stdout.write('msg:'+msg+'\n')  # 표준출력(콘솔)로 한 줄 출력
    sys.stderr.write('에러 메시지 출력')  # 표준에러로 에러 출력

def fileRead(path):
    try:
        f = open(path, 'r', encoding='utf-8')  # 파일오픈
        x = f.read()  # 파일읽기, 파일에서 읽은 내용을 반환하여 변수 x에 저장
        print(x)  # x(파일에서 읽은 내용) 출력
        f.close  # 파일닫기
    except Exception as e:
        print(e)

def fileWrite(path, msg):
    try:
        f = open(path, 'w', encoding='utf-8')
        f.write(msg)
        f.close()
    except Exception as e:
        print(e)

def printDirList(path):
    if not os.path.isdir(path):  # 디렉토리 존재를 True, False 로 반환
        print('없거나 디렉토리가 아님')
        return
    fname = os.listdir(path)  # path 폴더에 있는 모든 파일이나 디렉토리 이름(문자열)을 모두 읽어서 리스트에 담아서 반환
    for file in fname:
        print(file)

def main():
    # stdTest()
    # fileWrite('a.txt', 'hello file\n')
    # fileRead('a.txt')
    printDirList('./')

main()