import json
from datetime import date

infoEmployee = ''


with open("Працівники.json", 'r') as json_file:
    firma = json.load(json_file)

def add_person():
    firs_name = input('Імя\n  --> ')
    last_name = input('Призвіще\n  --> ')
    age = input('Вік\n  --> ')
    tel = input('Тел\n  --> ')
    email = input('email\n  --> ')
    post = input('Посада\n  --> ')
    number_cabinet = input('Кабінет\n  --> ')
    skype = input('skype:\n  --> ')
    return {'Firs Name': firs_name, 'Last Name':last_name, 'Age':age, 'Tel': tel, 'Email': email,
            'Post': post, 'Number cabinet': number_cabinet, 'Skype': skype}

def menu_third():
    print('\nЗробіть ваш вибір\n'
          '1.Добавити працівника\n'
          '2.Видалити працівника\n'
          '3.Пошук працівника за критеріями\n'
          '4.Замінити інфу працівника\n'
          '5.Показати працівників\n'
          '6.Вихід')
    return input('  --> ')

def main_third():
    c = 0
    choose = ''
    while not choose.startswith('6'):
        choose = menu_third()

        if choose.startswith('1'):
            firma[len(firma)+1] = add_person()

        elif choose.startswith('2'):
            last_name = input('Введіть Призвіще для пошуку\n  --> ')
            for k, v in firma.items():
                if last_name in v['Last Name']:
                    del firma[k]
                    print('\n*************** Видалено ******************\n')
                    break
                else:
                    c += 1
            print('\nТакого Призвіще неіснує\n')if c == len(firma) else True
            c = 0

        elif choose.startswith('3'):
            print('\n1.Пошук працівника за призвіщем\n'
                  '2.Пошук працівника за віком\n'
                  '3.Пошук прцівника за першою буквою Призвіща\n'
                  )
            choose_search = int(input('Ваш вибір\n  --> '))
            if choose_search == 1:
                last_name = input('\nВведіть Призвіще для пошуку\n  --> ')
                for k, v in firma.items():
                    if last_name == v['Last Name']:
                        print(f'\nПрацівник : {k}', end=" ")
                        infoEmployee = f'\nПрацівник : {k}'
                        for k1, v1 in v.items():
                            print(f'\n\t {k1} : {v1}', end=' ')
                            infoEmployee += f'\n\t {k1} : {v1}'
                        print()
                        with open('Пошук.txt', 'a+') as f:
                            f.write(infoEmployee)
                        print()
                    else:
                        c += 1
                print('\nНевідоме Призвіще\n') if c == len(firma) else True
                c = 0

            elif choose_search == 2:
                age = str(input('Введіть Вік для пошуку\n  --> '))
                for k, v in firma.items():
                    if age in v['Age']:
                        print(f'\nПрацівник : {k}', end=" ")
                        infoEmployee = f'\nПрацівник : {k}'
                        for k1, v1 in v.items():
                            print(f'\n\t {k1} : {v1}', end=' ')
                            infoEmployee += f'\n\t {k1} : {v1}'
                        print()
                        with open('Пошук.txt', 'a+') as f:
                            f.write(infoEmployee)
                    else:
                        c += 1
                print('\nНевідомий Вік\n')if c == len(firma) else True
                c = 0


            elif choose_search == 3:
                letter = str(input('Введіть першу букву Призвіща для пошуку\n  --> '))
                for k, v in firma.items():
                    if letter in v['Last Name']:
                        print(f'\nПрацівник : {k}', end=" ")
                        infoEmployee = f'\nПрацівник : {k}'
                        for k1, v1 in v.items():
                            print(f'\n\t {k1} : {v1}', end=' ')
                            infoEmployee += f'\n\t {k1} : {v1}'
                        print()
                        with open('Пошук.txt', 'a+') as f:
                            f.write(infoEmployee)

                    else:
                        c += 1
                print('\nТакої немає\n')if c == len(firma) else True
                c = 0
            else:
                print('********* Помилка вводу **********')
        elif choose.startswith('4'):
            last_name = input('Введіть Призвіще для зміни\n  --> ')
            for k, v in firma.items():
                if last_name in v['Last Name']:
                    print('\nВнесіть зміни\n')
                    firma[k] = add_person()
                else:
                    print('Такого Призвіща неіснує')
        elif choose.startswith('5'):
            for k, v in firma.items():
                print(f'\nПрацівник : {k}', end=" ")
                for k1, v1 in v.items():
                     print(f'\n\t {k1} : {v1}', end=' ')
            print()
        elif choose.startswith('6'):
            with open("Працівники.json", 'w') as f:
                f.write(json.dumps(firma, indent=4))
            print("\n************ Кінець *************")
        else:
            print('********* Помилка вводу **********')

main_third()

