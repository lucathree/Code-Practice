'''
피카츄 게임
hp - 초기값 30. 0이 되면 죽음, 게임오버 (hp 상한 없음)
exp - 기본 0
lv - 경험치 20마다 레벨 1 증가

기능: 밥먹기, 잠자기, 운동하기, 놀기, 생명체크, 경험치체크, 메뉴

해야되는 것:
hp 감소, 0이 됐을 때 게임 종료시키기
exp 증가, 레벨업 체크
'''
#기본상태 - 게임을 재시작 할 때마다 피카츄 상태를 초기화 시키기 위해 함수 작성. 한 번만 게임을 실행시킬거라면 함수로 만들 필요는 없는 것 같습니다.
def stats():
    global hp
    global exp
    global lv
    global alive    #피카츄 생사여부 판단용 변수. alive가 True인 동안만 게임이 진행되고, False가 되면 종료됩니다.
    hp = 30; exp = 0; lv = 1; alive = True

#밥먹기
def eat():
    global hp
    hp+=5
    print('피카츄는 밥을 먹었다.(hp +5)')

#잠자기
def sleep():
    global hp
    hp += 10
    print('피카츄는 잠을 잤다. (hp +10)')

#운동하기
def workout():
    global hp
    global exp
    hp -= 15
    exp += 15
    print('피카츄는 운동을 했다. (hp -15  exp +15)')

#놀기
def play():
    global hp
    global exp
    hp -= 5
    exp += 7
    print('피카츄는 즐겁게 놀았다. (hp -5  exp +7)')

#생명체크
def hpCheck(hp):
    global alive
    if hp <= 0:
        print('\nhp가 0이 되었습니다!\n피카츄는 생명을 다해 죽고말았습니다.\n')
        alive = False
    elif hp <= 10:  #낮은 hp 경고용. 재미로 만들었습니다ㅎㅎ
        print('피카츄의 hp가 너무 낮습니다! hp를 회복해주세요')

#경험치체크
def expCheck():
    global lv
    global exp
    if exp >= 20 and alive == True:  #피카츄가 죽었는데 레벨업이 되는 경우를 막기 위해 alive == True 조건 포함
        lv+=1
        exp-=20
        print('\n레벨업!')

#메뉴선택
def menu(num):
    if num == 1:
        eat()
    elif num == 2:
        sleep()
    elif num == 3:
        workout()
    elif num == 4:
        play()
    elif num == 5:
        global alive
        alive = False
    else:
        print('잘못된 선택입니다.')

#본 게임진행
def game():
    print('Game Start\n피카츄를 키워보자!')
    stats()     #피카츄 상태 초기화
    while alive == True:
        print('\n피카츄: lv', lv, '/ hp', hp, '/ exp', exp)    #피카츄의 현재 상태 확인
        num = int(input('1.밥먹기 2.잠자기 3.운동하기 4.놀기 5.종료'))
        menu(num)   #선택한 메뉴에 따라 동작 진행
        hpCheck(hp)     #동작 진행 후 피카츄의 hp 확인. hp가 0이 되면 alive = False 가 되고 루프종료
        expCheck()      #동작 진행 후 피카츄의 exp 확인, exp가 20 이상이면 레벨업 진행
    print('게임이 끝났습니다.')     #루프가 종료되면 게임이 끝났음을 출력

#게임 시작하기 - 피카츄가 죽은 뒤에도 게임 다시 시작가능
def start():
    played = False  #게임 플레이 여부 판단용 변수
    while True:
        if played == False:   #최초 플레이일 경우 played는 초기값대로 False
            gameon = input('게임을 시작할까요? y/n')
        else:   #played == True 일 경우, 게임을 한번 실행했다는 뜻이기 때문에 "다시" 실행할지 질문.
            gameon = input('게임을 다시 시작할까요? y/n')
        print()
        if gameon == 'y':   #게임 시작을 원할 경우
            played = True   #게임 플레이 여부를 True로 바꿔주고
            game()          #본 게임 진행
        elif gameon == 'n':
            print('게임을 종료합니다.')
            break           #게임 종료를 원할 경우 break를 통해 루프 종료
        else:
            print('잘못된 입력입니다.')

#메인
def main():
    print('★☆★☆피카츄 키우기에 오신 것을 환영합니다!★☆★☆')
    start()
    print('플레이해주셔서 감사합니다.')

main()

