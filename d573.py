while True:
    try:
        n = int(input())
        a = [0] * 100010
        for _ in range(n):
            b = list(map(int, input().split()))
            for i in range(2, len(b)):
                a[b[i]] = b[0]
        target = int(input())
        print(a[target])
    except:
        break