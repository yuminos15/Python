#for i in range(1,10):
    #print("*"*i)

#for i in range(10,0,-1):
    #print("*"*i)

#a = 0
#while(a<11):
    #print("*"*a)
    #a = a + 1

#a = 10
#while(a>0):
    #print("*"*a)
    #a = a - 1

def find_prime(j):
    count = 0

    for i in range(2, j//2 + 1):
        if j % i == 0:
            count += 1
    return count

prime = []


for j in range(2,100):
    count = find_prime(j)
    if count == 0:
        prime.append(j)
    #else:
        #print("Not prime")
print(prime)
