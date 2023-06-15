n = int(input())
k = 0
if n in [2,3]:
    print("Число простое")
elif n == 1 or n % 2 == 0:
    print("Число не является простым")
else:
    for i in range(3, (n // 2) + 1,2):
        if n % i == 0:
            k += 1
    if k == 0:
        print("Число простое")
    else:
        print("Число не является простым")