# a = int(input())
# b = 1000 - a
# coin = 0
coins = [500, 100, 50, 10]
change = 1400
total = 0


for i in range(len(coins)):
    coin = coins[i]
    #print(change // coin)
    if change // coin >= 1:
        total = total + change // coin
        change = change - coin * (change//coin)
        print(total, change)

#
# for i in range(len(coins)):
#     for i in range(0,3):
#         if b - coins[i] >= 0:
#             b = b - coins[i]
#             coin = coin + 1



    # elif b - 100 >= 0:
    #     b = b - 100
    #     coin = coin + 1
    # elif b - 50 >= 0:
    #     b = b - 50
    #     coin = coin + 1
    # elif b - 10 >= 0:
    #     b = b - 10
    #     coin = coin + 1

print(coin)