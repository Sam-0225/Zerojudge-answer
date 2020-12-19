while True:
    try:

        a = input().split()
        b = ''
        count = 0
        for i in a:
            for j in range(len(i)-1):
                if not i[j].isalpha():
                    if i[j+1].isalpha():
                        count += 1

        print(len(a)+count)
    except:
        break