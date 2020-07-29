import calendar

while True:
    try:
        y = int(input())
        cy = calendar.isleap(y)
        print("a leap year" if cy else "a normal year")
    except:
        break