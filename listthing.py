import random

def make_list():
    a = []
    for i in range(10):
        x = random.randrange(100)
        a.append(x)
    return a

a = make_list()
print(a)

def allign_list():
    for j in range(len(a)):
        b = j
        for i in range(j, len(a)):
            if a[b] > a[i]:
                b = i
        a[j], a[b] = a[b], a[j]
    return a

a = allign_list()
print(a)


