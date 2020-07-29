
while True:
    try:
        n, m = map(int, input().split())
        count = 0
        total = 0
        while True:
            total += n
            count += 1
            n += 1
            if total > m: #測資輸入可能有負數
                break
        print(count)
    except:
        break
