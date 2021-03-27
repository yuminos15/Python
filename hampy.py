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

def solutions(t, e, m):

    if game_map[t] == a and game_map[e] == a and game_map[m] == a:
        print("O has won")
    if game_map[t] == b and game_map[e] == b and game_map[m] == b:
        print("X has won")
    return game_map


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
            elif game_map[num] != "-":
                pass
        elif ham == 1:
            num = random.randrange(8)
            if game_map[num] == "-":
                game_map[num] = b
                print_map(game_map)
                ham = 0
                break
            elif game_map[num] != "-":
                pass
    if game_map[0] == a and game_map[3] == a and game_map[6] == a:
        print("O has won")
        break
    if game_map[2] == a and game_map[5] == a and game_map[8] == a:
        print("O has won")
        break
    if game_map[1] == a and game_map[4] == a and game_map[7] == a:
        print("O has won")
        break
    if game_map[0] == a and game_map[1] == a and game_map[2] == a:
        print("O has won")
        break
    if game_map[3] == a and game_map[4] == a and game_map[5] == a:
        print("O has won")
        break
    if game_map[6] == a and game_map[7] == a and game_map[8] == a:
        print("O has won")
        break
    if game_map[0] == a and game_map[4] == a and game_map[8] == a:
        print("O has won")
        break
    if game_map[2] == a and game_map[4] == a and game_map[6] == a:
        print("O has won")
        break
    #--------------------------------------------------------------
    if game_map[0] == b and game_map[3] == b and game_map[6] == b:
        print("X has won")
        break
    if game_map[2] == b and game_map[5] == b and game_map[8] == b:
        print("X has won")
        break
    if game_map[1] == b and game_map[4] == b and game_map[7] == b:
        print("X has won")
        break
    if game_map[0] == b and game_map[1] == b and game_map[2] == b:
        print("X has won")
        break
    if game_map[3] == b and game_map[4] == b and game_map[5] == b:
        print("X has won")
        break
    if game_map[6] == b and game_map[7] == b and game_map[8] == b:
        print("X has won")
        break
    if game_map[0] == b and game_map[4] == b and game_map[8] == b:
        print("X has won")
        break
    if game_map[2] == b and game_map[4] == b and game_map[6] == b:
        print("X has won")
        break
