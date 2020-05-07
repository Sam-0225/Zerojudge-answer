import math


def isPrime(n):
    if n == 1: return 0
    u = n - 1
    t = 0
    while u % 2 == 0:
        u >>= 1
        t += 1
    sprp = [2, 7, 61]
    for sk in sprp:
        a = sk % n
        if a == 0 or a == 1 or a == n-1: continue
        x = pow(a, u, n)
        if x == 1 or x == n-1: continue
        for i in range(t-1):
            x = pow(x, 2, n)
            if x == 1: return 0
            if x == n-1: break
        if x != n-1: return 0
    return 1
while True:
    try:
        a, b = map(int, input().split())
        r = 0
        k = a // 6
        v = 1
        while v:
            for n in (k * 6 + 1, k * 6 + 5):
                if n < a: continue
                if n > b:
                    v = 0
                    break
                r += isPrime(n)
            k += 1
        if a <= 2 and b >= 2: r += 1
        if a <= 3 and b >= 3: r += 1
        print(r)
    except:
        break
