a = input("Введите 6 значное число: ")
while len(a) != 6:
    a = input("Введите 6 значное число!!!: ")
a = int(a)

index = 0
b = int()
c = int()
while index != 3:
    b += a % 10
    print(b)
    a = a // 10
    index = index + 1
    
i = 0
while i != 3:
    c += a % 10
    print(c)
    a = a // 10
    i = i + 1

if b == c:
    print("yes")
else: print("no")