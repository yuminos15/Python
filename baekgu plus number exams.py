#132
#####
#####
#####

#133
'''a = ["A", "B", "C"]
i = 0
while i < len(a):
    print(a[i])
    i += 1'''

#136
'''for i in range(10, 31 ,10):
    print(i)'''
#141
'''a = [100, 200 ,300]
for i in a:
    print(i + 10)'''

#143
'''list = ["sk", "samsung", "lg"]
for i in list:
    print(len(i))'''

#144
'''a = ["dog", "cat", "parrot"]
for i in a:
    print(f"{i} {len(i)}")'''

#145
'''a = ["dog", "cat", "parrot"]
for i in a:
    print(i[0])'''

#151
'''a = [3, -20, -3, 44]
for i in a:
    if i < 0:
        print(i)'''

#152
'''a = [3, 100, 32 ,44]
for i in a:
    if i%3==0:
        print(i)'''
#153
'''a = [13, 21 ,12 ,14, 30, 18]
for i in a:
    if i %3 == 0 and i < 20:
        print(i)'''

#154
'''a = ["i","study","python","language"]
for i in a:
    if len(i) >= 3:
        print(i)'''

#155
'''list = ["A", "B", "c", "D"]
for i in list:
    if i.isupper():
        print(i)'''

#157
'''a = ["dog", "cat", "parrot"]
for i in a:
    print(i[0].upper() + i[1:])
    print(i.capitalize())'''

#158
'''a = ["hello.py", "ex01.py", "intro.hwp"]
for i in a:
    print(i.split(".")[0])'''

#159
'''a = ["intra.h", "intro.c", "define.h", "run.py"]
for i in a:
    if i.split(".")[1] == "h":
        print(i)'''

#160
'''for i in a:
    if i.split(".")[1] in ('h', 'c'):
        print(i)'''

#baekjoon 구구단
'''import random
a = random.randrange(1,9)
print(a)
for i in range(1,10):
    ham = a * i
    print(a , "*" , i , "=" , ham)
===============================
N = int(input)
for i in range(1,10):
    print(f"{N} + {i} = {N * i}")'''

#A+B - 3
'''import random
t = 5
for i in range(t):
    a, b = map(int, input().split())
    print(f"{a} + {b} = {a+b}")'''

#합
'''n = 5
ham = 1
for i in range(n):
    ham = ham + i
print(ham+i)'''
#=================
'''n = int(input())
s = 0
for i in range(i, n+1):
    s += i
print(s)'''
#==================
'''n = int(input())
print(int((n + 1) * n / 2))'''

# N jikgi
'''import random
n = random.randrange(0, 100000)
print(n)
for i in range(n+1):
    print(i)'''
# a+b - 7
'''t = 5
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")'''

#별 찍지- 1
'''n = int(input())

for i in range(1,n+1):
    print("*"*i)'''
#별 찍기 - 2
'''n = int(input())

for i in range(1,n+1):
    print(" " * (n-i) + "*" * i)'''

#X보다 작은 수
a = []
n, x = map(int, input().split())

a = list(map(int, input().split()))

for i in range(n):
    if a[i] < x:
        print (a[i])

for i in a:
    if i < x:
        print(i, end='')
