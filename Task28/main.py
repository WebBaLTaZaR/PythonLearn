a = int(input())
b = int(input())
def sumF(a,b):
    if b == 0:
        return a
    return sumF(a + 1, b - 1)
print(sumF(a,b))