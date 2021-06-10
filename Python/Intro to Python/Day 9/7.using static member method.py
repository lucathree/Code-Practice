#정적메서드 및 정적변수 활용 예 => 객체 생성없이 클래스에 제공하는 메서드(기능)을 사용하는 클래스
#API 기능 제공
#정적 클래스
class Math:
    #파이썬에서의 상수 정의 방법
    __pi = 3.14  # 변수 앞에 __붙이면 private 멤버변수 (클래스 밖에서 안보임)
    PI = pi

    def circleSize(r):
        return r*r*Math.PI

    def rectSize(w, h):
        return w*h

def main():
    print('pi:', Math.pi)
    w = Math.circleSize(5)
    print('원의 넓이:', w)
    w = Math.rectSize(5, 10)
    print('사각형의 넓이:', w)

main()