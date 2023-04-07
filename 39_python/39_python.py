import random

def binary_search(search, list):
    l = 0
    r = len(list)-1
    keyFound = False

    while (l <= r) and (keyFound==False):
        m = (l+r)//2

        if list[m] == search:
            keyFound = True
        elif list[m] > search:
            r = m - 1
        else:
            l = m + 1

    if keyFound:
        return m
    else:
        return -1

ls1 = [random.randint(0,10) for i in range(0,10)]
ls2 = [random.randint(-10,0) for y in range(0,10)]
ls3 = [random.randint(-10,10) for a in range(0,10)]
ls4 = [random.randint(-10,10) for b in range(0,10)]

print(f'first list: {ls1}\n'
      f'second list: {ls2}\n'
      f'third list: {ls3}\n'
      f'hourth list: {ls4}')

revers_list = []
ls5 = list(set(ls1)^set(ls2)^set(ls3)^set(ls4))

print(ls5)
choose_sort = int(input('1.sort ascending\n2.sort descending\nChoose: '))

if choose_sort == 1:
    ls5 = list(set(ls5))
    ls5.sort(key=int)
elif choose_sort == 2:
    revers_list = list(set(ls5)).copy()
    revers_list.sort(key=int, reverse=True)
    ls5 = revers_list
else:
    print('incorrect choice')
    choose_sort = input('1.sort ascending\n2.sort descending\nChoose: ')

print(f'five list: {ls5}')

choose_find = int(input('Enter your value: '))

find = binary_search(choose_find, ls5)
if find != -1:
    print(f'fined: {ls5[find]}\nindex: {find}')
else:
    print("Item is not found")
