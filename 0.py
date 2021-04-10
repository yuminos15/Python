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

game_map = make_map()
print_map(game_map)
a = 'o'

ham = 0

while True:
    if(ham % 2 != 0):
        a = 'x'
    elif ham % 2 == 0:
        a = 'o'
    while True:
        num = int(input("Enter the position : "))
        if game_map[num] == "-":
            game_map[num] = a
            print_map(game_map)
            ham = ham + 1
            break
        elif game_map[num] != "-":
            pass
    if game_map[0] and game_map[3] and game_map[6] == 'o':
        print("Yay u won")
        break











"""for i in range(100):
    if game_map[position] != 'o':
        game_map[position] = a
        print_map(game_map)
    elif game_map[position] == 'o':
        position = int(input("Enter the position : "))"""





