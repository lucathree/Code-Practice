#재귀함수 - 자신을 호출하는 함수

#5! = 5*4*3*2*1
'''
def factorial(num): #재귀함수
    if num==1:
        return 1
    else:
        return num * factorial(num-1)

def fact2(num):     #재귀함수 대신 for 루프로 만든 함수
    res = 1
    for i in range(1,num+1):
        res *= i
    return res

def main():
    res = factorial(32)
    print('32!:',res)

main()
'''
#재귀함수를 통해 피보나치 수열을 숫자 100개까지 출력하시오
#피보나치 수열 : 1, 1, 2, 3, 5, 8, 13, 21, ... (앞의 두 수를 합한 값으로 이어짐)
# 1.재귀함수 사용  2.루프사용  3.리스트 사용

#재귀함수
def fibo1(num1, num2):
    num3 = num1 + num2
    num4 = num2 + num3
    print(num1,num2,end=' ')
    return fibo1(num3, num4)

def fibo1(num):
    if num <= 2:
        return 1
    else:
        return fibo1(num-1)+fibo1(num-2)

#루프사용
def fibo2(cnt):
    i, j, k = 1, 1, 0
    for x in range(1,cnt+1):
        if x < 3:
            print(1,end=' ')
        else:
            k = i+j
            print(k,end=' ')
            i = j
            j = k

fibo2(100)
print()

#리스트 사용
def fibo3(cnt):
    res = [1,1]
    for i in range(2, cnt+1):
        res.append(res[i-2]+res[i-1])
    return res

print(fibo3(100))