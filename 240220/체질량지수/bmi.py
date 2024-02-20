length, weight = map(int, input().split())
bmi = int(weight // ((length / 100) ** 2))
print(bmi)

if bmi > 25:
    print("Obesity")