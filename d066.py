while True:
    try:
        h, m = map(int, input().split())
        temp = h*60+m
        if 450 <= temp < 1020:
            print("At School")
        else:
            print("Off School")

    except:
        break