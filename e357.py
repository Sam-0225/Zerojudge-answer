def f(x):
    if x == 1:
        return 1
    elif x % 2 == 0:
        return f(x/2)
    else:
        return f(x - 1) + f(x + 1)


print(f(int(input())))