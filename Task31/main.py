def fibon(n):
    if n in [1,2]:
        return 1
    return fibon(n-1) + fibon(n-2)
n = int(input())

listFib = []
for i in range(1, n):
    listFib.append(fibon(i))
print(listFib)