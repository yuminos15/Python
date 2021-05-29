import random

def make_random_list():
    list = []
    for i in range(10):
        x = random.randrange(100)
        list.append(x)

    return list


list = make_random_list()
print(list)

def compare_number():
    for j in range(9):
        for i in range(0,9):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

list = compare_number()

print(list)

# 3, 1, 100, 203, 10
#
# 1, 3, 100, 203, 10
#
# 1, 3, 10, 203, 100
#
# 1, 3, 10, 100, 203

