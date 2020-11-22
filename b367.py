#方法一
# n = int(input())
# for _ in range(n):
#     c, d = map(int, input().split())
#     a = []
#     for _ in range(c):
#         a.append(list(map(int, input().split())))
#     flag = True
#     for i in range(c):
#         for j in range(d):
#             if a[i][j] != a[c-1-i][d-1-j]:
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
