def main():
    print('프로그램 시작')

    try:
        #res = 3 / 0
        print('test1')      # 예외처리가 되고 나면 break를 만난 것 처럼 프로그램이 죽지는 않지만 그 뒤의 코드는 실행되지 않음
        #res = 'aaa' + 1
        print('test2')
        arr = [1, 2, 3]
        arr[3] = 4
    except ZeroDivisionError as e:
        print(e)
        print('0으로 나눌 수 없음')
    except TypeError:
        print('타입이 안맞음')
    except Exception as e:
        print(e)
    except:
        print('잡지못한 에러')
    else:
        print('예외가 발생하지 않았음')
    finally:
        print('예외 발생 유무와 상관없이 종료 전 항상 실행되는 블록')

    print('프로그램 종료')


main()
