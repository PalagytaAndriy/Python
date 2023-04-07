nam1 = int(input("Введіть початок діапазона - "))
nam2 = int(input("Введіть кінець діапазона - "))

for nam1 in range(nam1,nam2 + 1):
    q = 0
    for j in range(1,nam1 + 1):
        if nam1 % j == 0:
            q += 1
    if q == 2:
        print(nam1, " ", end="\f")

