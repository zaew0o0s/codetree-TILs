m = int(input())
if m > 2 and m < 12:
    if m < 6:
        print("Spring")
    elif m < 9:
        print("Summer")
    else:
        print("Fall")
else:
    print("Winter")