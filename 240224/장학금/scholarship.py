m, f = map(int, input().split())

if m < 90:
    print(0)
else:
    if f >= 95:
        print(100000)
    else:
        print(50000)