n = int(input("Введите длину списка: "))
step = int(input("введите разность: "))
a1 = int(input("Введите первый элемент: "))
list = []
for i in range(n):
	an = a1 + (i * step)
	list.append(an)
print(list)