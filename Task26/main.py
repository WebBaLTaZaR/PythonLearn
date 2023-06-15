a = int(input())
b = int(input())

def number(a,b):
    if b == 0:
        return 1
    return number(a,b - 1) * a

print(number(a,b))
