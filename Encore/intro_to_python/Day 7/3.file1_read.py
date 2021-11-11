'''
#파일입출력
#1.파일오픈
file = open(파일경로, [모드:기본은r])
open('a.txt','r')

#모드종류
#r(읽기, 파일 없으면 에러), w(쓰기, 파일이 없으면 새로생성. 있으면 파일 내용 지우고 새로씀), a(이어쓰기, 파일 없으면 새로쓰고 있으면 이어쓰기)
#t(텍스트), b(바이너리)
#r+(읽고쓰기), w+(읽고쓰기), a+(읽고쓰기)

#2.읽기/쓰기 작업
#읽기
read(size)  #size 크기만큼 파일에서 읽어서 반환
read()      #파일 전체 읽어서 반환
readline()  #한줄 읽어서 반환
#쓰기
write(출력값) #파일에 출력값을 씀
writelines(리스트, 튜플...) #리스트나 튜플에 들어있는 값들을 파일에 출력

#3.파일닫음 - 파일 사용이 끝나면 파일을 닫아야 한다
file.close()

#경로표현
1. 절대경로
    C:\\users\\clee0627\\... (역슬래쉬가 텍스트임을 인지시키기 위해 두번씩 넣어줘야함)
2. 상대경로
    현재 프로그램을 기준으로 해당 파일을 찾아감
    ./ 현재 디렉토리
    ../ 상위 디렉토리

    디렉토리명 -> 하위 디렉토리
    ./files/a.txt
    ../Day 6/6.names practice.py

'''

def open1():
    print('======1번======')
    file = open('./files/a.txt', 'r', encoding='utf-8')
    while True:
        s = file.read(3)  #한번에 3byte씩
        if s == '':       #더이상 읽을 것이 없을 때 멈춤
            break
        else:
            print(s, end='')
    print()
    file.close()

def open2():
    print('======2번======')
    file = open('./files/a.txt', 'r', encoding='utf-8')
    s = file.read() #한번에 전체 읽기
    print(s)
    file.close()

def open3():
    print('======3번======')
    file = open('./files/a.txt', 'r', encoding='utf-8')
    while True:
        s = file.readline()
        if s == '':
            break
        else:
            print(s)
    file.close()

def main():
    open1()
    open2()
    open3()

main()