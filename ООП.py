# Описание режима работы для Администратора (в дальнейшем админ):
# ■ В системе может быть только один админ, логин и пароль админа задается при
# первом входе в программу.
# ■ В дальнейшем пароль и логин можно изменить (но данную возможность имеет
# только админ).
# ■ Пароль и логин необходимо хранить только в зашифрованном виде.
# ■ При работе с системой админ имеет следующие возможности:
# ▶ Управление пользователями — создание, удаление, модификация
# пользователей.
# ▶ Просмотр статистики — просмотр результатов тестирования в общем по
# категориям, по конкретным тестам, по конкретным пользователям. Результаты
# просмотра статистики можно вывести в файл.
# ▶ Управление тестированием — админ имеет возможность добавлять
# категории,тесты, вопросы к тестам, задавать правильные и неправильные
# ответы, импортировать и экспортировать категории и тесты с вопросами из
# файла (и в файл)

# ■ При регистрации нужно указывать Ф.И.О., домашний адрес, телефон.
import os
import pickle
ADMIN_FILENAME = 'admin.bin'
USERS_FILENAME = 'users.bin'

users = []


class User:

    def __init__(self):
        self.__fullname = input("Будь ласка, введіть ім'я користувача ")
        self.__address = input("Будь ласка, введіть адресу користувача ")
        self.__phone = input("Будь ласка, введіть телефон користувача ")
        self.__login = input("Будь ласка, придумайте логін користувача ")
        self.__password = input("Будь ласка, придумайте пароль користувача ")
    def __str__(self):
        return f"{self.__fullname}\n{self.__address}\n{self.__phone}\n{self.__login}\n{self.__password}"
    def set_fullname(self):
        self.__fullname = input("Будь ласка, введіть нове ім'я користувача ")
    def set_address(self):
        self.__address = input("Будь ласка, введіть нову адресу користувача ")
    def set_phone(self):
        self.__phone = input("Будь ласка, введіть новий телефон користувача ")
    def set_login(self):
        self.__login = input("Будь ласка, введіть новий логін користувача ")
    def set_password(self):
        self.__password = input("Будь ласка, введіть новий пароль користувача ")
    def get__fullname(self):
        return self.__fullname
    def get__address(self):
        return self.__address
    def get__phone(self):
        return self.__phone
    def get__login(self):
        return self.__login
    def get__password(self):
        return self.__password


class Admin:

    __login = None
    __password = None


    def set_login(self):
        login = input("Будь ласка, введіть новий логін ")
        self.__login = login

    def set_password(self):
        password = input("Будь ласка, введіть новий пароль ")
        self.__password = password

    def get_login(self):
        return self.__login
    def get_password(self):
        return self.__password

def admin_menu():
    ex = False
    while ex != True:
        res = input("\n1. Змінити логін\n"
              "2. Змінити пароль\n"
              "3. Створити користувача\n"
              "4. Змінити дані користувача\n"
              "5. Видалити користувача\n"
              "6. Перегляд статистики\n"
              "7. Управління тестуванням\n"
              "8. Вихід\n")
        if res == "1" or res == "2" or res == "3" or res == "4" or res == "5" or res == "6" or res == "7"or res == "8":
            return res
            ex = True
        else:
            print("Помилка введення! Спробуйте ще!")

def search_user(user_login):
    with open(USERS_FILENAME, "rb") as file:
        global users
        users = pickle.load(file)
        index = 0
        for user in users:
            if user.get__login() == user_login:


                return index
            index += 1

        return None
def write_file_users():
    global  USERS_FILENAME
    global users
    try:
        with open(USERS_FILENAME, "wb") as file:
            pickle.dump(users, file)

    except Exception as ex:
        print(f"\n{ex}")
        exit()

if os.path.getsize(ADMIN_FILENAME) > 0:
    try:
        with open(ADMIN_FILENAME, "rb") as file:
            admin = pickle.load(file)
    except Exception as ex:
        print(f"\n{ex}")
        exit()
    print()
else:
    print("Вітаємо в системі тестування!\nЦе перший вхід!\nПотрібно зареструватись Адміністратору!\n\n")
    admin = Admin()
    admin.set_login()
    admin.set_password()
    try:
        with open(ADMIN_FILENAME, "wb") as file:
            pickle.dump(admin, file)
    except Exception as ex:
        print(f"\n{ex}")
        exit()

ex = False
while ex != True:
    ans = input("Виберіть режим:\n1 - Адміністратор\n2 - Пройти тести\n3 - Вихід\n")
    if ans == '1':
        log = input("Введіть логін ")
        if log == admin.get_login():
            pas = input("Введіть пароль ")
            if pas != admin.get_password():
                print("Невірний пароль!")
            else:
                print("Вітаємо! Ви зайшли в режимі адміністратора!")
                res=""
                while res != "8":
                    res = admin_menu()
                    if res == "1":
                        admin.set_login()
                        try:
                            with open(ADMIN_FILENAME, "wb") as file:
                                pickle.dump(admin, file)
                                print("Логін адміністратора успішно змінено")
                        except Exception as ex:
                            print(f"\n{ex}")
                            exit()
                    elif res == "2":
                        admin.set_password()
                        try:
                            with open(ADMIN_FILENAME, "wb") as file:
                                pickle.dump(admin, file)
                                print("Пароль адміністратора успішно змінено")
                        except Exception as ex:
                            print(f"\n{ex}")
                            exit()
                    elif res == "3":
                        user = User()
                        users.append(user)
                        write_file_users()
                        print(f"Користувача {user.get__login()} успішно створено")
                    elif res == "4":
                        l = input("Введіть логін користувача для пошуку в БД ")
                        i = search_user(l)
                        print(i)
                        if i != None:
                            print(f"Користувача {l} знайдено!")
                            while True:
                                data = input("Які дані потрібно змінити?\n\n"
                                             "1. ПІБ\n"
                                             "2. Адресу\n"
                                             "3. Телефон\n"
                                             "4. Логін\n"
                                             "5. Пароль\n"
                                             "6. Вийти\n")
                                if data == "1":
                                    users[i].set_fullname()
                                    write_file_users()
                                    print(f"ПІБ {users[i].get__login()} успішно змінено")
                                    break
                                elif data == "2":
                                    users[i].set_address()
                                    write_file_users()
                                    print(f"Адресу {users[i].get__login()} успішно змінено")
                                    break
                                elif data == "3":
                                    users[i].set_phone()
                                    write_file_users()
                                    print(f"Телефон {users[i].get__login()} успішно змінено")
                                    break
                                elif data == "4":
                                    users[i].set_login()
                                    write_file_users()
                                    print(f"Логін {users[i].get__login()} успішно змінено")
                                    break
                                elif data == "5":
                                    users[i].set_password()
                                    write_file_users()
                                    print(f"Пароль {users[i].get__login()} успішно змінено")
                                    break
                                elif data == "6":
                                    break
                                else:
                                    print("Помилка вводу, введіть цифру від 1 до 6")
                        else:
                            print(f"{l} не знайдено, спробуйте ще!")
                    elif res == "5":
                        pass
                    elif res == "6":
                        with open(USERS_FILENAME, "rb") as file:
                            users = pickle.load(file)
                            for user in users:
                                print(user)
                    elif res == "7":
                        pass
                    elif res == "8":
                        print("До побачення!")
        else:
            print("Невірний логін!")
        ex = True
    elif ans == "2":
        pass
        ex = True
    elif ans == "3":
        print("До побачення!")
        ex = True
    else:
        print("Помилка вводу! Введіть 1 або 2 \n")