import random

maxD = int(input("Введите максимальный диапазон"))
minD = int(input("Введите минимальный диапазон"))
n = int(input())
s = [random.randint(1, 50) for _ in range(n)]
print(s)
new = []
ind = 0
for i in s:
    if s[ind] >= minD and s[ind] <= maxD:
        new.append(i)
    ind += 1
print(new)