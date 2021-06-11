nums = []
x = 1

# 숫자를 nums 리스트에 저장
def addNum1():
    # x = 10  # 지역변수
    # print(x)    #global 전에 해당 변수가 있을 경우 에러 발생
    global x  # 전역변수로 x에 값을 할당할 것이니 지역변수로 x를 만들지 말라는 선언
    x = 20  # 전역변수 20으로 변경

    num = int(input('num:'))
    nums.append(num)  # 전역 객체를 사용하여 메서드 호출. global 필요 없음


def addNum2(num):  # 함수 호출할 때 값 하나를 괄호에 넣어서 호출해라
    nums.append(num)

def printNums():    #전역변수를 가져와서 출력만 하면됨. 파라미터 필요X
    print('숫자 개수:', len(nums))
    for i in nums:
        print(i, end=',')
    print()

# 탐색함수: 탐색한 결과 리턴
# 2개 (파라미터 있는 함수, 파라미터 없는 함수)

def searchNum1():
    num = int(input('찾을 숫자:'))
    idx = nums.index(num)
    print('위치:', idx)

def searchNum2(num):
    print('위치:', nums.index(num))

# 인덱스 함수를 쓰지 않고 구현

def searchNum3(num):
    for idx, i in enumerate(nums):
        if i == num:
            return idx

def searchNum4(num):
    for i in range(0, len(nums)):
        if nums[i] == num:
            return i

def searchNum5():
    num = int(input('찾을 숫자:'))
    idx = searchNum4(num)
    if idx == None:
        print('not found')
    else:
        print(idx,'위치에 있음')


# 삭제함수 (remove 함수를 쓰지 않고)

def delNum1():
    num = int(input('삭제할 숫자:'))
    idx = searchNum4(num)
    if idx == None:
        print('삭제할 숫자를 찾을 수 없습니다')
    else:
        del nums[idx]

def delNum2(num):
    print('삭제할 숫자:',num)
    idx = searchNum4(num)
    if idx == None:
        print('삭제할 숫자를 찾을 수 없습니다')
    else:
        del nums[idx]

def delNum3(num):
    if num in nums:     # in 연산자: 오른쪽의 리스트에서 왼쪽값이 포함되어 있으면 True, 없으면 False 반환
        nums.remove(num)
    else:
        print('삭제할 숫자를 찾을 수 없습니다')

def delNum4():
    num - int(input('삭제할 숫자:'))
    try:
        nums.remove(num)
    except:
        print('삭제할 숫자를 찾을 수 없습니다.')

