import hashlib
import json
import msvcrt
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

        if not login :
            self.login = input('please write login: ')
        if not password :
            self.password = input('please write password: ')
        self.first_name = input('please write first name: ')
        self.last_name = input('please write last name: ')
        self.address = input('please write address: ')
        self.tel = input('please write tel: ')

        user_data.update({str(len(user_data) + 1): {'login': login if login else self.login,
                                                    'password': password if password else self.password,
                                                    'first_name': self.first_name,
                                                    'last_name': self.last_name, 'address': self.address,
                                                    'tel': self.tel, 'passed_test': self.passed_test,
                                                    'pending_tests': self.pending_tests}})

        loading_toJSON(user_data, USERS_FILE_DIRECTORY)


class Admin(Person):
    def __init__(self, login = None, password = None):
        super().__init__(login, password)

    def registration(self):
        self.login = input('please write login: ')
        self.password = input('please write password: ')
        loading_toJSON({'login': self.login, 'password': self.password}, ADMIN_FILE_DIRECTORY)

    def filling(self,login,password):
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

        self.section = input('Write section to test: ')
        self.exam_name = input('Write exam name: ')

        question.append(input('Write question: '))
        answer.append(list(input('Write answer: ').split(',')))
        true_answer.append(input('Write true answer: '))

        quest = {"quests": question,
                 "answer": answer,
                 "true_answer": true_answer
                 }

        self.test_dict = quest
        test_data.update(
            {'section': self.section, 'exam_name': self.exam_name, 'test_dict': self.test_dict})

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
    except  Exception as e:
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
            print(f"Quest: {test_data['test_dict']['quests'][x]}")
            print(f"1.{test_data['test_dict']['answer'][x][0]}")
            print(f"2.{test_data['test_dict']['answer'][x][1]}")
            print(f"3.{test_data['test_dict']['answer'][x][2]}")

            user_answer.append(input('Write your answer: '))

            to_json = {'section': test_data['section'],
                       'exam_name': test_data['exam_name'], 'user_answer': user_answer}
            x += 1

    if 'exit' in user_answer:
        user_answer.remove('exit')
        user_data[str(array_login.index(login_user) + 1)]['pending_tests'] = to_json
        loading_toJSON(user_data, USERS_FILE_DIRECTORY)
    else:
        print("COMPLETED")
        t = 0
        for y in range(0, len(user_answer)):
            if user_answer[y] == test_data['test_dict']['true_answer'][y]:
                t += 1
        to_json.update({'grade': (12 * t) / len(user_answer)})
        user_data[str(array_login.index(login_user) + 1)]['passed_test'] = to_json
        user_data[str(array_login.index(login_user) + 1)]['pending_tests'] = ""
        loading_toJSON(user_data, USERS_FILE_DIRECTORY)

def check_result(login):
    print('your result')
    result = user_data[str(find_keys_in_all(user_data,'login').index(login) + 1)]['passed_test']
    print(f'section: {result["section"]}')
    print(f'exam name: {result["exam_name"]}')
    print(f'grade: {result["grade"]}')
    for y in range(0, len(test_data['test_dict']['true_answer'])):
        if test_data['test_dict']['true_answer'][y] == result['user_answer'][y]:
            print(f"{y+1}. {test_data['test_dict']['quests'][y]} -> {result['user_answer'][y]}: ответ верный")
        else:
            print(f"{y+1}. {test_data['test_dict']['quests'][y]} -> {result['user_answer'][y]}: ответ не верный")
    print()


admin_data = unloading_toJSON(ADMIN_FILE_DIRECTORY)
user_data = unloading_toJSON(USERS_FILE_DIRECTORY)
test_data = unloading_toJSON(TESTS_FILE_DIRECTORY)

# print(admin_data)
# print(user_data
#
# a = Admin()
# a.filling(admin_data['login'],admin_data['password'])



print('who are you?\n1.User\n2.Admin\n3.Exit')
main_choice = int(input('Choose: '))

while main_choice != 3:
    # TODO User
    if main_choice == 1:

        user = User()
        print('Pleace, enter login and password')
        login_user, password_user = [encoded_name('please write login: '), encoded_name('please write password: ')]

        check_login = find_keys_in_all(user_data, 'login')
        check_password = find_keys_in_all(user_data, 'password')

        if login_user in check_login and password_user in check_password:

            print('Welcom user')
            print('1.Take the test\n2.Finish failed tests\n3.View Results')

            user_choice_test = int(input('Choose: '))

            # TODO Take the test
            if user_choice_test == 1:

                print(f'1.{test_data["section"]}')

                user_choice_test_section = int(input('Choose: '))

                if user_choice_test_section == 1:
                    print(f'you choose {test_data["section"]}')
                    passing_test(check_login,login_user)

            # TODO Finish failed tests
            elif user_choice_test == 2:
                if len(user_data[str(check_login.index(login_user) + 1)]['pending_tests']) > 0:
                    pend_test = user_data[str(check_login.index(login_user) + 1)]['pending_tests']
                    print('У вас есть не законченны тесты')
                    print(pend_test)
                    print(pend_test['section']+' -> '+pend_test['exam_name'])
                    passing_test(check_login,login_user)

            # TODO View Results
            elif user_choice_test == 3:
                try:
                    check_result(login_user)
                except:
                    print('no tests passed')

        else:
            print('new user please register ->')
            user.registration(login=login_user,password=password_user)
            user_data = unloading_toJSON(USERS_FILE_DIRECTORY)

        print('who are you?\n1.User\n2.Admin\n3.Exit')

    # TODO Admin
    elif main_choice == 2:
        admin = Admin()
        if not (os.path.isfile(f'{ADMIN_FILE_DIRECTORY}.json')):
            print('it\'s you first entrance')
            admin.registration()
        else:
            # TODO 'admin has already been created
            print('Pleace, enter login and password')
            l, p = [encoded_name('Enter login: '), encoded_name('Enter password: ')]

            admin_data = unloading_toJSON(ADMIN_FILE_DIRECTORY)

            if admin_data['login'] == l and admin_data['password'] == p:
                print('Welcom admin')
                print('1.Сhange login details\n'
                      '2.User management\n'
                      '3.View statistics\n'
                      '4.Test management\n'
                      '5.Return to menu above'
                      )
                admin_choise = int(input('Choose admin menu: '))
                while admin_choise != 5:
                    # TODO Сhange login details
                    if admin_choise == 1:
                        print('1.Change login\n2.Change password')
                        admin_choise_change_login_details = int(input('Choose change details: '))
                        if admin_choise_change_login_details == 1:
                            admin.login = input('write a new login: ')
                            admin_data['login'] = admin.login
                        elif admin_choise_change_login_details == 2:
                            admin.password = input('write a new password: ')
                            admin_data['password'] = admin.password
                        else:
                            print('Incorrect choise')
                        loading_toJSON(admin_data, ADMIN_FILE_DIRECTORY)
                    # TODO User management
                    if admin_choise == 2:
                        print('1.Creat new user\n2.Delete user\n3.Change user')
                        admin_choise_change_user = int(input('Choose change user: '))
                        user = User()
                        #TODO Creat new user
                        if admin_choise_change_user == 1:
                            user.registration()
                        #TODO Delete user
                        elif admin_choise_change_user == 2:
                            user_del = encoded_name('Please write login user then to delete him: ')
                            check = find_keys_in_all(user_data, 'login')
                            if user_del in check:
                                print('found delete now')
                                user_data.pop(str(check.index(user_del) + 1))
                            else:
                                print('user does not exist')
                        #TODO Change user
                        elif admin_choise_change_user == 3:
                            user_change = encoded_name('Please write login user then to change him data: ')
                            check = find_keys_in_all(user_data, 'login')
                            if user_change in check:
                                print('found now let\'s make changes')
                                print(user_data[str(check.index(user_change) + 1)].values())
                                print('what item do you want to change?')
                                print('1.login\n'
                                      '2.password\n'
                                      '3.First name\n'
                                      '4.Last name\n'
                                      '5.Address\n'
                                      '6.Tel\n'
                                      '7.Passed test\n'
                                      '8.Pending test')
                                change_user = int(input('Choose change: '))
                                change_list = ['login', 'password', 'first_name', 'last_name', 'addres', 'tel',
                                               'passed_test', 'pending_test']
                                value = input(f'{change_list[change_user - 1]}: ')
                                user_data[str(check.index(user_change) + 1)][change_list[change_user - 1]] = value
                            else:
                                print('user does not exist')
                        else:
                            print('Incorrect choise')
                        loading_toJSON(user_data, USERS_FILE_DIRECTORY)

                    # TODO  View statistics
                    if admin_choise == 3:
                        user_name = input('Enter user name: ')
                        check_name = find_keys_in_all(user_data,'first_name')
                        if user_name in check_name:
                            check_result(user_data[str(check_name.index(user_name)+1)]['login'])
                    # TODO Test management
                    if admin_choise == 4:
                        test = Test('', '', '')
                        test.input_question()

                    print('1.Сhange login details\n'
                          '2.User management\n'
                          '3.View statistics\n'
                          '4.Test management\n'
                          '5.Return to menu above'
                          )
                    admin_choise = int(input('Choose admin menu: '))
            else:
                print('Incorrect login or password')
        print('who are you?\n1.User\n2.Admin\n3.Exit')

    else:
        print('Incorrect choise')

    main_choice = int(input('Choose: '))