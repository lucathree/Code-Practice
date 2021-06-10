#학습목표
#기본 입력/출력
#예외처리: 예외 발생시 프로그램이 중단되는 것을 막아 안정성 높임

'''
1.표준입출력(stdio)
sys.stdin: 표준입력
sys.stdout: 표준출력
sys.stderr: 표준에러

표준입출력 동작 예시 - print, input 함수가 없다면 이렇게 표준입출력을 진행한다
'''
import sys

def main():
    sin = sys.stdin     #키보드 입력 스트림
    sout = sys.stdout   #콘솔 출력 스트림
    serr = sys.stderr   #콘솔 에러 출력 스트림

    num = sout.write('문자를 입력하시오\n')     #write():출력스트림에 출력
    sout.write(str(num)+'개의 문자 출력됨\n')  #문자열로 변환
    s = sin.read(5)                         #read(size): 입력 스트림에서 size만큼 읽음. 버퍼
    sout.write('입력받은 값:'+s+'\n')
    sout.write('한줄을 입력하시오\n')
    sin.readline()
    s = sin.readline()
    sout.write('입력받은 값:'+s+'\n')
    serr.write('에러 메시지')

main()

'''
표준 입출력은 단방향. 입력은 입력만 가능하고 출력은 출력만 가능. 
input 함수는 이런 시스템 함수를 활용해서 만들어진 입출력이 혼합된 함수
'''

