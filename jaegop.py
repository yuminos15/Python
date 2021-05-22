m,n = map(int,input().split())

list = []
list.append(-1)
total = 0


for i in range(0,100):
    ham = i * i
    if m <= ham <= n:
        list.append(ham)
        total = total + ham


if total == 0:
    print(list[0])
else:
    print("최소:",list[1])
    print("total:",total)



