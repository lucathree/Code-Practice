def printList(arr):
    for i in arr:
        print(i, end=' ')
    print()

#리스트 요소의 총합 반환 함수
def listSum(list):
    sum = 0
    for i in list:
        sum+=i
    return sum

#리스트의 최대값 반환 함수
def listMax(list):
    max = list[0]
    for i in list:
        if max < i:
            max = i
    return max

#리스트의 최소값 반환 함수
def listMin(list):
    min = list[0]
    for i in list:
        if min > i:
            min = i
    return min

def main():     #main함수, 프로그램의 시작점
    a = [1,2,3,4,5]
    printList(a)

    b=[9,8,7,6,6,5,4]
    printList(b)

    sa = listSum(a)
    print(f'a의 총합: {sa}')
    sb = listSum(b)
    print(f'b의 총합: {sb}')

    maxa = listMax(a)
    print(f'a의 최대값: {maxa}')
    maxb = listMax(b)
    print(f'b의 최대값: {maxb}')

    mina = listMin(a)
    print(f'a의 최소값: {mina}')
    minb = listMin(b)
    print(f'b의 최소값: {minb}')

main()  #main 호출, 시작점