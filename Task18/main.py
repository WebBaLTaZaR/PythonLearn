import random
n = int(input())
num = list(map(int, input().split()))
x = int(input())
count = num[0]
minDif = abs(x - num[0])
for j in range(1, n):
	dif = abs(x - num[j])
	if dif < minDif:
		minDif = dif
		count = num[j]
print(count)