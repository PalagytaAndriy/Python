

def swo():
    k = 0
    kk = 0
    if list == '':
        print('False')
        exit()


    for i in list:

        if i == '(':
            k += 1
        if i == ')':
            kk += 1
    if k == kk:
        print('True')
    else:
        print('False')

    print('( = ', k)
    print(') = ', kk)

list = str(input('Введіть строку - '))
print('-------------------------------')

swo()