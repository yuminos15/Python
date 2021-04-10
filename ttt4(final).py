import random


def make_map():
    tic_map = []
    for i in range(9):
        tic_map.append("-")
    return tic_map


def print_map(nk_map):
    print('-----')
    print(nk_map[0] + '|' + nk_map[1] + '|' + nk_map[2])
    print('-----')
    print(nk_map[3] + '|' + nk_map[4] + '|' + nk_map[5])
    print('-----')
    print(nk_map[6] + '|' + nk_map[7] + '|' + nk_map[8])
    print('-----')


def check_win(game_map):
    check = False
    if game_map[0] == game_map[3] == game_map[6] and game_map[0] != '-':
        check = True
    elif game_map[2] == game_map[5] == game_map[8] and game_map[2] != '-':
        check = True
    elif game_map[1] == game_map[4] == game_map[7] and game_map[1] != '-':
        check = True
    elif game_map[0] == game_map[1] == game_map[2] and game_map[0] != '-':
        check = True
    elif game_map[3] == game_map[4] == game_map[5] and game_map[3] != '-':
        check = True
    elif game_map[6] == game_map[7] == game_map[8] and game_map[6] != '-':
        check = True
    elif game_map[0] == game_map[4] == game_map[8] and game_map[0] != '-':
        check = True
    elif game_map[2] == game_map[4] == game_map[6] and game_map[2] != '-':
        check = True
    return check

a = 'o'
b = 'x'
ham = 0
tic_map = make_map()


while True:
    if ham == 0:
        while True:
            num = int(input("Enter the position : "))
            if tic_map[num] == "-":
                tic_map[num] = a
                break
        ham = 1

    else:
        while True:
            num = random.randrange(0,8)
            if tic_map[num] == "-":
                tic_map[num] = b
                break
        ham = 0

    print_map(tic_map)
    game_win_check = check_win(tic_map)
    if game_win_check:
        print('win')
        break
    else:
        print("draw")
