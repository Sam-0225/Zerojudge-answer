def a(n):
    if n <= 100:
        return a(a(n + 11))
    else:
        return n - 10


while True:
    x = input()
    if int(x) == 0:
        break
    print('f91(' + x + ') =', str(a(int(x))))