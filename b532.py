a = int(input())
for i in range(a):
    b = input()
    c = ''
    for j in b:
        if not j.isalpha():
            c += j
    if c.find('+0'):
        c = c.replace('+0','+')
    elif c.find('-0'):
        c = c.replace('-0', '-')
    elif c.find('*0'):
        c = c.replace('*0', '*')
    elif c.find('/0'):
        c = c.replace('/0', '/')
    elif c.find('%0'):
        c = c.replace('%0', '%')
    print(int(eval(c)))

