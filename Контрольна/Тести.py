import hashlib
import json
import os

ADMIN_FILE_DIRECTORY = 'admin_file'
USERS_FILE_DIRECTORY = 'users_file'
TESTS_FILE_DIRECTORY = 'tests_file'


class Person:

    def __init__(self, login, password):
        self._login = login
        self._password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = str(hashlib.md5(value.encode('ascii')).digest())


    @login.deleter
    def login(self):
        del self._login

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = str(hashlib.md5(value.encode('ascii')).digest())

    @password.deleter
    def password(self):
        del self._password


class User(Person):

    def __init__(self, login = None, password = None, first_name = None, last_name = None, address = None,
                 tel = None, passed_test = None, pending_tests = None):
        super().__init__(login, password)
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.tel = tel
        self.passed_test = passed_test
        self.pending_tests = pending_tests

    def registration(self,login = None, password =None):

        if not login:
            self.login = input('Введіть логін'
                               '\n --> ')
        if not password:
            self.password = input('Введіть пароль'
                                  '\n --> ')
        self.first_name = input('Введіть імя'
                                '\n --> ')
        self.last_name = input('Введіть призвіще'
                               '\n --> ')
        self.address = input('Введіть адрес'
                             '\n --> ')
        self.tel = input('Ведіть тел.'
                         '\n --> ')

        user_data.update({str(len(user_data) + 1): {'login': login if login else self.login,
                                                    'password': password if password else self.password,
                                                    'first_name': self.first_name,
                                                    'last_name': self.last_name,
                                                    'address': self.address,
                                                    'tel': self.tel,
                                                    'passed_test': self.passed_test,
                                                    'pending_tests': self.pending_tests}})

        loading_toJSON(user_data, USERS_FILE_DIRECTORY)


class Admin(Person):
    def __init__(self, login=None, password=None):
        super().__init__(login, password)

    def registration(self):
        self.login = input('Введіть логін'
                           '\n --> ')
        self.password = input('Введіть пароль'
                              '\n --> ')
        loading_toJSON({'login': self.login, 'password': self.password}, ADMIN_FILE_DIRECTORY)

    def filling(self, login, password):
        self.login = login
        self.password = password

class Test:

    def __init__(self, section, exam_name, test_dict):
        self._section = section
        self._exam_name = exam_name
        self._test_dict = test_dict

    @property
    def section(self):
        return self._section

    @section.setter
    def section(self, value):
        self._section = value

    @section.deleter
    def section(self):
        del self._section

    @property
    def exam_name(self):
        return self._exam_name

    @exam_name.setter
    def exam_name(self, value):
        self._exam_name = value

    @exam_name.deleter
    def exam_name(self):
        del self._exam_name

    @property
    def test_dict(self):
        return self._test_dict

    @test_dict.setter
    def test_dict(self, value):
        self._test_dict = value

    @test_dict.deleter
    def test_dict(self):
        del self._test_dict

    def input_question(self):
        question = []
        answer = []
        true_answer = []

        self.section = input('Введіть тему для  запитання'
                             '\n --> ')
        self.exam_name = input('Введіть назву теми запитаннь'
                               '\n --> ')

        question.append(input('Введіть запитання'
                              '\n --> '))
        answer.append(list(input('Ведіть відповіді'
                                 '\n --> ').split(',')))
        true_answer.append(input('Ведіть правильну відповідь'
                                 '\n --> '))

        quest = {"quests": question,
                 "answer": answer,
                 "true_answer": true_answer}

        self.test_dict = quest
        test_data.update({'section': self.section, 'exam_name': self.exam_name, 'test_dict': self.test_dict})

        if os.path.isfile(f'{TESTS_FILE_DIRECTORY}.json') and os.access(f'{TESTS_FILE_DIRECTORY}.json', os.R_OK):

            data = unloading_toJSON(TESTS_FILE_DIRECTORY)

            data['test_dict']['quests'].extend(question)
            data['test_dict']['answer'].extend(answer)
            data['test_dict']['true_answer'].extend(true_answer)

            loading_toJSON(data, TESTS_FILE_DIRECTORY)
        else:
            loading_toJSON(test_data, TESTS_FILE_DIRECTORY)


def loading_toJSON(value, directory):
    try:
        with open(f'{directory}.json', 'w') as write_file:
            json.dump(value, write_file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f'Error: {str(e)}')


def unloading_toJSON(directory):
    try:
        with open(f'{directory}.json', "r") as read_file:
            return json.load(read_file)
    except  Exception as e:
        print(f'Error: {str(e)}')
        return {}


def find_keys_in_all(dict, key):
    return [dict[i][key] for i in dict.keys()]


def encoded_name(commnet):
    return str(hashlib.md5(input(f'{commnet}').encode('ascii')).digest())

def passing_test(array_login,login_user):

    to_json = dict

    try:
        if len(user_data[str(array_login.index(login_user) + 1)]['pending_tests']['user_answer']) > 0:
            x = len(user_data[str(array_login.index(login_user) + 1)]['pending_tests']['user_answer'])
            user_answer = user_data[str(array_login.index(login_user) + 1)]['pending_tests']['user_answer'].copy()

    except:
        x = 0
        user_answer = []

    while x < len(test_data['test_dict']['quests']) and 'exit' not in user_answer:

        if x < len(test_data['test_dict']['quests']):
            print(f"Запитання: {test_data['test_dict']['quests'][x]}")
            print(f"1.{test_data['test_dict']['answer'][x][0]}")
            print(f"2.{test_data['test_dict']['answer'][x][1]}")
            print(f"3.{test_data['test_dict']['answer'][x][2]}")

            user_answer.append(input('Введіть вашу відповідь або -- exit -- для виходу з тесту'
                                     '\n --> '))

            to_json = {'section': test_data['section'], 'exam_name': test_data['exam_name'], 'user_answer': user_answer}
            x += 1

    if 'exit' in user_answer:
        user_answer.remove('exit')
        user_data[str(array_login.index(login_user) + 1)]['pending_tests'] = to_json
        loading_toJSON(user_data, USERS_FILE_DIRECTORY)
    else:
        print("-------------------- Готово ----------------------")
        t = 0
        for y in range(0, len(user_answer)):
            if user_answer[y] == test_data['test_dict']['true_answer'][y]:
                t += 1
        to_json.update({'grade': (12 * t) / len(user_answer)})
        user_data[str(array_login.index(login_user) + 1)]['passed_test'] = to_json
        user_data[str(array_login.index(login_user) + 1)]['pending_tests'] = ""
        loading_toJSON(user_data, USERS_FILE_DIRECTORY)

def check_result(login):
    print('-------------------- Ваш результат --------------------\n')
    result = user_data[str(find_keys_in_all(user_data, 'login').index(login) + 1)]['passed_test']
    print(f'Секція: {result["section"]}')
    print(f'Тема: {result["exam_name"]}')
    print(f'Бали: {result["grade"]}')
    for y in range(0, len(test_data['test_dict']['true_answer'])):
        if test_data['test_dict']['true_answer'][y] == result['user_answer'][y]:
            print(f"{y+1}. {test_data['test_dict']['quests'][y]} -> {result['user_answer'][y]} -->  вірно")
        else:
            print(f"{y+1}. {test_data['test_dict']['quests'][y]} -> {result['user_answer'][y]} --> НЕ вірно")
    print()


admin_data = unloading_toJSON(ADMIN_FILE_DIRECTORY)
user_data = unloading_toJSON(USERS_FILE_DIRECTORY)
test_data = unloading_toJSON(TESTS_FILE_DIRECTORY)


print('Хто ви ?\n'
      '1.User\n'
      '2.Admin\n'
      '3.Вихід\n')
main_choice = str(input('Ваш вибір'
                        '\n --> '))

while main_choice != '3':
    if main_choice == '1':

        user = User()
        print('Введіть ваш логін і пароль\n')
        login_user, password_user = [encoded_name('Введіть ваш логін'
                                                  '\n --> '), encoded_name('Введіть ваш пароль'
                                                                           '\n --> ')]

        check_login = find_keys_in_all(user_data, 'login')
        check_password = find_keys_in_all(user_data, 'password')

        if login_user in check_login and password_user in check_password:
            print(f'--------- Вітаю  user ----------\n')
            print('1.Пройти тестування\n'
                  '2.Закіньчити непройдене тестування\n'
                  '3.Показати результат\n')

            user_choice_test = str(input('Введіть ваш вибір'
                                         '\n --> '))

            if user_choice_test == '1':

                print(f'1.{test_data["section"]}')

                user_choice_test_section = str(input('Введіть ваш вибір '
                                                     '\n --> '))

                if user_choice_test_section == '1':
                    print(f'Ваш вибір --> {test_data["section"]}')
                    passing_test(check_login, login_user)

            elif user_choice_test == '2':
                if len(user_data[str(check_login.index(login_user) + 1)]['pending_tests']) > 0:
                    pend_test = user_data[str(check_login.index(login_user) + 1)]['pending_tests']
                    print('У вас є непройдені  тести')
                    print(pend_test)
                    print(pend_test['section']+' --> '+pend_test['exam_name'])
                    passing_test(check_login, login_user)
                else:
                    print('\nУ вас немає непройдених тестів\n')

            elif user_choice_test == '3':
                try:
                    check_result(login_user)
                except:
                    print('Немає пройдених тестів\n')

        else:
            print('Такого юзера неіснує \n')
            print('Новий user зареєструйся\n')
            user.registration(login = login_user, password = password_user)
            user_data = unloading_toJSON(USERS_FILE_DIRECTORY)

        print('Хто ви ?\n'
              '1.User\n'
              '2.Admin\n'
              '3.Вихід')




    elif main_choice == '2':
        admin = Admin()
        if not (os.path.isfile(f'{ADMIN_FILE_DIRECTORY}.json')):
            print('Це перший вхід для Аdmin\n')
            admin.registration()
        else:

            print('Введіть ваш логін і пароль\n')
            l, p = [encoded_name('Введіть логін'
                                 '\n --> '), encoded_name('Введіть пароль'
                                                          '\n --> ')]

            admin_data = unloading_toJSON(ADMIN_FILE_DIRECTORY)

            if admin_data['login'] == str(l) and admin_data['password'] == str(p):
                print('Вітаю Аdmin\n')
                print('1.Змінити логін і пароль Адміна\n'
                      '2.Керування Юзерами\n'
                      '3.Статистика\n'
                      '4.Добавити тести або --- exit -----\n'
                      '5.Вихід у перше меню\n')
                admin_choise = str(input('Ваш вибір'
                                         '\n --> '))
                while admin_choise != '5':

                    if admin_choise == '1':
                        print('1.Змінити логін\n'
                              '2.Змінити пароль\n'
                              '3.Вихід у перше  меню\n')

                        admin_choise_change_login_details = str(input('Ваш вибір'
                                                                      '\n --> '))
                        if admin_choise_change_login_details == '1':
                            admin.login = input('Введіть новий логін'
                                                '\n --> ')
                            admin_data['login'] = admin.login
                        elif admin_choise_change_login_details == '2':
                            admin.password = input('Введіть новий пароль'
                                                    '\n --> ')
                            admin_data['password'] = admin.password

                        elif admin_choise_change_login_details == '3':
                            break



                        else:
                            print('Некоректний ввід')

                        loading_toJSON(admin_data, ADMIN_FILE_DIRECTORY)

                    if admin_choise == '2':
                        print('1.Добавити юзера\n'
                              '2.Видалити юзера\n'
                              '3.Внести зміни в інфу юзера\n')

                        admin_choise_change_user = str(input('Введіть імя user'
                                                             '\n --> '))
                        user = User()

                        if admin_choise_change_user == '1':
                            user.registration()

                        elif admin_choise_change_user == '2':
                            user_del = encoded_name('Введіть логін Юзера для видалення'
                                                    '\n --> ')
                            check = find_keys_in_all(user_data, 'login')
                            if user_del in check:
                                print('\n----------- Видалено --------------')
                                user_data.pop(str(check.index(user_del) + 1))
                            else:
                                print('Такого юзера неіснує')

                        elif admin_choise_change_user == '3':
                            user_change = encoded_name('Введіть логін юзера для пошуку і зміни ')
                            check = find_keys_in_all(user_data, 'login')
                            if user_change in check:
                                print('Що в інфі юзера ви хочете змінити ???')
                                print('1.Логін\n'
                                      '2.Пароль\n'
                                      '3.Імя\n'
                                      '4.Призвіще\n'
                                      '5.Адрес\n'
                                      '6.тел\n'
                                      '7.Пройдені тести\n'
                                      '8.НЕ пройдені тести')
                                change_user = int(input('Введіть ваш вибір'
                                                        '\n --> '))
                                change_list = ['login', 'password', 'first_name', 'last_name', 'addres', 'tel',
                                               'passed_test', 'pending_test']
                                value = input(f'{change_list[change_user - 1]}: ')
                                user_data[str(check.index(user_change) + 1)][change_list[change_user - 1]] = value
                            else:
                                print('Такого юзера НЕ існує')
                        else:
                            print('Некоректний ввід\n')
                        loading_toJSON(user_data, USERS_FILE_DIRECTORY)


                    if admin_choise == '3':
                        user_name = str(input('Введіть імя user'
                                              '\n --> '))
                        check_name = find_keys_in_all(user_data, 'first_name')
                        if user_name in check_name:
                            check_result(user_data[str(check_name.index(user_name)+1)]['login'])
                        else:
                            print('Некоректне імя юзера\n')

                    if admin_choise == '4':
                        test = Test('', '', '')
                        test.input_question()
                        break
            else:
                print('Не вірний логін і пароль Адміна\n')
        print('Хто ви ?\n'
              '1.User\n'
              '2.Admin\n'
              '3.Вихід')

    else:
        print('---------- Невірний ввід -------------')

    main_choice = str(input('\nВаш вибір'
                            '\n --> '))

