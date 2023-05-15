# 6040088286:AAGSR-tD1fn1xUE03c0xmzhutipK0G6rJC0
import datetime
import random

import telebot
from telebot import types

Api_url = 'https://www.omdbapi.com/'
Api_key = '55f2a631'

bot = telebot.TeleBot('6040088286:AAGSR-tD1fn1xUE03c0xmzhutipK0G6rJC0')



#    завдання 3

@bot.message_handler(commands=['Письменник'])
def send_welcome(message):
    print(message)

    bot.reply_to(message, 'Гемінґвей')


@bot.message_handler(commands=['Поет'])
def send_welcome(message):
    print(message)

    bot.reply_to(message, 'Шекспір')

@bot.message_handler(commands=['Поет'])
def send_welcome(message):
    print(message)

    bot.reply_to(message, 'Книга')

@bot.message_handler(commands=['Поет'])
def send_welcome(message):
    print(message)

    bot.reply_to(message, 'Три товариші')

@bot.message_handler(commands=['Монолог'])
def send_welcome(message):
    print(message)

    bot.reply_to(message, 'Бути чи не бути')



#    завдання 4






@bot.message_handler(commands=['Монолог'])
def send_welcome(message):
    print(message)
    monolog = ['Наступив час, коли абітурієнти вже мали обрати програму на творчій іспит! Але можливо є ті учні, які тільки починають обирати програму! Театрали мають великий досвід в цьому питанні і підкажуть на що звернути увагу! А для тих, хто вже обрав програму пропонуємо звернути увагу на важливе ще раз!',
               'В своих интервью 1979—1980 годов Пугачёва сообщала, что в её планах — создание новой по концепции концертной программы и разработка нового сценического образа, существенно отличающегося от образа, создаваемого в программе «Женщина, которая поёт», к которому все привыкли',
               'Monolog может быть сконфигурирован так, чтобы отправлять электронное письмо при возникновении ошибки в приложении. Для этого конфигурация требует несколько вложенных обработчиков, чтобы избегать получения слишком большого количества писем. Эта конфигурация на первый взгляд выглядит сложной, но каждый обработчик достаточно простой и ясный, если его разобрать на составляющие.']
    bot.reply_to(message, random.choice(monolog))


@bot.message_handler(commands=['Поет'])
def send_welcome(message):
    print(message)
    poet = ['Аверинцев, Сергей Сергеевич', 'Азалаис де Поркайрагас', 'Азеведу, Артур']
    bot.reply_to(message, random.choice(poet))


@bot.message_handler(commands=['Книга'])
def send_welcome(message):
    print(message)
    book = ['Тёмные начала', 'Автостопом по галактике', 'Властелин колец']
    bot.reply_to(message, random.choice(book))


@bot.message_handler(commands=['Письменник'])
def send_welcome(message):
    print(message)
    pus = ['Тарас Шевченко', 'Іван Франко', 'Ліні Костенко']
    bot.reply_to(message, random.choice(pus))



bot.polling()