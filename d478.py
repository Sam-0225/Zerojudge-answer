a = int(input().split()[0])
for _ in range(a):
    m = set(map(int, input().split()))
    n = set(map(int, input().split()))
    result = m.intersection(n)
    print(len(result))