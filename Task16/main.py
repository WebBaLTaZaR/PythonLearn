n = list(map(int, input().split()))
x = int(input())
count = 0
for i in n:
    if i == x:
        count += 1
print(count)

# Второй способ

print(sum(i == x for i in n)) #  list comprehensions