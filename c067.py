num = 0
while True:
    # noinspection PyBroadException
    try:
        n = int(input())
        if n == 0:
            break
        num += 1
        bricks = list(map(int, input().split()))
        m = sum(bricks)
        moves = 0
        for i in range(n):
            if bricks[i] > m/n:
                moves += bricks[i] - m/n
        print('Set #' + str(num) + '\nThe minimum number of moves is ' + str(int(moves)) + '.\n')
    except Exception as e:
        break
