a, b, c = map(int, input().split())

print(int(a == min(a, b, c)), int(a == b and b == c))