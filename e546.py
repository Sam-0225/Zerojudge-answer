while True:
    # noinspection PyBroadException
    try:
        n, r = map(int, input().split())
        survive = set(list(map(int, input().split())))
        if n == r:
            print('*')
        else:
            deadList = set(list(range(1, n+1)))
            print(' '.join(map(str, sorted(list(deadList - survive)))))
    except Exception as e:
        break
