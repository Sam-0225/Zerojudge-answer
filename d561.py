# round函數無法確實做到四捨五入
# print('%.2f' % round(eval(input()), 2))
f = input()
a = '0'
if int(f[f.find('.')+3]) >= 5:
    a = str(int(f[f.find('.') + 2])+1)
print(f[:f.find('.')+2] + a)

