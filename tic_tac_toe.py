import random

h = 0

f = open('ham.txt', 'r')
liens = f.readlines()
total_id = []
for line in liens:
    id, pwd = line.split(',')
    total_id.append(id)
f.close()


f = open("ham.txt", 'a')
print("__________Register__________")
id = input("enter the id : ")
pwd = input("and their pwd : ")

while h != 0:
    if id not in total_id:
        f.write('\n' + id + ',' + pwd)
        f.close()
    elif id in total_id:
        print("this id already exists")

print("____________Login____________")
input_id = input("Username: ")
input_pwd = input("Password: ")
tam = 6

from login import login_check

flag = login_check(input_id, input_pwd)
if flag:
    print("-------")
    print("Success")
    print("-------")
    tam = 0
else:
    print("Sorry, Try again")

from tictacfile import make_map

from tictacfile import print_map

from tictacfile import check_win

a = 'o'
b = 'x'
ham = 0

if tam == 0:
    print("____________Start_____________")
    tic_map = make_map()

    print_map(tic_map)

while True and tam == 0:
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