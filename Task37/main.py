def revers(n):
	if n == 0:
		return ''
	m = input()
	return revers(n - 1) + m

n = int(input())
print(revers(n))