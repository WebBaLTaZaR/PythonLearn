P = int(input("Введите сумму чисел: "))
S = int(input("Введите произведение чисел: "))
result = int()
for x in range(1, P):
    y = P - x
    if x * y == S:
        result = x, y

if result:
    print("Числа, которые задумал Петя: ", result[0], result[1])
else:
    print("Числа не найдены.")
