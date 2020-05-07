while True:
    try:
        a, n = map(int, input().split())
        print(pow(a, n, 10007))
    except:
        break