while True:
    try:
        a = input().lower()
        for i in range(len(a)):
            if a[i] != ' ':
                print(a[i].upper().join([a[:i], a[i+1:]]))
    except:
        break