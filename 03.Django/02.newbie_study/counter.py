import time

def count():
    for i in range(1,100,1):
        print(f'프로그램 실행 후 {i}초 경과')
        time.sleep(1)

count()