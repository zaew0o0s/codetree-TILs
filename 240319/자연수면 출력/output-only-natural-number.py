a, b = map(int, input().split())

if a > 0 and a % 1 == 0:
    for _ in range(b):
        print(a, end = '')
elif a <= 0:
    print(0)