import random

def make_map():
    tic_map = []
    for i in range(9):
        tic_map.append("-")
    return tic_map


def print_map(game_map):

    print('-----')
    print(game_map[0] + '|' + game_map[1] + '|' + game_map[2])
    print('-----')
    print(game_map[3] + '|' + game_map[4] + '|' + game_map[5])
    print('-----')
    print(game_map[6] + '|' + game_map[7] + '|' + game_map[8])
    print('-----')

def check_win(game_map):
    check = False
    if game_map[0] == game_map[3] == game_map[6]:
        check = True
    elif game_map[2] == game_map[5] == game_map[8]:
        check = True
    elif game_map[1] == game_map[4] == game_map[7]:
        check = True
    elif game_map[0] == game_map[1] == game_map[2]:
        check = True
    elif game_map[3] == game_map[4] == game_map[5]:
        check = True
    elif game_map[6] == game_map[7] == game_map[8]:
        check = True
    elif game_map[0] == game_map[4] == game_map[8]:
        check = True
    elif game_map[2] == game_map[4] == game_map[6]:
        check = True


game_map = make_map()
print_map(game_map)
a = 'o'
b = 'x'

ham = 0

while True:

    while True:
        if ham == 0:
            num = int(input("Enter the position : "))
            if game_map[num] == "-":
                game_map[num] = a
                print_map(game_map)
                ham = 1
                break
                check = check_win
                if check:
                    print("you win O")
                    break
            elif game_map[num] != "-":
                pass
        elif ham == 1:
            num = random.randrange(8)
            if game_map[num] == "-":
                game_map[num] = b
                print_map(game_map)
                ham = 0
                break
                check = check_win
                if check:
                    print("you win X")
                    break
            elif game_map[num] != "-":
                pass
        game_win_check = check_win(game_map)

        if game_win_check:
           break
