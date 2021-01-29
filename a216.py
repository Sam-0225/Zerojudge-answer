# def f(n):
#     if n == 1:
#         return 1
#     return n + f(n-1)
#
#
# def g(n):
#     if n == 1:
#         return 1
#     return n + f(n-1) + g(n-1)
#
#
# while True:
#     try:
#         a = int(input())
#         print(f(a), g(a))
#     except:
#         break

g = [0, 1]
while True:
    try:
        for i in range(2, 30001):
            g.append(int(g[i-1] + ((1 + i) * i / 2)))
        a = int(input())
        print(g[a] - g[a-1], g[a])
    except:
        break


# f = n + f(n-1)
# g = f(n) + g(n-1)
# 1 2 3  4  5  6  7  8   9   10
# 1 3 6  10 15 21 28 36  45  55
# 1 4 10 20 35 56 84 120 165 220
