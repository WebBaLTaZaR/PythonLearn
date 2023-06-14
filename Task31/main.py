def fibon(n):
    if n in [0,1]:
        return 1
    return fibon(n-1) + fibon(n-2)
n = int(input())
print(fibon(n))
