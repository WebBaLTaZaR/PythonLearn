n = int(input())
if n in [2,3]:
    print("Число простое")
elif n == 1 or n % 2 == 0:
    print("Число не является простым")
else:
    print("Число простое")