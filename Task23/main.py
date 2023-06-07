n = list(map(int, input().split())) # list compre
count = 0
for i in range(len(n) - 1):
    if n[i] < n[i+1]:
        count += 1
print(count)