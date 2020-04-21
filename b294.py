D = eval(input())
number = list(map(int, input().split()))
answer = 0
for i in range(D):
    answer += (i + 1) * number[i]
print(answer)



