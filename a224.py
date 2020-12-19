while True:
    try:
        x = input().lower()
        y = [0] * 26
        z = 0
        for i in range(len(x)):
            if x[i].isalpha():
                y[ord(x[i]) - 97] += 1
        for i in y:
            if i % 2 != 0:
                z += 1
        if z > 1:
            print('no...')
        else:
            print('yes !')
    except:
        break