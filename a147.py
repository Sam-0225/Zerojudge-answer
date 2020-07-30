while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(' '.join([str(n) for n in range(1, n) if n % 7 != 0]))
