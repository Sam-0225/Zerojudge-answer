a = int(input())
for i in range(a):
    b = input()
    c = ''
    for j in b:
        if not j.isalpha():
            c += j
    if c[c.find('+')+1] == '0':
        c = c.replace('+0','+')
    elif c[c.find('-')+1] == '0':
        c = c.replace('-0', '-')
    elif c[c.find('*')+1] == '0':
        c = c.replace('*0', '*')
    elif c[c.find('/')+1] == '0':
        c = c.replace('/0', '/')
    elif c[c.find('%') + 1] == '0':
        c = c.replace('%0', '%')
    print(int(eval(c)))

