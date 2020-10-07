N = int(input())
A = list(map(int, input().split()))
acc = 0
for i in range(N):
    acc += A[i]
    print(acc, end=' ')

