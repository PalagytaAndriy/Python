import re

data = str(input('введіть Дату в формате ДД/ММ/ГГГГ = '))
clock = str(input('Введіть Время в формате ЧЧ:ММ = '))
fraza_1 = 'Description: need'
fraza_2 = 'Your message on'
manse = ''
pattern_clock = '^([01][0-9]|2[0-3]):([0-5][0-9])$'
pattern_mail = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
pattern_data = '(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[0-2])[/](19[0-9][0-9]|20[012][0-9])'
boo = bool((re.findall(pattern_data, data)))

if data[3] == '0' and data[4] == '1':
    manse = 'Січеня'
if data[3] == '0' and data[4] == '2':
    manse = 'Лютого'
if data[3] == '0' and data[4] == '3':
    manse = 'Березеня'
if data[3] == '0' and data[4] == '4':
    manse = 'Квітеня'
if data[3] == '0' and data[4] == '5':
    manse = 'Травеня'
if data[3] == '0' and data[4] == '6':
    manse = 'Червеня'
if data[3] == '0' and data[4] == '7':
    manse = 'Липеня'
if data[3] == '0' and data[4] == '8':
    manse = 'Серпеня'
if data[3] == '0' and data[4] == '9':
    manse = 'Вересеня'
if data[3] == '1' and data[4] == '0':
    manse = 'Жовтеня'
if data[3] == '1' and data[4] == '1':
    manse = 'Листопада'
if data[3] == '1' and data[4] == '2':
    manse = 'Груденя'

if bool((re.findall(pattern_data, data))) == True and bool((re.findall(pattern_clock, clock))) == True:
    print('\n')
    print(fraza_2 ,data[0:2], manse, data[6:10], 'at', clock, 'oc. can be written')
    print('Your Description: need ..')
else:
    print('\n')
    print('Ваш ввод Некоректний')