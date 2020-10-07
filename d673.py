N = 1
while True:
    n = int(input())
    if n < 0:
        break
    print('Case ' + str(N) + ':')
    N += 1
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(12):
        if b[i] <= n:
            print('No problem! :D')
            n -= b[i]
        else:
            print('No problem. :(')
        n += a[i]