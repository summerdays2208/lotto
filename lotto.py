#로또 번호 추출
import random

def lotto_random():
    num_list = []
    for i in range(1, 46):
        num_list.append(i)
    # print(num_list)

    win_num_list = []
    for i in range(0,6):
        r_seed = random.randrange(0,len(num_list)) #랜덤으로 숫자뽑기
        win_num = num_list.pop(r_seed) #랜덤숫자를 리스트에서 뽑아서 win_num에 저장, 리스트에서는 삭제
        win_num_list.append(win_num) #다음 랜덤숫자를 뽑기위해 뽑았던 숫자는 win_num_list에 저장해두기
    win_num_list.sort() #숫자 정렬
    print(win_num_list)

    lotto = [7,11,16,21,27,33]
    lotto_bonus = 24

    point = 0
    for i in range(0,len(win_num_list)):
        for j in range(0,len(lotto)):
            if win_num_list[i] == lotto[j] :
                point += 1
    # print(point)

    point2 = 0
    for i in range(0,len(win_num_list)):
        if win_num_list[i] == lotto_bonus:
            point2 = 1
    # print(point2)

    if point == 3:
        print('5등')
    elif point == 4:
        print('4등')
    elif (point == 5) and (point2 == 0):
        print('3등')
    elif (point == 5) and (point2 == 1):
        print('2등')
    elif point == 6:
        print('1등')
    else:
        print('꽝')

for i in range(0,100):
    lotto_random()

