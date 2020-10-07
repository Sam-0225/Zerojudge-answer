while True:
    try:
        N = int(input())
        l = list(map(int, input().split()))
        while len(l) > 0:
            print(' '.join(map(str, l)))
            l.pop(0)
            l = l[::-1]
        print()
    except:
        break
