# 사용자 정의 예외
class NumError(Exception):
    def __init__(self, msg):  # 생성자, 객체 초기화 함수
        self.msg = msg


def f1(num):  # 5이하의 숫자만 가능, 5보다 큰 숫자를 받으면 심각한 에러가 발생한다고 가정
    if num > 5:
        raise NumError('5보다 작거나 같아야 함')  # raise 예외객체 : 예외 발생 구문
    print(num)


def f2(num):
    if not isinstance(num, int):  # isinstace(a, type): a의 타입이 type인지 확인. 맞으면 True 아니면 False
        raise TypeError('num은 int여야 함')  # TypeError 객체를 생성하여 던짐
    return num+10


def main():
    try:
        #f1(10)
        #f1(4)
        f2('aaa')
    except NumError as e:
        print(e.msg)


main()