import random
n = int(input())
m = int(input())
num = [random.randint(1, 50) for _ in range(n)]

num2 = [random.randint(1, 50) for _ in range(m)]
# print(num)
# print(num2)
print(set(num))
print(set(num2))
num3 = num & num2
print(num3)
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# common_elements = list(set(list1) & set(list2))

# print(common_elements)