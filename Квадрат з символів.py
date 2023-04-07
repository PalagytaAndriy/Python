dovgina = int(input('Введіть довжину сторони квадрата = '))
zapovn = str(input('если она равна " 1 ", квадрат заполненный , если " 0 " , квадрат пустой = '))

def povnuy(dov):
    j = 0
    i = 0
    for i in range(dov):
        for j in range(dov):
            print('%', end=' ')
        print()

def pystuy(dov):
    j = 0
    i = 0
    k = 0
    for i in range(dov):
        for j in range(dov):
            if i == 0:
                print('%', end=' ')
            elif j == 0 and i != dov - 1:
                print('%',' '*(dov+dov-5),'%', end=' ')
            elif i+1 == dov:
                print('%', end=' ')
        print()

if zapovn == '1':
    povnuy(dovgina)
if zapovn == '0':
    pystuy(dovgina)
