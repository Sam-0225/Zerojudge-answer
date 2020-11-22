while True:
    try:
        a = input()[0]
        b = input()[0]
        print((26 + ord(b) - ord(a)) % 26)
    except:
        break