n = list(map(int, input().split()))
count = 0
for i in range(len(n) - 1):
    if n[i] < n[i+1]:
        count += 1
print(count)


# Второе решение

print(sum(n[i] > n[i - 1] for i in range(1, len(n))))
