#파일쓰기
def write():
    file = open('./files/b.txt', 'w', encoding='utf-8')
    file.write('hello file')
    file.close()

def write2():
    file = open('./files/c.txt', 'w', encoding='utf-8')
    while True:
        s = input('메시지 입력(멈추려면 /stop):')
        if s == '/stop':
            break
        else:
            file.write(s+'\n')
    file.close()

def copy(src, dest): #파일복사(원본,경로)
    file = open(src, 'r', encoding='utf-8')
    file2 = open(dest, 'w', encoding='utf-8')
    s = file.read()  # 한번에 전체 읽기
    file2.write(s)
    file.close()
    file2.close()

def write3():  #이어쓰기
    file = open('./files/b.txt', 'a', encoding='utf-8')  #'a' -> 앞의 내용을 지우지 않고 작성한 내용 이어 붙이기
    file.write('가나다라마바사아자차카타파하에헤~으헤으헤으허허')
    file.close()

def write4():
    s = ['aaa\n', 'bbb\n', 'ccc\n']
    f = open('./files/e.txt', 'w', encoding='utf-8')
    f.writelines(s)
    f.close()

def with_open():  #파일오픈 with 블록. open() 동일, open()이 반환하는 파일 객체를 as 뒤 변수에 저장. 파일 닫기 생략
    with open('./files/e.txt', 'r') as f:
        while True:
            s = f.readline()
            if s == '':
                break
            else:
                print(s)

def main():
    with_open()


main()