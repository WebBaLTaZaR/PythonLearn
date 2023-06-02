n = int(input("введите количество ячеек: "))
count = int()
maxCount = int()

for n in range(n):
    temp = int(input("Введите температуру: "))
    if temp > 0:
        count += 1
    else:
        count = 0
    if count > maxCount:
        maxCount = count
print(maxCount)    