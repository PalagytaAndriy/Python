a = input("введіть шестизначне число = ")
if 6 == len(a):
    if (int(a[0])+int(a[1])+int(a[2]))==(int(a[3])+int(a[4])+int(a[5])):
        print("Це щасливе число")
    else:
        print("Це не щасливе число")
if len(a) > 6 or len(a) < 6:
    print("Невірне число")
