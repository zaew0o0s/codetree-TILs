a, b, c = map(int, input().split())

if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)
elif a < b and b > c:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if a > b:
        print(a)
    else:
        print(b)