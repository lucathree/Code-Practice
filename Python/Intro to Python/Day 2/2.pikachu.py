'''
피카츄
hp - 초기값 30. 0이 되면 죽음, 게임오버
exp - 기본 0
lv - 경험치 20마다 레벨 1 증가

해야되는 것:
hp 감소, 0이 됐을 때 게임 종료시키기
exp 증가, 레벨업 체크
'''
print('피카츄를 키워보자!')
hp = 30
exp = 0
lv = 1
while True:
    print('\n피카츄: lv',lv,'/ hp',hp,'/ exp',exp)
    menu = int(input('1.밥먹기 2.잠자기 3.놀기 4.운동하기 5.종료'))
    if menu == 1:
        print('피카츄는 밥을 먹었다.(hp +5)')   #hp 5증가
        hp+=5
        if hp>30:
            hp=30
    elif menu == 2:
        print('피카츄는 잠을 잤다. (hp +10)')      #hp 10증가
        hp += 10
        if hp > 30:
            hp = 30
    elif menu == 3:
        print('피카츄는 즐거운 시간을 보냈다. (hp -5  exp +7)')     #hp 5감소, exp 7증가
        hp-=5
        exp+=7
        if hp <= 0:
            print('피카츄는 너무 신나게 놀다가 죽고말았습니다ㅠㅠ')
            break
        elif exp >= 20:
            lv += 1
            exp -= 20
            print('레벨업!')
    elif menu == 4:
        print('피카츄는 운동을 했다. (hp -15  exp +15)')       #hp 15감소, exp 15증가
        hp-=15
        exp+=15
        if hp <= 0:
            print('운동을 하던 피카츄는 힘이 다해 죽고말았습니다ㅠㅠ')
            break
        elif exp >= 20:
            lv += 1
            exp -= 20
            print('레벨업!')
    elif menu == 5:
        end = input('게임을 종료하시겠습니까?(Y/N)')
        if end == 'Y':
            break
        elif end == 'N':
            continue
        else:
            print('잘못된 선택입니다.')
            continue
    else:
        print('잘못된 선택입니다.')
print('게임이 끝났습니다.')
