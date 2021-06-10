import calculation as calc     #패키지 파일에 있는 모든 함수를 불러옴
#from calculation import add     #패키지 파일에서 add함수 하나만 불러옴. 앞에 calc. 안 붙여도 됨
import file_control as fc


def main():
    res = calc.add(1, 2)
    print(res)

    res = calc.sub(1, 2)
    print(res)

    res = calc.mul(1, 2)
    print(res)

    res = calc.div(1, 2)
    print(res)

    base_path = '../../Day 7/files/'
    s = fc.file_read(base_path+'a.txt')
    print('file content:', s)
    fc.file_write(base_path+'g.txt', s)
    n = fc.file_read(base_path+'g.txt')
    print('g file content:', n)


main()
