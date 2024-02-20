a, b, c = map(int, input().split())
sum = a + b + c
ave = int(sum / 3)
print(sum, ave, sum - ave, sep = '\n')