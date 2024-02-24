a_age, a_sex = input().split()
b_age, b_sex = input().split()
a_age, b_age = int(a_age), int(b_age)

print(int(((a_age >= 19 or b_age >= 19) and (a_sex == "M" or b_sex == "M"))))