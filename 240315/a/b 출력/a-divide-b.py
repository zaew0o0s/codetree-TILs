a, b = map(int, input().split())

print(f"{a //b}.", end = '')
a %= b

for _ in range(20):
    print((a * 10) // b, end = '')
    a = (a * 10) % b