import random
n = int(input())
m = int(input())
num = [random.randint(1, 50) for _ in range(n)]
num2 = [random.randint(1, 50) for _ in range(m)]
print(num)
print(num2)
common_elements = list(sorted(set(num) & set(num2)))
print(common_elements)