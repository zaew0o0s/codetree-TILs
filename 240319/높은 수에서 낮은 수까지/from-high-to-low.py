a, b = map(int, input().split())

if a > b:
    for i in range(a - b + 1):
        print(a, end = ' ')
        a -= 1
else:
    for j in range(b - a + 1):
        print(b, end = ' ')
        b -= 1