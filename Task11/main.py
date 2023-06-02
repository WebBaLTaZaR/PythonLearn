fib = int(input())

i1 = int(0)
i2 = int(1)
index = int(2)

while i1 <= fib:
    if i2 == fib:
        print(index)
        break
    i1, i2 = i2, i1 + i2
    index += 1
else: print(-1)