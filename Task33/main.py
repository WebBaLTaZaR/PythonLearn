import random
n = int(input())
s = [random.randint(1, 5) for _ in range(n)]
print(s)
max1 = max(s)
min1 = min(s)
print(*[min1 if i == max1 else i for i in s])