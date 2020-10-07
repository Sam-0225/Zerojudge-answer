x = int(input())
B = list(map(int, input().split()))
A = [0] * x
for i in range(x-1, 0, -1):
    A[i] = B[i] - B[i-1]
A[0] = B[0]
print(' '.join(map(str, A)))