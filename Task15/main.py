n = int(input("введите количество арбузов: "))
waterMelon = int(input("Введите вес первого арбуза: "))
maxCount = waterMelon
minCount = waterMelon
for n in range(n):
    waterMelon = int(input("Введите вес следующего арбуза: "))
    if waterMelon > maxCount:
        maxCount = waterMelon
    if waterMelon < minCount:
        minCount = waterMelon
print(maxCount)
print(minCount)