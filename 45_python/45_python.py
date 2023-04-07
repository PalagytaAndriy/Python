
import json
import time
from datetime import date
import sys

firma = {}
infoEmployee = ''

print('Loading base employees', end=' ')
for i in range(0,4):
    time.sleep(0.2)
    print(' . ', end='')
print()

with open("Employees.json",'r') as json_file:
    firma = json.load(json_file)

def add_person():
    firs_name = input('Enter a firs name: ')
    last_name = input('Enter a last name: ')
    age = input('Enter your age: ')
    tel = input('Enter a tel number: ')
    email = input('Enter a email: ')
    post = input('Enter a post: ')
    number_cabinet = input('Enter a number cabinet: ')
    skype = input('Enter a skype: ')
    return {'Firs Name':firs_name,'Last Name':last_name, 'Age':age, 'Tel':tel,'Email':email,
            'Post':post,'Number cabinet':number_cabinet,'Skype':skype}

def menu_third():
    print('Choose action:\n'
          '1.Add a information of employee\n'
          '2.Remove a information of employee\n'
          '3.Finding information about an employee for last name\\age or first letter\n'
          '4.Replace a information of employee\n'
          '5.Show information of employees\n'
          '6.Exit')
    return input('Enter choose: ')

def main_third():
    c = 0
    choose = ''
    while not choose.startswith('6'):
        choose = menu_third()
        if choose.startswith('1'):
            firma[len(firma)+1] = add_person()
        elif choose.startswith('2'):
            last_name = input('Enter a last name employee: ')
            for k,v in firma.items():
                if last_name in v['Last Name']:
                    del firma[k]
                    break
                else:
                    print('Unknown Last name')
        elif choose.startswith('3'):
            print('Choose action:\n'
                  '1.Finding information about an employee for last name\n'
                  '2.Finding information about an employee for age\n'
                  '3.Finding information about an employee for first letter'
                  )
            choose_search = int(input('Enter choose: '))
            if choose_search == 1:
                last_name = input('Enter a last name employee: ')
                for k, v in firma.items():
                    if last_name == v['Last Name']:
                        print(f'\nPerson: {k} Info ', end=" ")
                        infoEmployee = f'\nPerson: {k} Info '
                        for k1, v1 in v.items():
                            print(f'\n\t {k1} : {v1}', end=' ')
                            infoEmployee += f'\n\t {k1} : {v1}'
                        print()
                        with open(f'SearchedEmployee{date.today()}.txt', 'a+') as f:
                            f.write(infoEmployee)
                        print()
                    else:
                        c += 1
                print('\nUnknown Last name\n') if c ==  len(firma) else True
                c = 0

            elif choose_search == 2:
                age = str(input('Enter a age: '))
                for k, v in firma.items():
                    if age in v['Age']:
                        print(f'\nPerson: {k} Info ', end=" ")
                        infoEmployee = f'\nPerson: {k} Info '
                        for k1, v1 in v.items():
                            print(f'\n\t {k1} : {v1}', end=' ')
                            infoEmployee += f'\n\t {k1} : {v1}'
                        print()
                        with open(f'SearchedEmployee{date.today()}.txt', 'a+') as f:
                            f.write(infoEmployee)
                    else:
                        c += 1
                print('\nUnknown Last name\n') if c == len(firma) else True
                c = 0

            elif choose_search == 3:
                first_letter =  str(input('Enter a first letter employees: '))
                for k, v in firma.items():
                    if first_letter in v['Last Name']:
                        print(f'\nPerson: {k} Info ', end=" ")
                        infoEmployee = f'\nPerson: {k} Info '
                        for k1, v1 in v.items():
                            print(f'\n\t {k1} : {v1}', end=' ')
                            infoEmployee += f'\n\t {k1} : {v1}'
                        print()
                        with open(f'SearchedEmployee{date.today()}.txt', 'a+') as f:
                            f.write(infoEmployee)
                    else:
                        c += 1
                print('\nUnknown Last name\n') if c == len(firma) else True
                c = 0
            else:
                print('Error')
        elif choose.startswith('4'):
            last_name = input('Enter a last name: ')
            for k, v in firma.items():
                if last_name in v['Last Name']:
                    print('Please, not write to new information about employee')
                    firma[k] = add_person()
                else:
                    print('Unknown Last name')
        elif choose.startswith('5'):
            for k,v in firma.items():
                print(f'\nPerson: {k} Info ', end=" ")
                for  k1,v1 in v.items():
                     print(f'\n\t {k1} : {v1}' ,end=' ')
            print()
        elif choose.startswith('6'):
            with open("Employees.json", 'w') as f:
                f.write(json.dumps(firma, indent=4))
            print("Good buy")
        else:
            print('Error')
if __name__ == '__main__':
    main_third()