# h, m = map(int, input().split())
# if m < 30:
#     h = (h + 2) % 24
#     m += 30
# else:
#     h = (h + 3) % 24
#     m = (m + 30) % 60
# print('{:0>2}'.format(h), ':', '{:0>2}'.format(m), sep='')

h, m = map(int, input().split())
if m < 30:
    h = (h + 2) % 24
    m += 30
else:
    h = (h + 3) % 24
    m -= 30
if len(str(h)) == 1:
    h = '0' + str(h)
if len(str(m)) == 1:
    m = '0' + str(m)
print(h, ':', m, sep='')
