n = int(input("Введите количество бросков монетки: "))
count1 = int()
count0 = int()
for n in range(n):
	coin = int(input("Введите 1 либо 0: "))
	if coin == 0:
		count0 += 1
	elif coin == 1:
		count1 += 1
	elif coin > 1 or coin < 0:
		print("Начните заново, вы ввели не верное значение!")
		break
if count0 > count1:
	print('решка выпадает чаще, значит быстрее поменять орлов ')
elif count1 > count0:
	print('орёл выпадает чаще, значит быстрее поменять решку ')