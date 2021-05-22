list = []
list.append(0)
list.append(1)

n = int(input("Enter The Number : "))

for i in range(0,n-1):
    ham = list[i] + list[i+1]
    list.append(ham)

print(list[n])


