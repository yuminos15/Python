# file i/o
# 절대경로 , 상대경로
# /home/namgil/test.txt
# ../namgil/test.txt
# 트리 구조

input_id = input("Username: ")
input_pwd = input("Password: ")


def login_check(input_id, input_pwd):
    f = open('test.txt', 'r')
    lines = f.readlines()
    flag = False
    for line in lines:
        temp = line.split('\n')[0]
        id, pwd = temp.split(',')
        if id == input_id and pwd == input_pwd:
            flag = True
            break
    return flag


flag = login_check(input_id, input_pwd)
if flag:
    print("Success")
else:
    print("Sorry, Try again")
