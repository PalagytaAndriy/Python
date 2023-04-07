qq = int(input('Введіть число для пошуку = '))
ww = str(input('Введіть " 1 " якщо відсортувати у зворотньому виді, якщо стандартно то нічого не вводьте = '))
a1 = [10, 2, 6, 22, 45]
a2 = [10, 5, 7, 11, 13]
a3 = [3, 9, 8, 8, 9, 9]
a4 = [1, 4, 5]
i = 0
j = 0
k = 0
bb = []
aa = a1 + a2 + a3 + a4

def sort_0():
    for j in range((len(bb))):
        for jj in range((len(bb) - j - 1)):
            if bb[jj] > bb[jj + 1]:
                temp = bb[jj]
                bb[jj] = bb[jj + 1]
                bb[jj + 1] = temp
    print(bb)

def sort_1():
    for j in range((len(bb))):
        for jj in range((len(bb) - j - 1)):
            if bb[jj] < bb[jj + 1]:
                temp = bb[jj]
                bb[jj] = bb[jj + 1]
                bb[jj + 1] = temp
    print(bb)

def Beenar_poshyk_0(list, keyitem):
    l = 0
    r = len(list) - 1
    keyFound = False
    while (l <= r) and (keyFound == False):
        m = (l + r) // 2
        if list[m] ==keyitem:
            keyFound = True
        elif list[m] > keyitem:
            r = m - 1
        else:
            l = m + 1
    if keyFound:
        print('\n','Те число що ми шукаємо на позиціі ','"', m,'"', 'в масиві')
        return m
    else:
        return -1

def Beenar_poshyk_1(list, keyitem):
    l = 0
    r = len(list) - 1
    keyFound = False
    while (l <= r) and (keyFound == False):
        m = (l + r) // 2
        if list[m] ==keyitem:
            keyFound = True
        elif list[m] < keyitem:
            r = m - 1
        else:
            l = m + 1
    if keyFound:
        print('\n','Те число що ми шукаємо на позиціі ','"', m,'"', 'в масиві')
        return m
    else:
        return -1




print(aa)
for i in range(len(aa)):
    k = 0
    for j in range(len(aa)):
        if aa[i] == aa[j]:
            k +=1
    if k == 1:
        bb.append(aa[i])
i = 0
for i in range(len(aa)):
    if aa[i] not in bb:
        bb.append(aa[i])
print(bb)

if ww == '1':
    sort_1()
    Beenar_poshyk_1(bb, qq)

if ww =='':
    sort_0()
    Beenar_poshyk_0(bb, qq)




