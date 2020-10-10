#方法一
# n = int(input())
# for _ in range(n):
#     c, d = map(int, input().split())
#     a = []
#     for _ in range(c):
#         a.append(list(map(int, input().split())))
#     flag = True
#     for i in range(c*d//2):
#         for j in range(c*d//2):
#             if a[i][j] != a[c-i-1][d-j-1]:
#                 flag = False
#                 break
#     if flag:
#         print('go forward')
#     else:
#         print('keep defending')
#方法二
n = int(input())
for _ in range(n):
    c, d = map(int, input().split())
    a = []
    for _ in range(c):
        a.extend(list(map(int, input().split())))
    b = a[:]
    a.reverse()
    if a != b:
        print('keep defending')
    else:
        print('go forward')
