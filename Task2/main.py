a = input("Введите 3-х значное число: ")
while len(a) != 3:
    a = input("Введите 3-х значное число!!!: ")

a = int(a)
b = int()
index = 0
while index != 3:
    b += a % 10
    index = index + 1
print(b)