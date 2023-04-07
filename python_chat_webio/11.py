import asyncio

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import defer_call, info as session_info, run_async, run_js
import json
import os
chat_msgs = []
online_users = set()
online_users_password = set()
oll = set
ADMIN_FILE_DIRECTORY = 'admin_file'



MAX_MESSAGES_COUNT = 100




class User():
    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    def registration(self, login=None, password=None):
            self.login = login
            self.password = password

            user_d = unloading_toJSON(ADMIN_FILE_DIRECTORY)

            check_login = find_keys_in_all(user_d, 'login')
            check_password = find_keys_in_all(user_d, 'password')
            if check_login != self.login and check_password != self.password:
                user_d.update({str(len(user_d) + 1): {'login': login if login else self.login, 'password': password if password else self.password}})
                loading_toJSON(user_d, ADMIN_FILE_DIRECTORY)


async def main():
    global chat_msgs
    user = User()
    user_d = unloading_toJSON(ADMIN_FILE_DIRECTORY)


    put_markdown("## 🧊 Онлайн чат!\nИсходный код данного чата укладывается в 100 строк кода!")
    put_markdown(f"##  Закрити онлайн чат! для {len(user_d)} користувачів\n ")


    msg_box = output()
    put_scrollable(msg_box, height=300, keep_bottom=True)


    nickname = await input("Увійти в чат -- login --", required=True, placeholder="Ваше имя",
                           validate=lambda n: "Такой ник уже используется!" if n in online_users or n == '📢' else None)

    password = await input("Увійти в чат -- password --", required=True, placeholder="Пароль",
                           validate=lambda
                               nn: "Такой ник уже используется!" if nn in online_users_password or nn == '📢' else None)


    check_login = find_keys_in_all(user_d, 'login')
    check_password = find_keys_in_all(user_d, 'password')
    k = 0
    for ii in range(len(user_d)):
        if check_login[ii] == nickname and check_password[ii] == password:
            k += 1
    if k == 0:
        nickname = await input("Регістрація в чат -- login --", required=True, placeholder="Ваше имя",
                                        validate=lambda
                                            n: "Такой ник уже используется!" if n in user_d or n == '📢' else None)
        if nickname in check_login:

            put_buttons(['------ Такий нік вже зайнятий -------- Перезайти ---------'], onclick=lambda btn: run_js('window.location.reload()'))
        else:

            password = await input("Регістрація в чат -- password --", required=True, placeholder="Пароль",
                                         validate=lambda
                                             nn: "Такой ник уже используется!" if nn in online_users_password or nn == '📢' else None)
            if nickname in check_login:
                n = await input("Такий логін вже існує", required=True, placeholder="Ваше имя",
                                   validate=lambda
                                       n: "Такой ник уже используется!" if n in user_d or n == '📢' else None)
            else:
                user.registration(nickname, password)

    #user_d = unloading_toJSON(ADMIN_FILE_DIRECTORY)

    check_login = find_keys_in_all(user_d, 'login')
    check_password = find_keys_in_all(user_d, 'password')

    k = 0
    for ii in range(len(user_d)):
        if check_login[ii] == nickname and check_password[ii] == password:
            k += 1
    if k == 1:

        chat_msgs.append(('📢', f'`{nickname} ` присоединился к чату!'))
        msg_box.append(put_markdown(f'📢 `{nickname} ` присоединился к чату'))

        refresh_task = run_async(refresh_msg(nickname, msg_box))

        while True:
            data = await input_group("💭 Новое сообщение", [
                input(placeholder="Текст сообщения ...", name="msg"),
                actions(name="cmd", buttons=["Отправить", {'label': "Выйти из чата", 'type': 'cancel'}])
            ], validate=lambda m: ('msg', "Введите текст сообщения!") if m["cmd"] == "Отправить" and not m['msg'] else None)

            if data is None:
                break

            msg_box.append(put_markdown(f"`{nickname}`: {data['msg']}"))
            chat_msgs.append((nickname, data['msg']))

        refresh_task.close()

                                    #online_users.remove(nickname)
        toast("Вы вышли из чата!")
        msg_box.append(put_markdown(f'📢 Пользователь `{nickname}` покинул чат!'))
        chat_msgs.append(('📢', f'Пользователь `{nickname}` покинул чат!'))

        put_buttons(['Перезайти'], onclick=lambda btn: run_js('window.location.reload()'))


async def refresh_msg(nickname, msg_box):
    global chat_msgs
    last_idx = len(chat_msgs)

    while True:
        global user_data
        await asyncio.sleep(1)

        for m in chat_msgs[last_idx:]:
            if m[0] != nickname:  # if not a message from current user
                msg_box.append(put_markdown(f"`{m[0]}`: {m[1]}"))

        # remove expired
        if len(chat_msgs) > MAX_MESSAGES_COUNT:
            chat_msgs = chat_msgs[len(chat_msgs) // 2:]

        last_idx = len(chat_msgs)


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
    except Exception as e:
        print(f'Error: {str(e)}')
        return {}

def find_keys_in_all(dict, key):
    return [dict[i][key] for i in dict.keys()]


if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False)