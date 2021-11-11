"""
문제
Test 클래스를 만들고
객체가 생성되는 것을 카운팅하시오
"""

class Test:
    count = 0  # 객체들이 공유해야 하는 값

    def __init__(self):
        Test.count += 1
        print(Test.count,'번째 객체 생성')

def main():
    a = Test()
    b = Test()
    c = Test()
    d = Test()

main()