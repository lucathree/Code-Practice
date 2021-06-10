#파일의 읽고 쓰기 위치 제어
#tell(): 현재 위치 반환
#seek(off, whence): whence를 기준으로 off만큼 떨어진 위치로 이동. whence는 0(맨앞), 1(현재위치), 2(맨뒤)

def writeFile():
    f = open('./files/f.txt', 'w')
    s = 'abcdefghijklmnopqrstuvwxyz'
    f.write(s)
    f.close()

def readFile():
    f = open('./files/f.txt', 'rb')     #byte 단위로 이동하기 때문에 'rb'로 설정해줘야함
    s = f.read(5)                       #3바이트 읽음 - c
    print(s)
    print('현재위치:', f.tell())         #현재위치 3 알려줌
    f.seek(5,1)                         #현 위치에서 5이동
    s = f.read(1)                       #그 다음칸을 읽어서 'i'
    print('현재 위치에서 5이동:', s)
    f.seek(-2, 1)                       #i에서 뒤로 2칸 이동, g
    s = f.read(1)                       #g 다음칸을 읽어서 'h'
    print('현재 위치에서 -2이동:', s)
    f.seek(10, 0)                       #맨 앞에서부터 10칸 이동, j
    s = f.read(1)                       #그 다음칸을 읽어서 'k'
    print('맨 앞에서 10이동:', s)
    f.seek(-2, 2)                       #맨 뒤에서 뒤로 두칸 이동, x
    s = f.read(1)                       #그 다음칸을 읽어서 'y'
    print('맨 뒤에서 -2이동:', s)
    f.close()

def main():
    writeFile()
    readFile()

main()