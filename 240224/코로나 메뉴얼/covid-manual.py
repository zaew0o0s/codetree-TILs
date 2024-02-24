x_sym, x_tem = input().split()
y_sym, y_tem = input().split()
z_sym, z_tem = input().split()
x_tem, y_tem, z_tem = int(x_tem), int(y_tem), int(z_tem)
emergency = 0

if x_sym == 'Y' and x_tem >= 37:
    emergency += 1
if y_sym == 'Y' and y_tem >= 37:
    emergency += 1
if z_sym == 'Y' and z_tem >= 37:
    emergency += 1

if emergency >= 2:
    print("E")
else:
    print("N")